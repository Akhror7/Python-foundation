# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:20:35 2021

@author: MVP
"""

# s = int(input('Iltimos, juft son kiriting>>>'))
# if s%2==0:
#     print('Rahmat!')
# else:
#     print('Bu juft son emas!')

# y = int(input('Yoshingiz?>>>'))
# if y>60 or y<4:
#     narh=0
# elif y<18:
#     narh=10000
# else:
#     narh=20000
# print(f'Siz uchun chipta {narh} so\'m')

# a = float(input('1-son>>>'))
# b = float(input('2-son>>>'))
# if a>b:
#     print(f'{a}>{b}')
# else:
#      print(f'{a}<{b}')

# mahsulotlar = ['un','suv','moy','non','choy','olma','asal','shakar','tuz','tuxum']
# savat =[]
# bor = []
# y = []
# for i in range(5):
#     savat.append(input(f'{i+1} - mahsulotni qo\'shing: '))
# for s in savat:
#     if s.lower() in  mahsulotlar:
#         bor.append(s)
#     else:
#         y.append(s)
# if y:
#     print('Quyidagi mahsulotlar do\'konimizda yo\'q: ' )
#     for i in y:
#         print(i)
# else:
#     print('siz so\'ragan barcha mahsulotlar do\'konimizda bor!')

# f = ['anvar','ahror','suhrob','umid','bobur']
# l = input('Loginni tanlang: ')
# if l.lower() in f:
#     print('Bu login band iltimos boshqa tanlang!')
# else:   
#     print(f'Xush kelibsiz ,{l}!')

s = int(input('butun son kiriting: '))
for i in range(2,11):
    if s%i==0:
        print(f'{s} soni {i} ga qoldiqsiz bo\'linadi')




