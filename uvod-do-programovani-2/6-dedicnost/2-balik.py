# Pokračuj ve své práci pro zásilkovou společnost.
# Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

# Vytvoř třídu CennyBalik, která dědí od třídy Balik.
# CennyBalik má navíc atribut hodnota, ostatní atributy dědí od třídy Balik.
# Atribut hodnota nastav pomocí funkce __init__.
# Ostatní parametry předej funkci __init__ třídy Balik.
# Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.


class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.dorucen = False

    def dorucit(self):
        self.dorucen = True

    def __str__(self):
        return (
            f"Balik na adresu {self.adresa}, hmotnost {self.hmotnost}"
            f' - {"doručen" if self.dorucen else "nedoručen"}'
        )


class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota):
        super().__init__(adresa, hmotnost)
        self.hodnota = hodnota

    def __str__(self):
        return super().__str__() + f" - hodnota: {self.hodnota}"


b1 = CennyBalik("Pepa - Praha 10", 10, 200)
b1.dorucit()
print(b1)
