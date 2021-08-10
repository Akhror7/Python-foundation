# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
Author is Akhror
8/03/2021
ahror.abdullayev.2000@gmail.com
"""
from transliterate import to_latin , to_cyrillic
print(f"Assalomu alaykum, lotin-krill dasturiga xush kelibsiz!")
again = 1
while again:

    matn = input(f"iltimos, matn kiriting:\n")
    lk = matn.isascii()
    if lk:
        print(to_cyrillic(matn))
    else:
        print(to_latin(matn))
    again = int(input(f"Yana matn kritishni xohlaysizmi?ha(1)/yo'q(0)>>>"))
print(f"Salomat bo'ling")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
