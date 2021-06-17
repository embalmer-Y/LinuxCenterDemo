import socket
import json


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
msg_dict = {}

#构建json对象
command = []
msg_dict["id"] = input("id=")
msg_dict["user_name"] = input('user_name=')
command.append(input('command='))
msg_dict["command"] = command
msg_dict["permission"] = input("permission=")
# msg_dict["id"] = "1"
# msg_dict["user_name"] = "Emb"
# msg_dict["command"] = ["HelloWorld"]
# msg_dict["permission"] = "root"
msg_json = json.dumps(msg_dict)
# 发送json数据
s.send(bytes(msg_json.encode('utf-8')))

print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
