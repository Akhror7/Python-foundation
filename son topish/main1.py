# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 02:48:06 2021

@author: MVP
"""

import functions1 as f
yana = True
while yana:
    x = int(input('Qaysi songacha o\'ylaymiz>>>'))
    a = f.sontop(x)
    b = f.sontopsin(x)
    if a>b:
        print(f"{a}:{b} hisobda yutqazdingiz")
    elif a<b:
        print(f"{a}:{b} hisobda yutdingiz")
    else:
        print(f"{a}:{b} hisobda durang")
    yana = int(input('Yana o\'ynaysizmi? (1) or (0)>>>'))
print('salomat bushat')
































