#!/usr/bin/python
# -*- coding: UTF-8 -*-
# �ļ�����client.py

import socket               # ���� socket ģ��
import webbrowser
s = socket.socket()         # ���� socket ����
host = socket.gethostname() # ��ȡ����������
port = 12345                # ���ö˿ں�

s.connect((host, port))
print s.recv(1024)
s.close()  