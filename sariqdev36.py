# uchta son qabul qilib , kattasini qaytaruvchi funksiya
#
# while True:
#     a = input("a = ")
#     if a.isdigit():
#         b = input("b = ")
#         if b.isdigit():
#             c = input('c = ')
#             if c.isdigit():
#                 break
#             else:
#                 print('Iltimos son kiriting')
#         else:
#             print('Iltimos son kiriting')
#     else:
#         print('Iltimos son kiriting')
#

def max_son(a, b, c):
    return max(a, b, c)


#matnlardan iborat ro'yxat qilib har birini birinchi harfni bosh harfga o'zgartiruvchi funksiya

b = ['shror', 'afrika', 'osiyo' ]
def upper_list(lis):
    for i in range(len(lis)):
        lis[i] = lis[i].title()

    return lis




#berilgan sonlar ro'yxatidan juft son ajratib oluvchi funksiya
def tub_son(a):
    b=[]
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b



#fibonachchi ketma - ketligi
def fibonaci(k,n):
    fb = [1, 1]
    for i in range(100):
        son = fb[i]+fb[i+1]
        fb.append(son)
    return  k in fb


































