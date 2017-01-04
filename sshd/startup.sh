#!/bin/bash

SSHDIR=/home/mpirun/.ssh/

if [ -n "$SSH_PORT" ]; then
      sed -ri "s/Port 22/Port ${SSH_PORT}/g" /etc/ssh/sshd_config
      echo "Port ${SSH_PORT}" >> ${SSHDIR}/config
fi

if [[ -z "${SSH_PASSWORD}" ]]; then
    SSH_PASSWORD="tryHPC"
fi

echo "Password Of User root is $SSH_PASSWORD"

echo "root:$SSH_PASSWORD" | chpasswd

/usr/sbin/sshd -D
