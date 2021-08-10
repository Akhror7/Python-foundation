# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 00:37:48 2021

@author: MVP
"""

import functions as f
s = input('Assalomu alaykum! son topish o\'yini o\'ynaymizmi? \(ha/yo\'q\)>>>')
while True:

    if s=='ha':
        print('Unda boshladik')
        uzunlik = int(input('Qaysi songacha o\'ylash mumkin>>>')) 
        a = f.son_top(uzunlik)
        b = f.son_topsin(uzunlik)     
        if a>b:
            s=input("Yutqazdingiz , yana o'ynaymizmi?\(ha/yo'q\)>>>")
        elif a<b:
            s=input("Yutdingiz , yana o'ynaymizmi?\(ha/yo'q\)>>>")
        else:
            s=input("Durang , yana o'ynaymizmi?\(ha/yo'q\)>>>")
    else:
        print('Xayr')
        break









