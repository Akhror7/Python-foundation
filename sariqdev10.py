# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 22:04:12 2021

@author: MVP
"""

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for c in cars:
#     if c.lower != 'gm':
#         print(c.title())
#     else:
#         print(c.upper()) 

# l = input('Loginni kiriting>>>')
# if l.lower=='admin':
#     print(f'Xush kelibsiz ,Admin , foydalanuvchilar ro\'yxatini ko\'rasizmi?')
# else:
#     print(f'Xush kelibsiz, {l.title()}')

# while True:
#     try:
#         a = float(input('1-son>>>'))
#         b = float(input('2-son>>>'))
#     except:
#         print("Iltmos son kiriting")
#     else:
#         break
# if a==b:
#     print('sonlar teng')
while True:
    try:
        son = float(input('son kiriting>>>'))
    except:
        print("Iltimos son kiriting")
    else:
        break
if son>0:
    print('musbat son')
elif son<0:
    print('manfiy son')

if son>0:
    print(f'{son} ning ildizi = {son**0.5}')
else:
    print('Musbat son kiriitng')











