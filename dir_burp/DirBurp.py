#!/usr/bin/env python
# coding=utf-8

from concurrent.futures import ThreadPoolExecutor
import requests
import os

def GetRespon(url):
    try:
        respon = requests.get(url,headers=header)
        if respon.status_code == 200 | respon.status_code == '200':
            print("[*]{:s}----->{:s}".format(url,respon.status_code))
            try:
                with open(os.path.abspath('.')+'/urldata.txt') as f:
                    f.write(url+'\r\n')
            except IOError as e:
                print(e)
                pass
        else:
            print("NoFound-->",respon.status_code)
    except Exception as e:
        print(e)
        pass


def BurpURLAdmin(file):
    with ThreadPoolExecutor(50) as Executor:
        with open(os.path.abspath('.')+'/'+str(file),'r') as f:
            for line in f:
                dic = line.strip('\n')
                url = target+dic
                try:
                    Executor.submit(GetRespon,url)
                    GetRespon(url)
                except Exception as e:
                    print(e)
                    pass


def Choise(choise):
    if choise == '1':
        for file in dirctory:
            if file.startswith('JSP') | file.startswith('ASPX') | file.startswith('PHP'):
                continue
            BurpURLAdmin(file)
    if choise == '2':
        for file in dirctory:
            if file.startswith('JSP') | file.startswith('ASP') | file.startswith('PHP'):
                continue
            BurpURLAdmin(file)
    if Choise == '3':
        for file in dirctory:
            if file.startswith('PHP') | file.startswith('ASP') | file.startswith('ASPX'):
                continue
            BurpURLAdmin(file)
    if Choise == '4':
        for file in dirctory:
            if file.startswith('ASP') | file.startswith('ASPX') | file.startswith('JSP'):
                continue
            BurpURLAdmin(file)
    if Choise == '5':
        for file in dirctory:
            BurpURLAdmin(file)
    

if __name__ == '__main__':
    global dirctory
    for r,d,f in os.walk('.'):
        dirctory = [name for name in f if name.endswith('.txt')]

    print(dirctory)
    print("[Note:]------------------>>欢迎使用<<---------------------")
    print("[Note:]            Autor:   NS   LiT0  ")
    global target
    target = input("[Note:] --->输入网址URL： ") 
    choise = input("[Note:] --->请选择网址类型： 1.ASP   2. ASPX  3.JSP  4. PHP 5.ALL")
    print("[Note:] --->Running!")

    global header
    header = {
        'Cache-Control':'max-age=0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8'
    }
    BurpURLAdmin('ASP.txt')
