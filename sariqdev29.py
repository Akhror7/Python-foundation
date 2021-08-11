class Avto:
    def __init__(self,markasi,nomi,narxi):
        self.markasi=markasi
        self.nomi=nomi
        self.narxi=narxi
        self.rangi='oq'
        self.yili=2021
        self.km=0
    def get_info(self):
        return f"Avtomobil {self.rangi} {self.markasi} {self.nomi} {self.yili} - da ishlab chiqarilgan {self.km} yurgan, uning narxi {self.narxi}$ "
    def update_km(self):
        self.km+=1000
    def set_km(self,km):
        self.km+=km


class Avtosalon:
    def __init__(self,nom,manzil):
        self.nom=nom
        self.manzil=manzil
        self.avtolar=[]
        self.avtolar_soni=0
    def add_avto(self,avto):
        self.avtolar_soni+=1
        self.avtolar.append(avto)
    def get_avtolar(self):
        return  [avto.get_info() for avto in self.avtolar]
    def get_avtolar_soni(self):
        print(self.avtolar_soni)

avto1 = Avto("chevrolet","gentra",13000)
avto2 = Avto("chevrolet","tracker",23000)
avto3 = Avto("lada","cross",12000)
avto4 = Avto("chevrolet","tahoe",73000)
chevrolet = Avtosalon("chevrolet","samarqand")
chevrolet.add_avto(avto1)
chevrolet.add_avto(avto2)
chevrolet.add_avto(avto3)
chevrolet.add_avto(avto4)

print(chevrolet.get_avtolar())






