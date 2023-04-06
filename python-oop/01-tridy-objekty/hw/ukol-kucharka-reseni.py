class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False

    def __str__(self):
        return f"Recept {self.nazev} (narocnost {self.narocnost}) z webu {self.url_adresa}.  Vyzkoušen: {self.vyzkouseno}."

    def __repr__(self):
        return str(self)

    def zmen_narocnost(self, nova_hodnota):
        self.narocnost = nova_hodnota

    def zkusit(self):
        self.vyzkouseno = True


class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []

    def __str__(self):
        return f"Kuchařka se jmenuje {self.nazev}, napsala ji {self.autor}. Obsahuje {self.spocitej_recepty()} receptu."

    def spocitej_recepty(self):
        self.pocet_receptu = len(self.recepty)
        return self.pocet_receptu

    def pridej_recept(self, recept):
        self.recepty.append(recept)

    ## BONUS
    def najdi_vyzkousene_recepty(self):
        vyzkousene_recepty = []
        for recept in self.recepty:
            if recept.vyzkouseno:
                vyzkousene_recepty.append(recept)
        return f"{vyzkousene_recepty}"


## Pridam tiramisu
tiramisu = Recept("Tiramisu", 5, "url-adresa")
print(tiramisu)  # -> 'Tiramisu (narocnost: 5) - jeste nevyzkouseno'

## Pridam muffiny, vyzkousim a zmenim narocnost
muffiny = Recept("Muffiny", 3, "url-adresa")
# muffiny.zkusit()
muffiny.zmen_narocnost(2)
print(muffiny)  # -> Muffiny (narocnost: 2) - vyzkouseno'

moje_kucharka = Kucharka("Dezerty", "Aneta")
# print(moje_kucharka)  # -> 'Dezerty od Anety (0 receptu)'

## Pridam recepty do kucharky
moje_kucharka.pridej_recept(tiramisu)
moje_kucharka.pridej_recept(muffiny)
# print(moje_kucharka.spocitej_recepty())  # -> 2

# print(moje_kucharka)  # -> 'Dezerty od Anety (2 recepty)'

pernik = Recept("Pernik", 2, "url-adresa")
moje_kucharka.pridej_recept(pernik)
print(moje_kucharka)  # -> 'Dezerty od Anety (3 recepty)'

print(moje_kucharka.najdi_vyzkousene_recepty())  # => []
pernik.zkusit()
moje_kucharka.najdi_vyzkousene_recepty()  # => []

print(
    moje_kucharka.najdi_vyzkousene_recepty()
)  # => ['Pernik (narocnost: 2) - vyzkouseno']
