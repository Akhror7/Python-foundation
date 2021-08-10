"""
Abdullayev Ahror
08/08/2021
ahror.abdullayev.2000@gmail.com
"""
class User:
    def __init__(self,login,ism,familiya,t_yil,email):
        self.login=login
        self.ism=ism
        self.familiya=familiya
        self.t_yil=t_yil
        self.email=email

    def get_info(self):
        return f"Yangi foydalanuvchi logini {self.login}, uning ismi {self.ism} ,familiyasi {self.familiya} , tug'ilgan yili {self.t_yil} , email manzili {self.email} "
    def get_age(self,yil=2021):
        return yil-self.t_yil


foydalanuvchi = User('mvp','Ahror','Abdullayev',2000,'ahror.abdullayev.2000@gamil.com')
foydalanuvchi1 = User('Dima','Dilmurod','Sadinov',2000,'dimabilan.2000@gamil.com')
foydalanuvchi2 = User('Mizik','Muhammad-Mizrob','Amononv',2001,'ar.abd.0@gamil.com')
foydalanuvchi3 = User('Ewon','Islom','O\'zbekxonov ',2000,'islom.2000@gamil.com')
print(foydalanuvchi.get_info())
print(foydalanuvchi2.get_age())









