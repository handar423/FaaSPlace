import time

from typing import List, Dict

import gevent
from config import config
from src.function_manager.container import Container
from src.function_manager.template_info import TemplateInfo
from gevent.lock import BoundedSemaphore
from src.function_manager.port_manager import PortManager
from src.workflow_manager.repository import Repository

repo = Repository()


class RequestInfo:
    def __init__(self, request_id, workflow_name, template_name, templates_infos, block_name, block_inputs,
                 block_infos):
        self.request_id = request_id
        self.workflow_name = workflow_name
        self.template_name = template_name
        self.templates_infos = templates_infos
        self.block_name = block_name
        self.block_inputs = block_inputs
        self.block_infos = block_infos
        # self.result = event.AsyncResult()
        self.arrival_time = time.time()
        self.cold_start_time = 0
        self.queuing_time = 0

idle_lifetime = 600

class Template:
    def __init__(self, client, template_info: TemplateInfo, port_manager: 
                 PortManager, parallel_limit, cpus, function_manager):
        self.client = client
        self.template_info = template_info
        self.port_manager = port_manager
        self.parallel_limit = parallel_limit
        self.cpus = cpus

        self.KAFKA_CHUNK_SIZE = None
        kafka_config = repo.get_kafka_config()
        if kafka_config is not None:
            self.KAFKA_CHUNK_SIZE = kafka_config['KAFKA_CHUNK_SIZE']
        self.num_processing = 0
        self.request_queue: List[RequestInfo] = []
        # lock may be useless!
        self.lock = BoundedSemaphore()
        self.num_exec = 0
        self.idle_containers: List[Container] = []
        # Todo: this need GC.
        self.requestID_block_container = {}
        self.requestIDs_container: Dict[str, Container] = {}
        self.function_manager = function_manager
        self.target_container_number = 0
        # 等于正在运行的和warm的和
        self.warm_container_number = 0
        self.working_container_number = 0

    def upd(self, request_id, block_name, container: Container):
        if request_id not in self.requestID_block_container:
            self.requestID_block_container[request_id] = {}
        self.requestID_block_container[request_id][block_name] = container

    def create_container(self, block_name):
        # self.lock.acquire()
        if self.num_exec > self.template_info.max_containers:
            # self.lock.release()
            return None
        self.num_exec += 1
        # self.lock.release()
        # st = time.time()
        try:
            container = Container.create(self.client,
                                         self.template_info.image_name,
                                         self.template_info.blocks.keys(),
                                         self.port_manager.allocate(),
                                         'exec',
                                         self.cpus,
                                         self.parallel_limit,
                                         self.KAFKA_CHUNK_SIZE)
        except Exception as e:
            print(e)
            self.num_exec -= 1
            return None
        # ed = time.time()
        # print('container cold start', ed - st)
        # self.lock.acquire()
        container.idle_blocks_cnt -= 1
        if container.idle_blocks_cnt > 0:
            self.idle_containers.append(container)
        # self.lock.release()
        # container.running_blocks.add(block_name)
        # self.init_container(container)
        return container

    def get_idle_container(self, block_name=None):
        assert block_name is not None
        # self.lock.acquire()
        for i in range(len(self.idle_containers)):
            if self.idle_containers[i].idle_blocks_cnt > 0:
                res = self.idle_containers[i]
                self.idle_containers[i].idle_blocks_cnt -= 1
                assert self.idle_containers[i].idle_blocks_cnt >= 0
                if self.idle_containers[i].idle_blocks_cnt == 0:
                    self.idle_containers.pop(i)
                return res
        else:
            return None

    def put_idle_container(self, container):
        # self.lock.acquire()
        self.idle_containers.append(container)
        # self.num_exec -= 1
        # self.lock.release()

    def run_block(self, container: Container, request: RequestInfo):
        # self.upd(request.request_id, request.block_name, container)
        st = time.time()
        transfer_time, inter_data_record = container.run_block(request.request_id, request.workflow_name, request.template_name,
                request.templates_infos, request.block_name, request.block_inputs, request.block_infos)
        ed = time.time()
        # print(request.request_id, request.template_name, transfer_time)
        if self.template_info.gc == 'True' or self.template_info.gc == True:
            container.run_gc()
        wait_time = transfer_time + request.cold_start_time
        gevent.spawn_later(wait_time, self.put_container, container)
        repo.save_latency(
            {'request_id': request.request_id, 'template_name': request.template_name, 'block_name': request.block_name,
             'phase': 'use_container', 'time': ed - st, 'st': st, 'ed': ed, 'cpu': self.cpus})
        repo.save_latency(
            {'request_id': request.request_id, 'template_name': request.template_name,
             'phase': 'detail_time_flag', 'timestamp': time.time(), 'duration_time': ed - st,
             'cold_start_time' : request.cold_start_time, 'data_time': transfer_time, 
             'queuing_time': request.queuing_time, 'arrive_time': request.arrival_time, 
             'st': st, 'ed': ed, 'intermediate_data_record': inter_data_record})

    def send_data(self, request_id, workflow_name, function_name, datas, datatype):
        self.requestIDs_container[request_id].send_data(request_id, workflow_name, function_name, datas, datatype)

    def allocate_block(self, request_id, workflow_name, template_name, templates_infos, block_name, block_inputs,
                       block_infos, scaling_index):
        request = RequestInfo(request_id, workflow_name, template_name, templates_infos, block_name, block_inputs,
                              block_infos, scaling_index)
        self.request_queue.append(request)

    def preempt_block(self, request_id, workflow_name, template_name, buddy_block_name, block_name, block_inputs,
                      block_infos):
        container: Container = self.requestID_block_container[request_id][buddy_block_name]
        self.lock.acquire()
        if block_name not in container.running_blocks:
            container.running_blocks.add(block_name)
            self.lock.release()
            print('preempt_block_success!->', request_id, workflow_name, template_name, block_name, '--[buddy_block]<-',
                  buddy_block_name)
            gevent.spawn(container.run_block, request_id, workflow_name, template_name, block_name, block_inputs,
                         block_infos)
            return True
        else:
            self.lock.release()
            return False
        pass

    # def run_function(self, request_id, workflow_name, function_name):
    #     self.requestIDs_container[request_id].run_function()
    #     print(function_name, workflow_name, request_id, ' finished!')
    #     self.put_idle_container(self.requestIDs_container[request_id])

    # def send_request(self, request_id, workflow_name, input_data, output_data):
    #     print('send_request() in function.py', request_id, self.function_info.function_name,
    #           time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    #     data = {'request_id': request_id,
    #             'workflow_name': workflow_name,
    #             'input_data': input_data,
    #             'output_data': output_data}
    #     request = RequestInfo(request_id, data)
    #     self.request_queue.append(request)
    #     # res = request.result.get()
    #     # return res

    # def allocate(self, request_id, workflow_name, function_name, function_info):
    #     data = {'request_id': request_id,
    #             'workflow_name': workflow_name,
    #             'function_name': function_name,
    #             'function_info': function_info}
    #     request = RequestInfo(request_id, workflow_name, function_name, function_info)
    #     self.request_queue.append(request)

    def put_container(self, container: Container):
        container.idle_blocks_cnt += 1
        assert container.idle_blocks_cnt > 0
        if container.idle_blocks_cnt == 1:
            self.idle_containers.append(container)
        self.working_container_number -= 1
        if self.warm_container_number > self.target_container_number:
            self.warm_container_number -= 1
            self.function_manager.worker_idle_size += self.function_manager.memory_map[self.template_info.template_name]

    def dispatch_request(self):
        if self.warm_container_number > self.target_container_number and self.warm_container_number < self.working_container_number:
            delete_number = self.warm_container_number - max(self.target_container_number, self.working_container_number)
            self.warm_container_number -= delete_number
            self.function_manager.worker_idle_size += delete_number * self.function_manager.memory_map[self.template_info.template_name]
        # if self.num_processing >= len(self.request_queue):
        #     return
        if len(self.request_queue) == 0 or self.working_container_number >= self.target_container_number:
            return
        request = self.request_queue.pop(0)
        # print('Allocating a block...')

        if self.warm_container_number > self.working_container_number:
            self.working_container_number += 1
        elif self.function_manager.worker_idle_size >= self.function_manager.memory_map[self.template_info.template_name]:
            self.function_manager.worker_idle_size -= self.function_manager.memory_map[self.template_info.template_name]
            self.warm_container_number += 1
            self.working_container_number += 1
            request.cold_start_time = self.function_manager.cold_start_map[self.template_info.template_name]
        else:
            print("not enough memory for function %s, waiting ..." % self.template_info.template_name)
            self.request_queue.append(request)
            return

        container = self.get_idle_container(request.block_name)

        if container is None:
            assert False, "cannot find container for %s" % self.template_info.template_name
        # self.num_processing -= 1

        request.queuing_time = time.time() - request.arrival_time
        self.run_block(container, request)
        # self.lock.acquire()
        # container.idle_blocks_cnt += 1
        # assert container.idle_blocks_cnt > 0
        # if container.idle_blocks_cnt == 1:
        #     self.idle_containers.append(container)
        # self.lock.release()
        # self.requestIDs_container[request.request_id] = container
        # request_status_code = container.send_request(request)
        #
        # self.put_idle_container(container)

    def regular_clean(self):
        outdated_containers = []
        left_idle_containers = []
        self.lock.acquire()
        now_time = time.time()
        pos = len(self.idle_containers)
        for i, container in enumerate(self.idle_containers):
            if now_time - container.last_time > idle_lifetime:
                assert container.idle_blocks_cnt == self.parallel_limit
                # if len(container.running_blocks) == 0:
                #     outdated_containers.append(container)
                # else:
                #     left_idle_containers.append(container)
            else:
                pos = i
                break
        self.num_exec -= pos
        outdated_containers.extend(self.idle_containers[:pos])
        self.idle_containers = self.idle_containers[pos:]
        self.lock.release()

        for container in outdated_containers:
            self.remove_container(container)

    def remove_container(self, container: Container):
        container.destroy()
        self.port_manager.put(container.port)
