
from bs4 import BeautifulSoup
import requests
import threading
import urllib
import re
import os
import chardet
import sys
import io
import tkinter
from tkinter import *

global headers1
headers1 = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='euckr')



class stockPrice:
    def getNintendoStockPrice(self):
        global t
        x = 'https://textream.yahoo.co.jp/message/1007974/ga4e7f2'
        start_html=requests.get(x,headers=headers1)
        Soup = BeautifulSoup(start_html.text,'lxml')
        NintendoPrice = Soup.find('div', attrs = {'class':'stockPrice cf'})

        return NintendoPrice.text


    def getLGStockPrice(self):
        global u
        x = 'http://finance.naver.com/item/main.nhn?code=034220'
        start_html_2=requests.get(x,headers=headers1)
        Soup_2 = BeautifulSoup(start_html_2.text,'lxml')
        Soup_2.prettify()

        LGPrice = Soup_2.find('dl',attrs={'class':'blind'})

        print('%s: %s'%(y,LGPrice.get_text()))
        print(type(LGPrice))


    def getLGStockPrice1(self):
        global u
        x = 'http://finance.daum.net/item/main.daum?code=034220'
        start_html_2=requests.get(x,headers=headers1)
        Soup_2 = BeautifulSoup(start_html_2.text,'lxml')
        Soup_2.prettify()

        LGPrice = Soup_2.find('span',attrs={'class':'rate'})
        LGLivePrice = Soup_2.select('.list_stockrate')

        '''使用select方法来快速查找'''

        LGLivePrice = LGLivePrice[0].get_text()
        '''使用.get_text()方法来从单一list中取出数据'''
        return LGLivePrice[0:20]


    def getTencentStockPrice(self):
        global u
        headers1 = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        x = 'http://gu.qq.com/hk00700/gp'
        start_html_3 = requests.get(x,headers=headers1)
        Soup_3 = BeautifulSoup(start_html_3.text,'lxml')
        Soup_3.prettify()
        tencentPrice1 = Soup_3.select('.fr')
        tencentRealPrice = Soup_3.select('.data')
        f2 = open('D:\\1.txt','w')
        return '\n'+tencentRealPrice[0].get_text()+'\n'+ tencentPrice1[1].get_text()



    def showPrice(self):
        ui1.label_4.config(text = '%s'%((stockPrice.getNintendoStockPrice('Nintendo','https://textream.yahoo.co.jp/message/1007974/ga4e7f2'))))
        ui1.label_5.config(text = '%s'%(stockPrice.getLGStockPrice1('LG','http://finance.naver.com/item/main.nhn?code=034220')))
        ui1.label_6.config(text = '%s'%(stockPrice.getTencentStockPrice('Tencent','http://gu.qq.com/hk00700/gp')))









