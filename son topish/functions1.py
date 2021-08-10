
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 02:48:08 2021

@author: MVP
"""
import random as r

def sontop(x=10):
    """Kompyuter bir son o'ylab ,uni topishingizni so'raydi"""
    a = r.randint(1,x)
    count = 0
    print(f"Birdan {x} gacha  bir son o'yladim. U nechaga teng? ")
    while True:
        b = int(input('>>>'))
        count = count+1
        if b>a:
            print(f"Men o'ylagan son {b} kichikroq.Qaytadan urininb ko'ring:")
      
        elif a>b:
            print(f"Men o'ylagan son {b} kattaroq.Qaytadan urininb ko'ring:")
            
        else:
            print(f"{count}-urinishda to'g'ri topdingiz")
            break
    return count

def sontopsin(x=10):
    """Siz o'ylagan sonni kompyuter topishga harakat qiladi"""
    count = 0
    input(f"Birdan {x} gacha bir son o'ylang. Men uni topishga harakat qilib ko'raman")
    q = 1
    y = x
    while True:
        count+=1
        a = r.randint(q,y)
        print(f'Siz o\'ylaga son {a} mi?')
        b = input("(Ha),kattaroq (+), kichikroq(-)>>>").lower()
        if b=='+':
            q = a+1
        elif b=='-':
            y= a-1
        else:
            print(f"{count}- urinishda topdim")
            break
    return count














