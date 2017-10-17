from bs4 import BeautifulSoup
import requests
import threading
import urllib
import re
import os
import chardet
import sys
import io

global headers1
headers1 = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='euckr')

def getNintendoStockPrice(y,x):
    global t
    x = 'https://textream.yahoo.co.jp/message/1007974/ga4e7f2'
    start_html=requests.get(x,headers=headers1)
    Soup = BeautifulSoup(start_html.text,'lxml')
    #livePrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
    NintendoPrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
    #print(livePrice)
    print('%s: %s'%(y,NintendoPrice.text))
    f=open('D:\\2.txt','a')
    print('%s: %s'%(y,NintendoPrice.text), file=f)



def getLGStockPrice(y,x):
    global u
    x = 'http://finance.naver.com/item/main.nhn?code=034220'
    start_html_2=requests.get(x,headers=headers1)
    Soup_2 = BeautifulSoup(start_html_2.text,'lxml')
    Soup_2.prettify()
    #livePrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
    LGPrice = Soup_2.find('dl',attrs={'class':'blind'})
    #LGPrice = Soup_2.find(text='현재가 ')
    #f2 = open('D:\\1.txt','w')
    #LGPrice = str(LGPrice)
    #f2.write(LGPrice)
    #f2.close()

    #print(livePrice)
    #print('%s: %s'%(y,LGPrice.get_text()))
    print('%s: %s'%(y,LGPrice.get_text()))
    print(type(LGPrice))

    #f2 = open('D:\\1.txt','w')
    #LGPrice = str(LGPrice.encode('euckr'))
    #f2 = f2.write(LGPrice)


    #t = threading.Timer(1, getLGStockPrice,[y,x])
    #t.start()

def getLGStockPrice1(y,x):
    global u
    x = 'http://finance.daum.net/item/main.daum?code=034220'
    start_html_2=requests.get(x,headers=headers1)
    Soup_2 = BeautifulSoup(start_html_2.text,'lxml')
    Soup_2.prettify()
    #livePrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
    LGPrice = Soup_2.find('span',attrs={'class':'rate'})
    LGLivePrice = Soup_2.select('.list_stockrate')

    '''使用select方法来快速查找'''
    #LGPrice = Soup_2.find(text='현재가 ')
    #f2 = open('D:\\1.txt','w')
    #LGPrice = str(LGPrice)
    #f2.write(LGPrice)
    #f2.close()

    #print(livePrice)
    #print('%s: %s'%(y,LGPrice.get_text()))
    #print('%s:\n %s'%(y,LGPrice.get_text()))
    LGLivePrice = LGLivePrice[0].get_text()
    '''使用.get_text()方法来从单一list中取出数据'''
    print('%s: %s'%(y,LGLivePrice[0:18]))
    #print('Find method result is %s'%((type(LGPrice))))
    #print('Select method result is %s'%(type(LGLivePrice)))

    #f=open('D:\\2.txt','w+')
    #print('%s:\n %s'%(y,LGLivePrice[0].get_text()), file=f)


    #t = threading.Timer(1, getLGStockPrice,[y,x])
    #t.start()

def getTencentStockPrice(y,x):
    global u
    headers1 = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    x = 'http://gu.qq.com/hk00700/gp'
    start_html_3 = requests.get(x,headers=headers1)
    Soup_3 = BeautifulSoup(start_html_3.text,'lxml')
    Soup_3.prettify()
    #livePrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
    #tencentPrice = Soup_3.find_all('span',attrs={'class':'fr'})
    tencentPrice1 = Soup_3.select('.fr')
    tencentRealPrice = Soup_3.select('.data')
    #LGPrice = Soup_2.find(text='현재가 ')
    f2 = open('D:\\1.txt','w')
    #tencentPrice1 = str(tencentPrice1)
    #tencentRealPrice = str(tencentRealPrice)
    #f2.write(tencentPrice1)
    #f2.close()
    #print(livePrice)
    #print('%s: %s'%(y,LGPrice.get_text()))
    #print('%s: %s'%(y,tencentPrice))
    print('%s:\n %s, %s'%(y,tencentRealPrice[0].get_text(),tencentPrice1[1].get_text()))
    f=open('D:\\2.txt','a')
    print('%s:\n %s, %s'%(y,tencentRealPrice[0].get_text(),tencentPrice1[1].get_text()), file=f)

    #f2 = open('D:\\1.txt','w')

#t = threading.Timer(5, getNintendoStockPrice,['Nintendo','https://textream.yahoo.co.jp/message/1007974/ga4e7f2'])
#t = threading.Timer(1, getLGStockPrice,['LG','http://finance.naver.com/item/main.nhn?code=034220'])
#getLGStockPrice('LG','http://finance.naver.com/item/main.nhn?code=034220')

while True:
    input()
    print('*'*50)
    getLGStockPrice1('LG','http://finance.naver.com/item/main.nhn?code=034220')
    print('*'*30)
    getNintendoStockPrice('Nintendo','https://textream.yahoo.co.jp/message/1007974/ga4e7f2')
    print('*'*30)
    getTencentStockPrice('Tencent','http://gu.qq.com/hk00700/gp')
    #f1 = open('D:\\1.txt','r')
    #f1.encoding('utf-8')
    #print(f1.read())
    #f1.close()
#t.start()
