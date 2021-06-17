"""
也可以写其他接受数据的方式掉用Center类中的方法
"""

import socket
import time
import threading
import json

from center import TaskCenter


def create_task(msg_data):
    # 注册task对象
    task = TaskCenter()
    task.reg_task(msg_data["id"], msg_data["user_name"], msg_data["command"], msg_data["permission"])
    # 执行任务
    task.run_task()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'connect!')

    data = sock.recv(1024)
    msg_data = json.loads(data.decode('utf-8'))
    time.sleep(1)
    sock.send(("get msg").encode('utf-8'))
    # 调用上面的函数执行json中的任务
    create_task(msg_data)

    sock.close()
    print('Connection from %s:%s closed.' % addr)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 9999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
    # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
