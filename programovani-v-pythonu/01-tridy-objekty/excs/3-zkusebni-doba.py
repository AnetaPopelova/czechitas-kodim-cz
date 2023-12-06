# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.


class Zamestnanec:
    def __init__(self, jmeno, pozice):
        self.jmeno = jmeno
        self.pozice = pozice

    def __str__(self):
        return f"{self.jmeno} pracuje na pozici {self.pozice}."


# Rozšiř metodu `__init__` třídy `Zamestnanec` o parametr `zkusebni_doba`, který bude typu `bool`.
# Tuto hodnotu ulož jako atribut třídy `Zamestnanec`.
# Uprav metodu `__str__()`.
# Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text "Je ve zkušební době."


class Zamestnanec:
    def __init__(self, jmeno, pozice, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.zkusebni_doba = zkusebni_doba

    def __str__(self):
        return (
            f"{self.jmeno} pracuje na pozici {self.pozice}."
            f"{' Je ve zkušební době.' if self.zkusebni_doba else ''}"
        )


z1 = Zamestnanec("Karel", "dělník", zkusebni_doba=False)
print(z1)

z2 = Zamestnanec("Josef", "brigádník", zkusebni_doba=True)
print(z2)
