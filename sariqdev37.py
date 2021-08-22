class Car():
    def __init__(self, marka, rang, nom, km=0, narx=None):
        self.marka = marka
        self.rang = rang
        self.nom = nom
        self.__km = km
        self.narx = narx

    def get_info(self):
        info = f"{self.marka} avtomobili: {self.rang} {self.nom} "
        if not self.__km:
            info += f"{self.__km} km yurgan "
        if self.narx:
            info += f"narxi : {self.narx} "
        return info

    def add_km(self,km):
        if km>0:
            self.__km += km
        else:
            raise ValueError('Km manfiy bo\'la olmaydi')

    def set_price(self, price):
        self.narx = price

    def get_km(self):
        return self.__km


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

    def get_age(self, yil = 2021):
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
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan."
        info += f"Uning unvoni {self.unvon}"
        return info

















