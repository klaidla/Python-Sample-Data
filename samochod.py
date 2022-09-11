class Samochod:
    max_predkosc = 180
    ilosc_samochodow = 0
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.predkosc = 0
        Samochod.ilosc_samochodow += 1

    def jedz(self, predkosc:int):
        self.predkosc = self.max_predkosc if predkosc > self.max_predkosc else predkosc
        print(f'Jade z predkoscia {self.predkosc} km/h')

    def hamuj(self):
        if self.predkosc > 0:
            print('Hamuje...')
            self.predkosc = 0

    def __str__(self):
        return f'{self.marka} {self.model}, {self.rok_produkcji} - predkosc {self.predkosc}'


class Magazyn:
    def __init__(self):
        self.lista = []
        self.nazwa_pliku = 'auta.txt'

    def dodaj(self, auto:Samochod):
        self.lista.append(auto)

    def zapisz(self):
        # Zapisz w pliku auta.txt kazdy samochod w nowym wierszu (marka, model, rok_produkcji oddzielone przecinkami)
        with open(self.nazwa_pliku, 'w', encoding='utf-8') as f:
            for auto in self.lista:
                f.write(f'{auto.marka},{auto.model},{auto.rok_produkcji},{auto.predkosc},{auto.max_predkosc}\n')
        print(f'Zapisano do pliku {self.nazwa_pliku}')

    def wczytaj(self):
        # wyczysc liste przed wczytaniem
        self.lista.clear()
        with open(self.nazwa_pliku, encoding='utf-8') as f:
            for linia in f:
                wartosci = linia.split(',')
                auto = Samochod(wartosci[0], wartosci[1], wartosci[2])
                auto.max_predkosc = int(wartosci[4])
                auto.jedz(int(wartosci[3]))
                self.lista.append(auto)
        print(f'Wczytano z pliku {self.nazwa_pliku}')

    def wypisz(self):
        print('Lista samochodów w magazynie:')
        for auto in self.lista:
            print(auto)

    def usun_samochody_z(self, marka):
        self.lista = [auto for auto in self.lista if auto.marka.lower() != marka.lower()]


from datetime import date, timedelta

class Samochod:
    max_predkosc = 180
    ilosc_samochodow = 0
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.predkosc = 0
        Samochod.ilosc_samochodow += 1

    def jedz(self, predkosc:int):
        self.predkosc = self.max_predkosc if predkosc > self.max_predkosc else predkosc
        print(f'Jade z predkoscia {self.predkosc} km/h')

    def hamuj(self):
        if self.predkosc > 0:
            print('Hamuje...')
            self.predkosc = 0

    def __str__(self):
        return f'{self.marka} {self.model}, {self.rok_produkcji} - predkosc {self.predkosc}'


class SportowySamochod(Samochod):
    max_predkosc = 260
    def __init__(self, marka, model, rok_produkcji, kolor, dni_do_przegladu):
        super().__init__(marka, model, rok_produkcji)
        self.kolor = kolor
        self.data_utworzenia = date.today()
        self.data_przegladu = self.data_utworzenia + timedelta(days=dni_do_przegladu)

    def czy_aktualny_przeglad(self):
        return date.today() <= self.data_przegladu

    def __str__(self):
        return f'{super().__str__()}, kolor {self.kolor}, data przeglądu {self.data_przegladu}'


class Magazyn:
    def __init__(self):
        self.lista = []
        self.nazwa_pliku = 'auta.txt'

    def dodaj(self, auto:Samochod):
        self.lista.append(auto)

    def zapisz(self):
        # Zapisz w pliku auta.txt kazdy samochod w nowym wierszu (marka, model, rok_produkcji oddzielone przecinkami)
        with open(self.nazwa_pliku, 'w', encoding='utf-8') as f:
            for auto in self.lista:
                f.write(f'{auto.marka},{auto.model},{auto.rok_produkcji},{auto.predkosc},{auto.max_predkosc}\n')
        print(f'Zapisano do pliku {self.nazwa_pliku}')

    def wczytaj(self):
        # wyczysc liste przed wczytaniem
        self.lista.clear()
        with open(self.nazwa_pliku, encoding='utf-8') as f:
            for linia in f:
                wartosci = linia.split(',')
                auto = Samochod(wartosci[0], wartosci[1], wartosci[2])
                auto.max_predkosc = int(wartosci[4])
                auto.jedz(int(wartosci[3]))
                self.lista.append(auto)
        print(f'Wczytano z pliku {self.nazwa_pliku}')

    def wypisz(self):
        print('Lista samochodów w magazynie:')
        for auto in self.lista:
            print(auto)

    def usun_samochody_z(self, marka):
        self.lista = [auto for auto in self.lista if auto.marka.lower() != marka.lower()]


xc60 = Samochod('Volvo', 'XC60', 2015)
duster = Samochod('Dacia', 'Duster', 2012)
fiat = Samochod('Fiat', '126p', 1998)

magazyn = Magazyn()
magazyn.dodaj(xc60)
magazyn.dodaj(duster)
magazyn.dodaj(fiat)
magazyn.wypisz()

xc60.jedz(60)
duster.jedz(120)
fiat.jedz(30)
fiat.hamuj()
fiat.max_predkosc = 220
duster.jedz(200)
fiat.jedz(200)

magazyn.zapisz()
magazyn.lista.clear()
magazyn.wczytaj()
magazyn.wypisz()




bmwM3Gtr = SportowySamochod('BMW', 'M3 BTR', 2020, 'czarny', 170)
bmwM3Gtr.jedz(250)
print(bmwM3Gtr)


xc60 = Samochod('Volvo', 'XC60', 2015)
duster = Samochod('Dacia', 'Duster', 2012)
fiat = Samochod('Fiat', '126p', 1998)

magazyn = Magazyn()
magazyn.dodaj(xc60)
magazyn.dodaj(duster)
magazyn.dodaj(fiat)
magazyn.wypisz()

xc60.jedz(60)
duster.jedz(120)
fiat.jedz(30)
fiat.hamuj()
fiat.max_predkosc = 220
duster.jedz(200)
fiat.jedz(200)

magazyn.zapisz()
magazyn.lista.clear()
magazyn.wczytaj()
magazyn.wypisz()

'''MAGICZNE '''
def __eq__(self,
           other):  # freemont1(self) == freemont2(other)       Samochod.__eq__(feemont1, freemont2)   freemont1.__eq__(freemont2)
    return self.marka == other.marka and self.model == other.model


def __ne__(self, other):  # freemont1 != freemont2
    ...


def __gt__(self, other):  # freemont1 > freemont2    (rok produkcji freemont1 > rok produkcji freemont2)
    ...


def __lt__(self, other):  # freemont1 < freemont2
    ...


def __ge__(self, other):  # freemont1 >= freemont2
    ...


def __le__(self, other):  # freemont1 <= freemont2
    ...

freemont1 = Samochod('fiat', 'freemont', 2021)
freemont2 = Samochod('fiat', 'freemont', 2021)


