# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 03:26:18 2021

@author: MVP
"""
ismlar = ['Dilmurod','Azizbek','Shexroz']
print(f'Salom {ismlar[1]},bugun choyxonaga boramizmu?\n')
print(f'Salom {ismlar[0]},bugun choyxonaga boramizmu? \n')
print(f'Salom {ismlar[2]},bugun choyxonaga boramizmu? \n')

sonlar = [1,-9,0.56,'a',-0.23,12,25,-96]
try:
    print(f'{sonlar[1]}+{sonlar[3]}={sonlar[1]+sonlar[3]}\n')
    print(f'{sonlar[2]}-{sonlar[3]}={sonlar[2]-sonlar[3]}\n')
    print(f'{sonlar[4]}/{sonlar[2]}={sonlar[4]/sonlar[2]}\n')
    print(f'{sonlar[0]}*{sonlar[1]}={sonlar[0]*sonlar[1]}\n')
except:
    print("amallar faqat sonlar ustida bo'ladi")
sonlar[0] = sonlar[0]+4
sonlar[1] = sonlar[2]-5
sonlar[4] = 123
del sonlar[-1]

print(sonlar)

t_shaxslar = ['imom Buxoriy','Abu bakr','Amir Temur','Ibrohim alayhissalom']
z_shaxslar = ['Muhammadali','Duvrov','Putin','Elon Musk']

print(f' Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(3)} bilan suhbat qilishni xohlar edim')

friends = []
friends.append('Eshon')
friends.append('Eshon2')
friends.append('Azizbek')
friends.append('Dilmurod')
friends.append('Ravshan')
friends.append('Laziz')
print(friends)
friends.remove('Laziz')
friends.insert(0,'Shexroz')
friends.insert(3,'Shoxruh')
friends.insert(7,'Mehroj')
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(0))

print(mehmonlar)




