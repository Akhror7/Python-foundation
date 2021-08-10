# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 00:37:52 2021

@author: MVP
"""
import random as r
def son_top(uzunlik):
    '''Bu funksiya bir son o\'ylab uni topishingizni so\'raydi'''
    a =  r.randint(1,int(uzunlik))
    print(f"Men 1dan {uzunlik}gacha bir son o\'yladim")
    b = int(input('Bu sonni toping:>>>'))
    try1=1
    while True:
        if a>b:
            print(f"Men o'ylagan son {b} dan katta")
            b = int(input('Bu sonni toping:>>>'))
            try1+=1
        elif a<b:
            print(f"Men o'ylagan son {b} dan kichik")
            b = int(input('Bu sonni toping:>>>'))
            try1+=1
        else:
            print(f"{try1}-urinishda to'g'ri topdingiz\n")
            break
    return try1



def son_topsin(uzunlik):
    '''Kompyuter siz o\'ylagan sonni topadi'''
    print(f"1 dan {uzunlik} gacha bir son o'ylang")
    a =  r.randint(1,int(uzunlik))
    try2 = 1
    while True:
        print(f"Siz o'ylagan son {a} ga tengmi?")
        b = input("Agar {a} son bo'lsa 'ha', agar siz o'ylagan son {a}dan katta bo'lsa '+', agar siz o'ylagan son {a} dan kichik bo'lsa '-' qo'ying ")
        if b =='+':
            a = r.randint(a+1,int(uzunlik))
            try2+=1
        elif b =='-':
            a = r.randint(1,a-1)
            try2+=1
        else:
            print(f"{try2}-urinishda to'g'ri topdingiz")
            break
    return try2
















































