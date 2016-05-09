# docker build -t registry.cn-beijing.aliyuncs.com/tensorflow-samples/tf_grpc_server:0.12.0 .

FROM registry.cn-hangzhou.aliyuncs.com/denverdino/tensorflow:0.12.0
RUN mkdir -p /var/worker
ADD . /var/worker
RUN chmod 777 /var/worker/*

ENTRYPOINT ["/var/worker/grpc_tensorflow_server.py"]