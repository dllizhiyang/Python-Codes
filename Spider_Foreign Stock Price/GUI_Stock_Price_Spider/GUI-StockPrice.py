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

class stockprice:

    def getNintendoStockPrice(self,y,x):
        global t
        x = 'https://textream.yahoo.co.jp/message/1007974/ga4e7f2'
        start_html=requests.get(x,headers=headers1)
        Soup = BeautifulSoup(start_html.text,'lxml')
        #livePrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
        NintendoPrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
        #print(livePrice)
        return NintendoPrice.text




    def getLGStockPrice(self,y,x):
        global u
        x = 'http://finance.naver.com/item/main.nhn?code=034220'
        start_html_2=requests.get(x,headers=headers1)
        Soup_2 = BeautifulSoup(start_html_2.text,'lxml')
        Soup_2.prettify()
        #livePrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
        LGPrice = Soup_2.find('dl',attrs={'class':'blind'})
        #LGPrice = Soup_2.find(text='??? ')
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

    def getLGStockPrice1(self,y,x):
        global u
        x = 'http://finance.daum.net/item/main.daum?code=034220'
        start_html_2=requests.get(x,headers=headers1)
        Soup_2 = BeautifulSoup(start_html_2.text,'lxml')
        Soup_2.prettify()
        #livePrice = Soup.find('div', attrs = {'class':'stockPrice cf'})
        LGPrice = Soup_2.find('span',attrs={'class':'rate'})
        LGLivePrice = Soup_2.select('.list_stockrate')

        '''使用select方法来快速查找'''
        #LGPrice = Soup_2.find(text='??? ')
        #f2 = open('D:\\1.txt','w')
        #LGPrice = str(LGPrice)
        #f2.write(LGPrice)
        #f2.close()

        #print(livePrice)
        #print('%s: %s'%(y,LGPrice.get_text()))
        #print('%s:\n %s'%(y,LGPrice.get_text()))
        LGLivePrice = LGLivePrice[0].get_text()
        '''使用.get_text()方法来从单一list中取出数据'''
        return LGLivePrice[0:18]
        #print('Find method result is %s'%((type(LGPrice))))
        #print('Select method result is %s'%(type(LGLivePrice)))

        #f=open('D:\\2.txt','w+')
        #print('%s:\n %s'%(y,LGLivePrice[0].get_text()), file=f)


        #t = threading.Timer(1, getLGStockPrice,[y,x])
        #t.start()

    def getTencentStockPrice(self,y,x):
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
        #LGPrice = Soup_2.find(text='??? ')
        f2 = open('D:\\1.txt','w')
        #tencentPrice1 = str(tencentPrice1)
        #tencentRealPrice = str(tencentRealPrice)
        #f2.write(tencentPrice1)
        #f2.close()
        #print(livePrice)
        #print('%s: %s'%(y,LGPrice.get_text()))
        #print('%s: %s'%(y,tencentPrice))
        return '\n'+tencentRealPrice[0].get_text()+'\n'+ tencentPrice1[1].get_text()


    #f2 = open('D:\\1.txt','w')

#t = threading.Timer(5, getNintendoStockPrice,['Nintendo','https://textream.yahoo.co.jp/message/1007974/ga4e7f2'])
#t = threading.Timer(1, getLGStockPrice,['LG','http://finance.naver.com/item/main.nhn?code=034220'])
#getLGStockPrice('LG','http://finance.naver.com/item/main.nhn?code=034220')

############################################################################################################
tk = tkinter.Tk()
tk.geometry('600x100')
tk.title("StockPrice")
global tryWidth
tryWidth = '20'
priceWindows1 = Label(width = tryWidth,text ='Nintendo',font='20')
priceWindows2 = Label(width = tryWidth,text = 'LGDisplay',font='20')
priceWindows3 = Label(width = tryWidth,text = 'Tencent',font='20')
btShow = Button(text='涨涨涨！',font = '20',command = lambda :showPrice(),height='5', width='10')
############################################################################################################

getstockprice = stockprice()

def showPrice():
    priceWindows1.config(width = tryWidth,text = 'Nintendo:%s'%((getstockprice.getNintendoStockPrice('Nintendo','https://textream.yahoo.co.jp/message/1007974/ga4e7f2'))),font='20')
    priceWindows2.config(width = tryWidth,text = 'LG:%s'%(getstockprice.getLGStockPrice1('LG','http://finance.naver.com/item/main.nhn?code=034220')),font='20')
    priceWindows3.config(width = tryWidth,text ='Tencent: %s'%(getstockprice.getTencentStockPrice('Tencent','http://gu.qq.com/hk00700/gp')),font='20')





'''
btShow.pack(side='bottom')
priceWindows1.pack(side = 'left', anchor = 'nw')
priceWindows2.pack(side = 'top', anchor = 'n')
priceWindows3.pack(side = 'right',anchor = 'ne')
'''

btShow.grid(column = 1, row=0)
priceWindows1.grid(column = 2, row=0, sticky = 'w')
priceWindows2.grid(column = 3, row=0, sticky = 'n')
priceWindows3.grid(column = 4, row=0, sticky = 'e')


#btShow.grid(row = 1, column = 10)



tk.mainloop()


'''
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
'''
