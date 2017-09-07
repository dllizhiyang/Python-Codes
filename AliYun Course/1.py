
'''随机生成猜数字，判断输入是否为整数'''
'''
import random
result = random.randint(0,10)
print(result)
each = input()
try:
    each = int(each)
    while each != result:
        if each > result:
            print("too large")
            each = int(input())
        if each < result:
            print("too small")
            each = int(input())
    print("yes")
except ValueError:
    print("wrong type")
'''


'''判断字符类型'''
'''each = input()
if type(each) != str:
    print("wrong")
if type(each) == str:
    print ("yes")'''

'''print(isinstance(input(),str))'''


'''一直相加'''
'''
sum = 0
each = input()
while each != "end":
    sum = sum + int(each)
    each = input()
print(sum)
'''

'''GUI编程'''
'''
import tkinter
from tkinter import *

tk = tkinter.Tk()
tk.geometry('500x300')
tk.title("StockPriceSeeker")
priceWindows = Label(text ='hahahahha')

def helloworld():
    priceWindows.config(text = 'xxxxx')


btShow = Button(text='Show',command = lambda :helloworld())

btShow.pack(side='bottom')
priceWindows.pack(side='top',anchor='nw')

tk.mainloop()
'''


'''获取微信信息'''
'''
from wxpy import *
robot = Bot()
robot.chats()

Friends = robot.friends()
print(Friends.stats_text())
print(dir(Friends))

Groups = robot.groups()

print(type(Groups))
print(type(Friends))

for i in Groups:
    print(i)

for y in Friends:
    print('nickname is %s, id is %s, signature is %s' % (y.nick_name, y.remark_name, y.signature))
'''


'''设置定时'''
'''
import threading

def sayhello(x):
    global t
    print(x)
    t = threading.Timer(5.0,sayhello,[x])
    t.start()
t = threading.Timer(5.0,sayhello,['hahahahah'])
t.start()

'''

'''获取股票价格，Beautiful Soup的使用, 读写文件操作'''
'''see GUI-StockPrice.py'''


'''1.Given an array of integers, every element appears twice except
for one. Find that single one.'''
'''
list1=[1,1,3,3,6,8,4,6,8]
class solution:
    def findthesingle(self,A):
        for i in A:
            if A.count(i) == 1:
                print(i)
quiz = solution()
quiz.findthesingle(list1)
'''



#1.1 remove deplicates from sorted array
# A sorted array will be given, delete the deplicated elements and return the length of new array
'''
A = [1,2,3,4,5,6,6,7,7,7,8,9]
B = []

class solution:
    def removeDuplicates(self,num):
        if len(num) == 0:
            return 0
        for i in num:
            if num.count(i) > 1:
                num.remove(i)
        return len(num)
quiz = solution()
print(quiz.removeDuplicates(A))
print(A)
'''
###或者把所有重复元素找出放入一个新的数组
'''class solution:
    def removeDuplicates(self,num):
        if len(num) == 0:
            return 0
        for i in num:
            if num.count(i) == 1:
                B.append(i)  
quiz = solution()
print(quiz.removeDuplicates(A))
print(B)
'''

###或者使用set函数
''''
A = list(set(A))
print(A)
'''


#1.2 remove deplicates from sorted array
# A sorted array will be given, keep at least two deplicated elements and return the length of new array
'''
A = [1,2,3,4,5,6,6,7,7,7,8,9]
B = []
class solution:
    def removeDuplicates(self,num):
        if len(num) == 0:
            return 0
        for i in num:
            if num.count(i) > 2:
                num.remove(i)
        return len(num)
quiz = solution()
print(quiz.removeDuplicates(A))
print(A)'''


#1.3 Search in Rotated Sorted Array
#search the target in the given array, return the its index, if not in there, return -1
'''
A = [4,5,0,8,1,4,2,9,3]
B = 4
class solution:
    def findthetarget(self,nums,target):
        if nums.count(target) == 0:
            return -1
        if nums.count(target) >= 1:
            return nums.index(target)
quiz = solution()
print(quiz.findthetarget(A,B))
'''

#1.4, find the target in the list, and report all index(may be more than 1)
'''
A = [4,5,0,8,1,4,2,9,5,4,3]
B = 4
C = []
class solution:
    def findthetarget(self,nums,target):
        if nums.count(target) == 0:
            return -1
        if nums.count(target) == 1:
            return nums.index(target)
        if nums.count(target) > 1:
            for i in range(len(nums)):
                if nums[i] == target:
                    C.append(i)  #############.index()只会报出第一次出现的位置
quiz = solution()
print(quiz.findthetarget(A,B))
print(C)
'''''''''
