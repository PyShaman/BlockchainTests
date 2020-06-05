import random
from datetime import datetime
from datetime import timedelta

class Produkt:
    def __init__(self,ID = 1,  nazwa="Jablka", kategoria = "owoce", vat =5, cena_netto =12):
        self.ID = ID
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.vat = vat
        self.cena_netto = cena_netto
    def get_ID(self):
        f=open("products.json", 'r')
        lines = f.readlines()
        self.ID = lines[2]
        f.close()
    def get_nazwa(self):
        f = open("products.json", 'r')
        lines = f.readlines()
        self.nazwa=lines[3]
        f.close()
    def get_kategoria(self):
        f = open("products.json")
        lines = f.readlines()
        self.kategoria=lines[5]
        f.close()
    def get_cenanetto(self):
        f=open("products.json", 'r')
        lines = f.readlines()
        self.cena_netto = lines[6]
        f.close()
    def get_vat(self):
        f = open("products.json", 'r')
        lines = f.readlines()
        self.vat = lines[8]
        f.close()

produkt_1 = Produkt()
produkt_1.get_ID()
produkt_1.get_cenanetto()
produkt_1.get_kategoria()
produkt_1.get_vat()
produkt_1.get_nazwa()

class Klient(object):
    def __init__(self,ID,miasto , ulica, kod_pocztowy, nr_budynku,nr_mieszkania , mail, rodzaj):
        self.ID = ID
        self.miasto = miasto
        self.ulica = ulica
        self.kod_pocztowy = kod_pocztowy
        self.nr_budynku = nr_budynku
        self.nr_mieszkania = nr_mieszkania
        self.mail = mail
        self.rodzaj = rodzaj
    def get_ID(self):
        f=open("Klient.txt", 'r')
        lines = f.readlines()
        self.ID = lines[2]
    def city(self):
        f = open("Klient.txt", 'r')
        lines = f.readlines()
        self.miasto = lines[16]
        f.close()
    def get_ulica(self):
        f= open("Klient.txt" , 'r')
        lines = f.readlines()
        self.ulica = lines[8]
        f.close()
    def get_kod_pocztowy(self):
        f = open("Klient.txt" , 'r')
        lines = f.readlines()
        self.kod_pocztowy = lines[14]
        f.close()
    def get_nrmieszkania(self):
        f=open("Klient.txt", 'r')
        lines = f.readlines()
        self.nr_mieszkania = lines[12]
        f.close()
    def get_nrbudynku(self):
        f=open("Klient.txt",'r')
        lines = f.readlines()
        self.nr_budynku = lines[10]
        f.close()
    def get_mail(self):
        f=open("Klient.txt" , 'r')
        lines = f.readlines()
        self.mail = lines[6]
        f.close()
    def get_rodzaj(self):
        f=open("Klient.txt",'r')
        lines = f.readlines()
        self.rodzaj = lines[19]
        f.close()

    def adres_dostawy(self):
            print(f"{self.mail}\n ul. {self.ulica} {self.nr_budynku} m.{self.nr_mieszkania}\n {self.kod_pocztowy} {self.miasto}\n POLSKA\n")

class Klient_indywidualny(Klient):
    def __init__(self, ID='',imie="", nazwisko="", ulica="szara", nr_budynku='', nr_mieszkania='', kod_pocztowy='', miasto='', mail='', rodzaj=0):
        super().__init__(ID,miasto, ulica, kod_pocztowy, nr_budynku, nr_mieszkania, mail,rodzaj)
        self.imie=imie
        self.nazwisko=nazwisko

    def get_imie(self):
        f= open("Klient.txt", 'r')
        lines = f.readlines()
        self.imie = lines[3]
        f.close()
    def get_nazwisko(self):
        f = open("Klient.txt",'r')
        lines = f.readlines()
        self.nazwisko = lines[4]
    def adres_dostawy(self):
        print(f"Dane odbiorcy:\n {self.imie} {self.nazwisko} ")
        super().adres_dostawy()

klient = Klient_indywidualny()
klient.get_ID()
klient.get_imie()
klient.get_nazwisko()
klient.get_ulica()
klient.city()
klient.get_kod_pocztowy()
klient.get_nrbudynku()
klient.get_nrmieszkania()
klient.get_mail()
klient.get_rodzaj()


class Firma(Klient):
    def __init__(self,ID, NIP, ulica, nr_budynku, nr_mieszkania, kod_pocztowy, miasto, mail, rodzaj = 1):
        super(). __init__(ID,miasto,ulica,kod_pocztowy,nr_budynku, nr_mieszkania,mail,rodzaj)
        self.NIP = NIP

    def adres_dostawy(self):
        print(f"Dane odbiorcy: \n {self.NIP}")
        super().adres_dostawy()


class Zamowienie(object):
    def __init__(self,ID=1, nazwa_produktu='', ilosc_produktow='', Vat='',kwota_brutto='', cena_netto='', cena='', data_wystawienia='', data_sprzedazy='', czas_platnosci='', numer_paragonu=''):
        self.ID = ID
        self.nazwa_produktu = nazwa_produktu
        self.ilosc_produktow = ilosc_produktow
        self.Vat = Vat
        self.kwota_brutto = kwota_brutto
        self.cena_netto = cena_netto
        self.cena = cena
        self.data_wystawienia = data_wystawienia
        self.data_sprzedazy = data_sprzedazy
        self.czas_platnosci = czas_platnosci
        self.numer_paragonu = numer_paragonu

    def get_ID(self):
        f = open("Zamowienie.txt",'r')
        lines = f.readlines()
        self.ID = lines[1]
        f.close()
    def get_nazwa_produktu(self):
        f = open("Zamowienie.txt")
        lines = f.readlines()
        self.nazwa_produktu= lines[2]
        f.close()
    def get_ilosc(self):
        return 5

    def get_cenanetto(self):
        f=open("Zamowienie.txt")
        lines = f.readlines()
        self.cena_netto = lines[3]
        f.close()
    def get_Vat(self):
        f=open("Zamowienie.txt")
        lines = f.readlines()
        self.Vat= lines[5]
        f.close()
    def get_kwotabrutto(self):
        f = open("Zamowienie.txt", 'r')
        lines = f.readlines()
        self.kwota_brutto = lines[6]
        print(f"{self.kwota_brutto}")

zamowienie_1 = Zamowienie()
zamowienie_1.get_ilosc()
numer = str(random.randrange(88888888))
now = datetime.now()
data = now.strftime("%d/%m/%Y %H:%M:%S")
pozniej = ((datetime.now() + timedelta(days=11)))
Zaplata = pozniej.strftime("%d/%m/%Y %H:%M:%S")
#Cena = int(produkt_1.get_cenanetto() * zamowienie_1.get_ilosc())
f =open("Faktura", 'w')
f.write("\t\t\t PARAGON\n")
f.write("nr_paragonu: " + numer + '\n')
f.write("data sprzedazy: " + data + '\n')
f.write("Sklep A.O\n")
f.write(f"Produkty: {zamowienie_1.get_ilosc()}\n")
#f.write("Cena za sztukę: " + produkt_1.get_cenanetto()  + "zl" + '\n')
#f.write("Ilość : " + zamowienie_1.get_ilosc() + "\n" )
#f.write("Cena netto: " + produkt_1.get_cenanetto() + 'zl'+ '\n')
f.close()

def main():
    klient_1 = Klient_indywidualny()
    firma_1 = Firma(2,"20197361","Szara", 23, 1, "21-421", "Krakow", "rmainfiwd.pl")
    #klient_1.adres_dostawy()
    #firma_1.adres_dostawy()
    #faktura.zamowienie()
    #paragon.zamowienie()
    #klient_1.adres_dostawy()
numer=str(random.randrange(888888))
