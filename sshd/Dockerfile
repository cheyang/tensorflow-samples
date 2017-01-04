# docker build -t registry.cn-beijing.aliyuncs.com/tensorflow-samples/tensorflow-sshd:0.12.0-devel .

FROM registry.cn-hangzhou.aliyuncs.com/denverdino/tensorflow:0.12.0-devel

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends openssh-server && \
    apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /var/run/sshd && \
    sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

ADD startup.sh /usr/sbin/startup.sh

RUN chmod 777 /usr/sbin/startup.sh 

RUN echo export PATH=${PATH} >> /etc/profile && \
    echo export LD_LIBRARY_PATH=${LD_LIBRARY_PATH} >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/startup.sh"]