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
  
    for letter in word.upper():
        if letter in user_l.upper():
            print(letter,end='')
        else:
            print('-',end='')
            
def play():
            
    input(f"Assalomu alaykum, SO'Z TOPISH o'yiniga xush kelibsiz!!!\nDavom etish uchun enter tugmasini bosing  ")
    yana = True
    while yana:
        word = get_word()
        print(f"Men {len(word)} harfli so'z o'yladim topishga urinib ko'ring: ")
        set_word=list(set(word))
        letters = ''
        display(letters,word)
        while set_word:
            if letters:
                print(f"\n\nSiz shu paytgacha kiritganlar   :  {letters},",end='')
                user_l = input('Marhamat harf kirgizing:>>>').upper()
            else:
                user_l = input('Marhamat harf kirgizing:>>>').upper()
            letters=letters+user_l
            display(letters,word)
            for letter in set_word:
                if letter in letters:
                    set_word.remove(letter)
           
        print(f"!!!\n\nTabriklayman {word} so'zini {len(letters)} urinishda topdingiz!")
        yana = int(input("Yana o'ynaysizmi? ha(1)/yo'q(0)"))
    print("Sog'-salomat bo'ling")















