'''
    Python 3
'''
class Vozilo:
    def __init__(self, znamka, model, kilometri, zadnji_servis):
        self.znamka = znamka
        self.model = model
        self.kilometri = kilometri
        self.zadnji_servis = zadnji_servis

class BazaVozil:
    vozila = []
    pot = "vozila.txt"

    def __init__(self):
        try:
            with open(self.pot, "r") as f:
                for vrstica in f:
                    znamka, model, kilometri, zadnji_servis = vrstica.split(";")
                    self.vozila.append(Vozilo(znamka, model, int(kilometri), zadnji_servis))
        except:
            with open(self.pot, "w"):
                pass
                    
    def izpisi(self):
        indeks = 1
        for v in self.vozila:
            print("Vozilo ", indeks)
            print("               Znamka: ", v.znamka)
            print("                Model: ", v.model)
            print("  Prevoženi kilometri: ", v.kilometri)
            print("        Zadnji servis: ", v.zadnji_servis)
            print()
            indeks += 1

    def dodaj(self):
        znamka = input("Znamka: ")
        model = input("Model: ")
        kilometri = int(input("Prevoženi kilometri: "))
        zadnji_servis = input("Zadnji servis: ")
        self.vozila.append(Vozilo(znamka, model, kilometri, zadnji_servis))

    def izbrisi(self):
        indeks = int(input("Zaporedno število vozila: ")) - 1
        del self.vozila[indeks]

    def uredi_kilometre(self):
        indeks = int(input("Zaporedno število vozila: ")) - 1
        v = self.vozila[indeks]
        print("Prevoženi kilometri (stari): ", v.kilometri)
        v.kilometri = int(input("Prevoženi kilometri (novi): "))

    def uredi_zadnji_servis(self):
        indeks = int(input("Zaporedno število vozila: ")) - 1
        v = self.vozila[indeks]
        print("Zadnji servis (stari): ", v.zadnji_servis)
        v.zadnji_servis = input("Zadnji servis (novi): ")

    def shrani(self):
        with open(self.pot, "w") as f:
            for v in self.vozila:
                f.write("%s;%s;%d;%s\n" % (v.znamka, v.model, v.kilometri, v.zadnji_servis))

bazaVozil = BazaVozil()

izbira = ""

while izbira != "6":
    print("1 - Izpiši vozila")
    print("2 - Dodaj vozilo")
    print("3 - Izbriši vozilo")
    print("4 - Uredi prevožene kilometre")
    print("5 - Uredi datom zadnjega servisa")
    print("6 - Shrani in končaj")
    izbira = input("Izbira: ")

    if izbira == "1": bazaVozil.izpisi()
    elif izbira == "2": bazaVozil.dodaj()
    elif izbira == "3": bazaVozil.izbrisi()
    elif izbira == "4": bazaVozil.uredi_kilometre()
    elif izbira == "5": bazaVozil.uredi_zadnji_servis()

bazaVozil.shrani()
