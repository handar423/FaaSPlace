from gevent import monkey

monkey.patch_all()
import time

from gevent import event
import sys

sys.path.append('../../')
import json
import gevent
import requests
from typing import Dict

from config import config
from repository import Repository
from flask import Flask, request
from gevent.pywsgi import WSGIServer
from workflow_info import WorkflowInfo
from kafka import KafkaAdminClient

app = Flask(__name__)
repo = Repository()
workflows_info = WorkflowInfo.parse(config.WORKFLOWS_INFO_PATH)
worker_addrs = config.WORKER_ADDRS


class RequestInfo:
    def __init__(self, request_id):
        self.request_id = request_id
        self.result = event.AsyncResult()


requests_info: Dict[str, RequestInfo] = {}
workersp_url = 'http://{}:8000/{}'


@app.route('/run', methods=['POST'])
def run():
    inp = request.get_json(force=True, silent=True)
    workflow_name = inp['workflow_name']
    request_id = inp['request_id']
    input_datas = inp['input_datas']
    function_routing = inp['function_routing']
    repo.create_request_doc(request_id)
    requests_info[request_id] = RequestInfo(request_id)
    workflow_info = workflows_info[workflow_name]
    worker_num = len(worker_addrs)
    templates_info = {}
    for i, template_name in enumerate(workflow_info.templates_infos):
        ip = worker_addrs[i % worker_num]
        if workflow_name == 'video':
            ip = worker_addrs[video_sp_ip_idx[worker_num][template_name]]
            if template_name == 'video__transcode' and worker_num == 3:
                flag = int(request_id[-1]) % 2
                if flag == 0:
                    idx = 0
                else:
                    idx = 2
                ip = worker_addrs[idx]

        ip = worker_addrs[function_routing[template_name]]
        # print(template_name, ip)
        templates_info[template_name] = {'ip': ip}

    # templates_info = {template_name: {'ip': '127.0.0.1'} for template_name in workflow_info.templates_infos}
    # split video workflow to different nodes!
    # print(templates_info)
    data = {'request_id': request_id,
            'workflow_name': workflow_name,
            'templates_info': templates_info}
    ips = set()
    for template_info in templates_info.values():
        ips.add(template_info['ip'])
    st = time.time()
    # 1. transmit request_info to all relative nodes
    events = []
    for ip in ips:
        remote_url = workersp_url.format(ip, 'request_info')
        events.append(gevent.spawn(requests.post, remote_url, json=data))
    gevent.joinall(events)
    # 2. transmit input_datas of this request to relative nodes
    # 2.1 gather input_datas of each IP
    ips_datas_mapping: Dict[str, dict] = {}
    for input_data_name in input_datas:
        for dest_template_name in workflow_info.data['global_inputs'][input_data_name]['dest']:
            ip = templates_info[dest_template_name]['ip']
            if ip not in ips_datas_mapping:
                ips_datas_mapping[ip] = {}
            if input_data_name not in ips_datas_mapping[ip]:
                ips_datas_mapping[ip][input_data_name] = input_datas[input_data_name]
    # 2.2 transmit input_datas
    # Todo. Assume user's input_datas are small.
    events = []
    for ip in ips_datas_mapping:
        remote_url = workersp_url.format(ip, 'transfer_data')
        data = {'request_id': request_id,
                'workflow_name': workflow_name,
                'template_name': 'global_inputs',
                'block_name': 'global_inputs',
                'datas': ips_datas_mapping[ip]}
        events.append(gevent.spawn(requests.post, remote_url, json=data))
    gevent.joinall(events)
    result = requests_info[request_id].result.get()
    ed = time.time()
    return json.dumps({'result': result, 'latency': ed - st})

@app.route('/sent_scaling', methods=['POST'])
def sent_scaling():
    inp = request.get_json(force=True, silent=True)
    scaling_info = inp['scaling_info']
    for ip in worker_addrs:
        remote_url = workersp_url.format(ip, 'sent_scaling_data')
        data = {'scaling_info': scaling_info}
        r = requests.post(remote_url, json=request_info)
        assert r.status_code == 200
    return 'OK', 200

@app.route('/post_user_data', methods=['POST'])
def post_user_data():
    inp = request.get_json(force=True, silent=True)
    request_id = inp['request_id']
    datas = inp['datas']
    # print(datas)
    requests_info[request_id].result.set(datas)
    return 'OK', 200


@app.route('/clear', methods=['POST'])
def clear():
    client.delete_topics(client.list_topics())
    requests_info.clear()
    return 'OK', 200


if __name__ == '__main__':
    client = KafkaAdminClient(bootstrap_servers=config.KAFKA_URL, api_version=(2,0,2))
    client.delete_topics(client.list_topics())
    server = WSGIServer((sys.argv[1], int(sys.argv[2])), app)
    server.serve_forever()
