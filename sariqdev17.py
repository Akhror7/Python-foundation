# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:14:21 2021

@author: MVP
"""
# k = ''

# while k != 'stop':
#     k = input('Yaxshi ko\'rgan kitobongizni nomini kiriting Dasturni to\'xtatish uchun "stop" deb yozing>>>')
# print('Tugadi')
    
# yosh= ''
# while (yosh!='exit' and yosh!='quit'):
#     yosh = (input('Yoshingizni (kiriting(dasturni tugatish uchun exit yoki quit yozing):>>>')) 
#     if yosh=='exit' or yosh=='quit':
#         print('Tugadi')
#     else:
#         yosh = int(yosh)
#         if yosh<=7:
#             print(f'Siz uchun chipta narhi 2000 so\'m')
#         elif 7<yosh<=18:
#             print(f'Siz uchun chipta narhi 3000 so\'m')
#         elif 18<yosh<=65:
#             print(f'Siz uchun chipta narhi 10000 so\'m')
#         else:
#             print('Sizga chipta tekin')



savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat)<0:
        print('Musbat son emas!!!')
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

























