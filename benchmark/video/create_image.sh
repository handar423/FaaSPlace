docker build --no-cache -t workflow_video_base /mydata/FaaSPlace/benchmark/template_functions/video__base
docker build --no-cache -t video__upload /mydata/FaaSPlace/benchmark/template_functions/video__upload
docker build --no-cache -t video__split /mydata/FaaSPlace/benchmark/template_functions/video__split
docker build --no-cache -t video__group0 /mydata/FaaSPlace/benchmark/template_functions/video__group0
docker build --no-cache -t video__transcode /mydata/FaaSPlace/benchmark/template_functions/video__transcode
docker build --no-cache -t video__merge /mydata/FaaSPlace/benchmark/template_functions/video__merge
docker build --no-cache -t video__simple_process /mydata/FaaSPlace/benchmark/template_functions/video__simple_process

