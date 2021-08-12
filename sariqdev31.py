class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __o_son = 0
    def __init__(self, ism, familiya, passport, tyil,millat='o\'zbek'):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__millat = millat
        Shaxs.__o_son +=1
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    def get_millat(self):
        return f"Shaxs millati {self.__millat}"
    @classmethod
    def get_son(cls):
        return cls.__o_son
class Talaba:
    """Talaba klassi"""
    __t_son = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam,jinsi ):
        """Talabaning xususiyatlari"""
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []
        self.__jins = jinsi
        Talaba.__t_son +=1
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def set_fan(self,fan):
        self.fanlar.append(fan)

    def del_fan(self,fan):
        self.fanlar.remove(fan) if fan in self.fanlar else print(f"siz {fan}ga yozilmagansiz")
    def get_jinsi(self):
        return self.__jins
    @classmethod
    def get_son(cls):
        print(cls.__t_son)

talabacha = Talaba("Dilmurod","Sadinov","AA5448789",2000,"K3423545","Odamni erkaki")
talabacha = Talaba("Dilmurod","Sadinov","AA5448789",2000,"K3423545","Odamni erkaki")
talabacha = Talaba("Dilmurod","Sadinov","AA5448789",2000,"K3423545","Odamni erkaki")
odamcha  = Shaxs("Dilmurod","Sadinov","AA5448789",2000)
print(odamcha.get_millat())
print(odamcha.get_son())
talabacha.get_son()




















