#git pull
docker build --no-cache -t  codeless_base /mydata/FaaSPlace/src/container
bash /mydata/FaaSPlace/benchmark/svd/create_image.sh
bash /mydata/FaaSPlace/benchmark/video/create_image.sh
bash /mydata/FaaSPlace/benchmark/wordcount/create_image.sh
bash /mydata/FaaSPlace/benchmark/recognizer/create_image.sh
docker image prune -f