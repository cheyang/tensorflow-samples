import tensorflow as tf
import os
import logging
import sys


root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

# TensorFlow集群描述信息，ps_hosts表示参数服务节点信息，worker_hosts表示worker节点信息

tf.app.flags.DEFINE_string("ps_hosts", "", "Comma-separated list of hostname:port pairs")

tf.app.flags.DEFINE_string("worker_hosts", "", "Comma-separated list of hostname:port pairs")

# TensorFlow Server模型描述信息，包括作业名称，任务编号，隐含层神经元数量，MNIST数据目录以及每次训练数据大小（默认一个批次为100个图片）

tf.app.flags.DEFINE_string("job_name", "", "One of 'ps', 'worker'")

tf.app.flags.DEFINE_integer("task_index", 0, "Index of task within the job")


