import unittest
from sariqdev37 import Car, Shaxs, Professor

class TestCar(unittest.TestCase):
    def setUp(self):
        marka = 'Gm'
        rang = 'Oq'
        nom = 'Cobalt'
        self.km = 10000
        self.narx = 13000
        self.avto1 = Car(marka, rang, nom)
        self.avto2 = Car(marka, rang, nom, km=self.km, narx=self.narx)

    def test_info(self):
        self.assertEqual(self.avto1.get_info(), f'Gm avtomobili: Oq Cobalt 0 km yurgan ')

    def test_create(self):
        self.assertIsNotNone(self.avto1.marka)
        self.assertIsNotNone(self.avto1.rang)
        self.assertIsNotNone(self.avto1.nom)
        self.assertIsNone(self.avto1.narx)
        self.assertEqual(self.avto1.get_km(), 0)

        self.assertIsNotNone(self.avto2.marka)
        self.assertIsNotNone(self.avto2.rang)
        self.assertIsNotNone(self.avto2.nom)
        self.assertEqual(self.avto2.narx, self.narx)
        self.assertEqual(self.avto2.get_km(), self.km)

    def test_add_km(self):
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        new_km = -1000
        try:
            self.avto1.add_km(new_km)
        except ValueError as e:
            self.assertEqual(type(e), ValueError)


class Test(unittest.TestCase):
    def setUp(self):
        name = "Ahror"
        surname = "Abdullayev"
        passport = "AB6968227"
        year = 2000
        unvon = "Student"
        self.odam = Shaxs(name, surname, passport, year)
        self.talaba = Professor(name,surname, passport, year, unvon)

    def test_create(self):
        self.assertIsNotNone(self.odam.ism)
        self.assertIsNotNone(self.odam.familiya)
        self.assertIsNotNone(self.odam.passport)
        self.assertIsNotNone(self.odam.tyil)

        self.assertIsNotNone(self.talaba.ism)
        self.assertIsNotNone(self.talaba.familiya)
        self.assertIsNotNone(self.talaba.passport)
        self.assertIsNotNone(self.talaba.tyil)
        self.assertIsNotNone(self.talaba.unvon)

    def test_info(self):
        f = f'Ahror Abdullayev. Passport:AB6968227, 2000-yilda tug`ilgan'
        self.assertEqual(self.odam.get_info(), f)
        f1 = f'Ahror Abdullayev. Passport:AB6968227, 2000-yilda tug`ilgan.Uning unvoni Student'
        self.assertEqual(self.talaba.get_info(),f1)

    def test_age(self):
        self.assertEqual(self.talaba.get_age(),21)


































