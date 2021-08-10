# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 07:17:23 2021

@author: MVP
"""
import random as r
from uzwords import words
def get_word():
    """So'z tanlaydigan funksiya"""
    word = r.choice(words)
    while '-' in word or ' ' in word:
        word = r.choice(words)
    return word.upper()


def display(user_l,word):
    """Harfni so'zda bor yo'qligini tekshiradi"""
    display_letter=''
    for letter in word.upper():
        if letter in user_l.upper():
            display_letter+=letter
        else:
            display_letter+='-'
    return display_letter
def play():
            
    input(f"Assalomu alaykum, SO'Z TOPISH o'yiniga xush kelibsiz!!!\nDavom etish uchun enter tugmasini bosing  ")
    yana = True
    while yana:
        word = get_word()
        print(f"Men {len(word)} harfli so'z o'yladim topishga urinib ko'ring: ")
        display_letter=display('',word)
        print(display_letter)
        letters=''
        d_letter=''
        while '-' in display_letter:
            if letters:
                print(f"Siz shu paytgacha kiritgan harflar:  {d_letter}")
            user_l=input(f"Marhamat harf kiriting:>>>").upper()
            if user_l in letters:
                print(f"Bu harf kiritilgan, iltimos, boshqa harf kiriting! ")
                continue
            elif user_l in word:
                print(f"Ajoyib , shu tarzda davom eting: ")
                d_letter+=user_l
            else:
                print(f"Afsus, bu harf so'zimizda mavjud emas , yana  urinib ko'ring:")
                d_letter+=user_l
            letters+=user_l
            display_letter=display(letters,word)
            print(display_letter)
            
        print(f"!!!\n\nTabriklayman {word} so'zini {len(letters)} urinishda topdingiz!")
        yana = int(input("Yana o'ynaysizmi? ha(1)/yo'q(0)"))
    print("Sog'-salomat bo'ling")














