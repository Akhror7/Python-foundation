# Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
# Obyekt haqida ma'lumot (__rerp__)
# Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)
# Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
# Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
# Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
# Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling.
#

class Odam:
    __o_son = 0
    def __init__(self,ism,familiya,tyil,millat):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.millat = millat
        Odam.__o_son +=1
    
    @classmethod
    def get_son(cls):
        return cls.__o_son
    
    def __repr__(self):
        return f"{self.familiya} {self.ism} {self.tyil}-yilda tug'ilgan , millati {self.millat}"
    
    def set_item(self, index, value):
        self.index = value

    def get_yosh(self, yil=2021):
        return yil-self.tyil
    
    def __eq__(self, y):
        if self.tyil == y.tyil:
            print(f"Odamlar bir yoshda")
        elif    self.tyil < y.tyil:
            print(f"{self.familiya} {self.ism} ning yoshi katta")
        elif self.tyil > y.tyil:
            print(f"{y.familiya} {y.ism} ning yoshi katta")


    
class Student(Odam):
    __s_son = 0
    def __init__(self,ism,familiya,tyil,millat,fakultet,id,bosqich = 1):
        super(Student, self).__init__(ism, familiya, tyil, millat)
        self.fakultet = fakultet
        self.__id = id
        self.bosqich = bosqich
        Student.__s_son +=1
  
    @classmethod
    def get_son(cls):
        return cls.__s_son

    def __repr__(self):
        return f"{self.familiya} {self.ism} {self.tyil}-yilda tug'ilgan , millati {self.millat}, {self.fakultet}ning {self.bosqich}-bosqich talabasi"

    def get_id(self):
        return self.__id

    def up_bosqich(self):
        return self.bosqich + 1

    def __call__(self):
        print(f"Talaba {self.familiya} {self.ism}")
        
    def __lt__(self, y):
        if self.bosqich > y.bosqich:
            print(f"{self.familiya} {self.ism} yuqori bosqichda")
        elif self.bosqich < y.bosqich:
            print(f"{y.familiya} {y.ism} yuqori bosqichda")
        else:
            print(f"Talabalar bir bosqichda")
        
    def __eq__(self, y):
        if self.bosqich == y.bosqich:
            print(f"Talabalar bir bosqichda")
        elif    self.bosqich > y.bosqich:
            print(f"{self.familiya} {self.ism} yuqori bosqichda")
        elif self.bosqich < y.bosqich:
            print(f"{y.familiya} {y.ism} yuqori bosqichda")



class Fan:
    def __init__(self, nomi):
        self.nom = nomi
        self.talabalar = []

    def add_talaba(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Student):
                self.talabalar.append(talaba)
            else:
                print(f"Iltimos talaba kiriting!")

    def __getitem__(self, index):
        return self.talabalar[index]

    def __setitem__(self, key, value):
        if isinstance(value, Student):
            self.talabalar[key] = value
        else:
            print(f"Iltimos talaba kiriting!")

    def __len__(self):
        return len(self.talabalar)

    def __add__(self, other):
        if isinstance(other, Fan):
            yangi_fan = Fan(f"{self.nom}{other.nom}")
            yangi_fan.talabalar = self.talabalar + other.talabalar
            return yangi_fan
        elif isinstance(other,Student):
            self.talabalar.append(other)
        else:
            print(f"Iltimos talaba yoki fan kiriting!")


    def __isub__(self, other):
        if isinstance(other,Student):
            self.talabalar.remove(other)
        else:
            for t in self.talabalar:
                if other == t.__id:
                    self.talabalar.remove(t)
                else:
                    print(f"{other} ID raqamli talaba yo'q")

    def __call__(self, *talaba):
        if talaba:
            for t in talaba:
                print(t)
        else:
            print(f"{self.nom} fani talabalari: {[t for t in self.talabalar]}")



yigit = Odam("Azizbek", "Lapasov", 2000, "O'zbek")
qiz = Odam("Parizod", "Axtamova", 2001, "O'zbek")

talaba1 = Student("Azizbek", "Xurramov", 1999, "O'zbek", "Iqtisodiyot", "K4507675", 3)
talaba2 = Student("Zuxriddin", "Baxriddinov", 1998, "O'zbek", "iqtisodiyot", "k3457879", 3)
talaba3 = Student("Shaxrizoda", "Raximova", 2000, "O'zbek", "iqtisodiyot", "k5467872", 3)
talaba4 = Student("Iroda", "Jumanova", 2001, "Qirg'iz", "iqtisodiyot", "k8763243", 2)
talaba5 = Student("Ali", "Valiyev", 2003, "Tojik", "biologiya","k8765432")
talaba6 = Student("Vali", "Aliyev", 2004, "Rus", "jimoniy madaniyat", "k3451235")

mat = Fan("Oliy matematika")
kim = Fan("Kimyo")
mat + talaba6
mat + talaba5
mat(talaba6)




