import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np




def func(x):
    return np.log(1+x**2)-np.sin(x)
def func_diff(x):
    return 2*x/(1+x**2)-np.cos(x)
def func_sec_diff(x):
    return 2*(1-x**2)/(1+x**2)**2+np.sin(x)

def dihotomy_method(func, a, b, accuracy):
    i=0
    while True:
        i+=1
        x1=(b+a-accuracy)/2
        x2=(b+a+accuracy)/2
        y1 = func(x1)
        y2 = func(x2)
        print(f'iter№: {i}|     a: {round(a, 4)}|     b: {round(b, 4)}|     x1: {round(x1, 4)}|       x2: {round(x2, 4)}|       y1: {round(y1, 4)}|       y2: {round(y2, 4)}')
        if y1>y2:
            a = x1
        else:
            b = x2
        if b-a < 2*accuracy:
            xm=(a+b)/2
            ym=func(xm)
            return [xm, float(ym), i]

def gold_method(func, a, b, accuracy):
    x1 = 0.382 * (b - a) + a
    x2 = 0.618 * (b - a) + a
    y1 = func(x1)
    y2 = func(x2)
    i=0
    while True:
        i+=1
        print(f'iter№: {i}|     a: {round(a, 4)}|     b: {round(b, 4)}|     x1: {round(x1, 4)}|       x2: {round(x2, 4)}|       y1: {round(y1, 4)}|       y2: {round(y2, 4)}')
        if y1>=y2:
            a = x1
            x1 = x2
            x2 = a+0.618*(b-a)
            y1=y2
            y2 = func(x2)
        else:
            b=x2
            x2= x1
            x1 = a+0.382*(b-a)
            y2 = y1
            y1 = func(x1)
        if b-a < 2*accuracy:
            xm=(a+b)/2
            ym=func(xm)
            return [xm, float(ym), i]

def hord_method(func_diff, a, b, accuracy):
    i=0
    while True:
        i+=1
        x_per = a - func_diff(a)/(func_diff(a)-func_diff(b))*(a-b)
        fdx = func_diff(x_per)
        print(f'iter№: {i}|     a: {round(a, 4)}|     b: {round(b, 4)}|     x_per: {round(x_per, 4)}|       f`(x_per): {fdx}')
        if abs(fdx)<accuracy:
            return [float(x_per), float(fdx), i]
        if fdx>0:
            b = x_per
        else:
            a = x_per

def Newton_method(func_diff, func_sec_diff, a, b, accuracy):
    i=0
    x_per = (a + b) / 2
    while True:
        i+=1
        fdx = func_diff(x_per)
        print(f'iter№: {i}|     a: {round(a, 4)}|     b: {round(b, 4)}|     x_per: {round(x_per, 4)}|       f`(x_per): {fdx}')
        if abs(func_diff(x_per)) < accuracy:
            return [float(x_per), float(func_diff(x_per)), i]
        x_per = x_per - fdx / func_sec_diff(x_per)

print('Ответ:', dihotomy_method(func, 0, np.pi/4, 0.03))
print('Ответ:', gold_method(func, 0, np.pi/4, 0.03))
print('Ответ:', hord_method(func_diff, 0, np.pi/4, 0.03))
print('Ответ:', Newton_method(func_diff, func_sec_diff,0, np.pi/4, 0.03))

