#docker build -t registry.cn-beijing.aliyuncs.com/tensorflow-samples/distribute_linear_regression:0.12.0 .

FROM registry.cn-hangzhou.aliyuncs.com/denverdino/tensorflow:0.12.0

RUN mkdir -p /var/worker
ADD . /var/worker
RUN chmod 777 /var/worker/*

CMD ["python", "/var/worker/client.py"]