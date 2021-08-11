# class Talaba:
#     """Talaba klassi"""
#
#     def __init__(self, ism, familiya, passport, tyil, idraqam, ):
#         """Talabaning xususiyatlari"""
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.fanlar = []
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
#
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info
#     def set_fan(self,fan):
#         self.fanlar.append(fan)
#
#     def del_fan(self,fan):
#         self.fanlar.remove(fan) if fan in self.fanlar else print(f"siz {fan}ga yozilmagansiz")
#
#
# class Fan:
#     def __init__(self,tur,nom):
#         self.tur = tur
#         self.nom = nom
#     def get_info(self):
#         info = f"{self.tur} fanlar turkumidagi {self.nom} fani"
#         return info
#
# talaba1 = Talaba('Vali','Aliyev','AA3245432',1999,'k234223')
# fan1 = Fan('ijtimoiy','tarix')
# fan2 = Fan('aniq','matematika')
#
# talaba1.set_fan(fan1)
# talaba1.set_fan(fan2)
# talaba1.del_fan(fan2)
#
# print([fan.get_info() for fan in talaba1.fanlar])
#
#

class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Professor(Shaxs):

    def __init__(self, ism, familiya, passport, tyil,  unvon):
        super().__init__( ism, familiya, passport, tyil)
        self.unvon = unvon
    def get_unvon(self):
        print(f"Bu professorning unvoni {self.unvon}")
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        info += f"Uning unvoni {self.unvon}"
        return info
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, id, parol):
        super().__init__( ism, familiya, passport, tyil)
        self.id = id
        self.parol = parol
    def get_id(self):
        print(f"Foydalanuvchi ID si {id}")
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        info += f"ID:{self.id}, parol:{self.parol}"
        return info

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, id, parol, daraja):
        super().__init__(ism, familiya, passport, tyil, id, parol)
        self.daraja = daraja
    def ban_user(self,foydalanuvchi):
        print(f"{foydalanuvchi} bloklandi")
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        info += f"ID:{self.id}, parol:{self.parol}"
        info += f" Daraja:{self.daraja}"
        return info
admin1 = Admin('Ahror', 'Abdullayev', 'AA6968227', 2000, "k1235442", "kracav4ik", 'katta')
foydal = Foydalanuvchi('Ahror', 'Abdullayev', 'AA6968227', 2000, "k1235442", "kracav4ik")
print(foydal.get_info())
print(admin1.get_info())
admin1.ban_user(foydal)