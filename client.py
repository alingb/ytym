#!/usr/bin/env python
# _*_enconding:utf-8_*_
# TIME:2018/6/1 14:22
# FILE:client.py


import socket

HOST = '192.168.1.57'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    cmd = raw_input("[root@master mnt]#")
    s.sendall(cmd)
    data = s.recv(10240)
    print data
s.close()
