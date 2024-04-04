from concurrent.futures import ThreadPoolExecutor
import time

t = ThreadPoolExecutor(2)
num = 0

def _add():
    global num
    for i in range(0, 1000000):
        num += 1


def _desc():
    global num
    for i in range(0, 1000000):
        num -= 1


future_add = t.submit(_add)
future_desc = t.submit(_desc)

"""
    并没有阻塞等待，所以主线程马上执行完，而上面两个线程不断的切换，上面两个线程不断在一个时间片切换执行，
    在执行到某个地方时主线程已经要输出结果了，此时可能是加法进程在执行，有可能减法进程在执行，就导致结果可能正也可能负
    加上下面这两句代码，等两个线程都执行完必然为0
    future_add.result()
    future_desc.result()
"""
# future_add.result()
# future_desc.result()
print(num)
