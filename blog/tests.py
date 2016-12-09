from django.test import TestCase

# Create your tests here.
#
# def count():
#     fs=[]
#     for i in range(1,4):
#         def f(i):
#             return i*i
#         fs.append(f)
#     return fs
#
# print(count())
#
# f1,f2,f3=count()
# print(f1())
# print(f3())
#
# class from_obj(object):
#     def __init__(self, to_obj):
#         self.to_obj = to_obj
#
# b = [1,2,3]
# a = from_obj(b)
# print(id(a.to_obj))
# print(id(b))
#
#
# from sys import getrefcount
#
# a = [1, 2, 3]
# print(getrefcount(a))
# c=1
#
# b = [[a]*4]
# print(b)
# print globals()
# print(getrefcount(a))
# # class S(object):
# #     def test(self,num):
# # #         return (num % 9 or 9) if num else 0
# from sys import getrefcount
#
# a = [1, 2, 3]
# b = a
# print(getrefcount(a))
#
# del a
# print(getrefcount(b))
#
# from sys import getrefcount
#
# a = [1, 2, 3]
# b = a
# print(getrefcount(b))
#
# a = 1
# print(getrefcount(b))




c=input('test')
c=int(c)


b=0;


if c<100:
	b=c*100


print(b);


import threading


import threading,time

class Timer(threading.Thread):
    def __init__(self,fn,args=(),sleep=0,lastDo=True):
        threading.Thread.__init__(self)
        self.fn = fn
        self.args = args
        self.sleep = sleep
        self.lastDo = lastDo
        self.setDaemon(True)

        self.isPlay = True
        self.fnPlay = False
