# Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini konsolga chiqaring: talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
# Ushbu JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.
# Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash tili haqidagi maqolani JSON ko'rinishida ko'rishingiz mumkin. Brauzerda chiqqan ma'lumotni JSON ko'rinishida saqlang (brauzerda Ctrl+S tugmasini bosib). Faylni Pythonda oching va konsolga maqolaning sarlavhasi (title) va qisqa matnini (extract) chiqaring: https://uz.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Python
#
import json
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_j = json.dumps(data)
# # print(type(data_j))
#
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# #print(f"{talaba['ism']} {talaba['familiya']}")
#
# with open('data/json1','w') as f:
#     json.dump(data_j,f)
#     json.dump(talaba_json,f)
#
# with open('data/students.json','r') as f:
#    student = json.load(f)
# print(student)
#
# for dic in student['student']:
#     print(f"{dic['name']} {dic['lastname']} {dic['faculty']} fakulteti {dic['year']}-kurs talabasi")

with open('data/api-result.json','r') as f:
    text = json.load(f)

print(text)

print(f"{text['query']['pages']['13801']['title']}\n{text['query']['pages']['13801']['extract']}")




















































