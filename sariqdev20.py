# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 00:34:22 2021

@author: MVP
"""

# def ok(ism,familiya,t_yil,t_joy,email,manzil='',tel=''):
#     '''Foydalanuvchidan kerakli ma\'lumotlarni olib lug\'at qayataruvchi funksiya'''
#     mijoz={'ism':ism,
#             'familiya':familiya,
#             'tug\'ilgan yili':t_yil,
#             'tug\'ilgan joyi':t_joy,
#             'e-mail manzili':email,
#             'manzili':manzil,
#             'telefon raqami':tel,
#             'yoshi':2021-int(t_yil)}
#     return mijoz
# mijozlar = []
# while True:
#     ism = input('Foydalanuvchi ismi?>>>')
#     familiya = input('Foydalanuvchi familiyasi?>>>')
#     t_yil = input('Foydalanuvchi tug\'ilgan yili?>>>')
#     t_joy = input('Foydalanuvchi tug\'ilgan joyi?>>>')
#     email = input('Foydalanuvchi e-maili?>>>')
#     manzil = input('Foydalanuvchi manzili?>>>')
#     tel = input('Foydalanuvchi raqami?>>>')
#     mijoz =ok(ism,familiya,t_yil,t_joy,email,manzil,tel)
#     mijozlar.append(mijoz)
#     a=input('Yana ma\'lumot kiratasizmi?>>>')
#     if a=='no':
#         print('Rahmat!')
#         break
# for mijoz in mijozlar:
#     print(f'Foydalanuvchi haqida ma\'lumotlar:')
#     for m in mijoz:
#         print(f'{m.capitalize()}:{mijoz[m]}')


# def katta(a,b,c):
#     k=max(a,b,c)
#     print(f'{k} eng katta ')
# katta(1,2,3)

# def aylana(r):
#     d=2*r
#     s=r**2*3.1415
#     c=2*r*3.1415
#     a = {
#         'radius':r,
#         'diametr':d,
#         'uzunligi':c,
#         'yuzi':s
#         }
#     return a
# r = float(input('r= '))
# a = aylana(r)
# for i,o in a.items():
#     print(f'{i}:{o}')


# def tub(a,b):
#     s = []
#     i=1
#     t=0
#     while a<b:
#         while i<=a:
#             if a%i==0:
#                 t=t+1
#             i=i+1
#         if t==2:
#             s.append(a)
#         t=0
#         i=1
#         a+=1
#     return s
# si = tub(5,78)
# print(si)

# quyida domla usuli
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar


# def son(s):
#     '''Fibonachchi ketma ketligi'''
#     i=1
#     t=1
#     l = [1]
#     while (len(l))<s:
#         l.append(i)
#         i=l[t-1]+l[t]
#         t+=1
#     return l
# lis = son(15)
# print(lis)




# i = 1
# l = [1]
# l.append(i)
# print(l)
# i=l[i-1]+l[i]
# print(i)




# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))





# def tub(a,b):
#     """Berilgan oraliqdagi tub sonlarni topadi"""
#     s = []
#     for i in range(a,b):
#         t = True
#         if i==0 or i==1:
#             t = False
#         else:
#             for x in range(2,i):
#                 if i%x==0:
#                     t = False
                
#         if t:
#             s.append(i)
#     return s
# s = tub(0,17)
# print(s)


# def fib(a):
#     """Fibonachchi ketma-ketligi"""
#     s = [1]
#     t= 1
#     for i in range(1,a+1):
#         s.append(t)
#         t=s[i-1]+s[i]
#     return s
# s= fib(14)
# print(s)


























