###################面向对象编程，类的定义，类的实例化，#####################
class myfriend:
    friendnum = 0
    def print_the_name(self,name): ##############子函数必须第一个引入self变量作为自参
        print(name)
        myfriend.friendnum += 1    ###############引用类中参数的方式

    def print_number(self):
        print(myfriend.friendnum)

aaa = myfriend()                   ###############类的实例化
aaa.print_the_name('lala')
aaa.print_the_name('cc')
aaa.print_number()







'''2.Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.'''



