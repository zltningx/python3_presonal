#!/usr/bin/env python
# coding=utf-8

import requests
import sys
import argparse
from queue import Queue
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QWidget

class Proxy():
    def __init__(self,url):
#        super().__init__()
#        self.initUI()
        self._url = url
        self._positionurl = ''
        self._newslist = list()

    def getnews(self):
        try:
            news = requests.get(self._url)
        except Exception as e:
            print (e)
        soup = BeautifulSoup(news.content)
        list = soup.find_all('a')
        for i in list:
            nlist = []
            try:
                if i['href'].startswith("http://news.sina.com.cn/"):
                    nlist.append(i.string)
                    nlist.append(i['href'])
                    self._newslist.append(nlist)
            except Exception as e:
                print(e)

    def shownews(self):
        i = 1
        for h in self._newslist:
            if h[0] is not None:
                print('{}. {}'.format(i,h[0]))
                i += 1
        num = input('你想要浏览的新闻:')
        num = int(num)-1
        self._positionurl = self._newslist[num]

    def readnews(self):
        try:
            res = requests.get(self._positionurl[1],timeout=4)
            soup = BeautifulSoup(res.content)
            reader = soup.find_all('p')
        except Exception as e:
            print(e)
        print('\n\t标题： {}'.format(self._positionurl[0]))
        print('\n\n')
        for i in reader:
            if i.string is not None:
                print(i.string)

if __name__ == '__main__':
    ex = Proxy('http://news.sina.com.cn/')
    ex.getnews()
    ex.shownews()
    ex.readnews()
