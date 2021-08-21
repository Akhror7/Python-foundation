# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 04:42:56 2021

@author: MVP
"""
try:
    a = float(input('Istalgan sonni kiriting : '))
except:
    print("Siz son kiritmadingiz")
else:
    print(f'{a} ning kvadrati {a**2}')
    print(f'{a} ning kubi {a**3}')
try:
    b = int(input('Yoshingiz nechada? : '))
except:
    print("Siz butun son kiritmadingiz")
else:
    print(f'Siz {2021-b}-yilda tug\'ilgansiz')
try:
    x = float(input('x = '))
    y = float(input('y = '))
except:
    print("Siz x va y qiymatlarga son kiritmadingiz")
else:
    print(f'{x}+{y} = {x+y}')
    print(f'{x}-{y} = {x-y}')
    print(f'{x}*{y} = {x*y}')
    print(f'{x}/{y} = {x/y}')





















