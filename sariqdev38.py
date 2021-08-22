import datetime as dt
import re

bugun = dt.date.today()
#
# for i in range(100):
#     if bugun.month in [1, 3, 5, 7, 8, 10, 12]:
#         m = 31
#     elif bugun.month == 2:
#         m = 28
#     else:
#         m = 30
#     kun = bugun.day + 1
#     if kun <= m :
#         bugun = bugun.replace(day = kun)
#     else:
#         bugun = bugun.replace(month=bugun.month+1,day=1)
#     print (bugun)

rh = dt.date(2022,5,2)
qh = dt.date(2022,7,10)
tk = dt.date(2000,6,1)
frh = rh - bugun
fqh = qh -bugun
print(f"Mana azizlar ramazon hayitigacha {frh.days} kun va qurbon hayitagacha {fqh.days} kun qoldi")

tel = '(?:\+\([9]{2}[8]\)[0-9]{2}\ [0-9]{3}\-[0-9]{2}\-[0-9]{2})'
t= input('tel>>>')
if re.match(tel,t):
    print('rahmat')
else:
    t = input('qayta>>>')



andoza = "((http|ftp)s?://.*?)"
url = '<p>Hello World</p><a href="http://example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>'
print(re.findall(andoza,url))
























