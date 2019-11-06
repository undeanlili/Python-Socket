#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import socket
import datetime
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
server.bind((host,9090)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    while True:
        data = conn.recv(1024)  #接收数据
        print(data.decode()) #打印接收到的数据
        serverTimeReceive = datetime.datetime.now().microsecond
        print(serverTimeReceive)#打印服务器接收到数据时间点
        
        msg = '客户端接收到数据的时间！' 
        conn.send(msg.encode('utf-8')) #然后再发送数据        
        serverTimeSend = datetime.datetime.now().microsecond
        print("服务器发送数据的时间点\n",serverTimeSend)#打印服务器发送数据时间点
        time.sleep(5)
    conn.close()
