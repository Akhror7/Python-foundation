# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 21:40:21 2021

@author: MVP
"""

import random
print('Keling son topish o\'yini o\'ynaymiz!')
while True:
    a=random.randint(1,10)
    b = int(input('Men birdan o\'ngacha bir son o\'yladim ,uni topishga urinib ko\'ring:   '))
    u=1
    while True:
        if a<b:
            b=int(input(f"Men o'ylagan son {b} dan kichik, qaytadan urinib ko'ring>>>"))
            u=u+1
        if a>b:
            b=int(input(f"Men o'ylagan son {b} dan katta, qaytadan urinib ko'ring>>>"))
            u=u+1     
        else:
            break
    print(f"To'g'ri siz sonni {u} urinishda topdingiz!")
    s=1
    print(f"Endi siz son o'ylang men uni topaman")


    a=random.randint(1,10)
    while True:
        w=input(f"Siz o'ylagan son {a}, agar to'gri bo'lsa 't',siz o'ylagan son {a}dan kichik bo'lsa 0 , agar siz o'ylagan son {a} dan katta bo'lsa 1 qo'ying:   ")
        if w== '1':
            a = random.randint(a+1,10)
            w=input(f"Siz o'ylagan son {a}, agar to'gri bo'lsa 't',siz o'ylagan son {a}dan kichik bo'lsa '-' , agar siz o'ylagan son {a} dan katta bo'lsa '+' qo'ying:   ")
            s=s+1
        if w== '0':
            a = random.randint(1,a-1)
            w=input(f"Siz o'ylagan son {a}, agar to'gri bo'lsa 't',siz o'ylagan son {a}dan kichik bo'lsa '-' , agar siz o'ylagan son {a} dan katta bo'lsa '+' qo'ying:   ")
            s=s+1   
        if w=='t' or w=='T':
            print(f"Men sonni {s} urinishda topdim")
            break
    if u>s:
        print('Men yutdim')
    elif u<s:
        print('Siz yutdingiz')
    else:
        print(f"durang")
    o=input('Yana o\'ynaymizmi?\(ha/yo\'q\)   ')
    if o=='yo\'q':
        break



































