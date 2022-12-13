# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# - Vytvoř třídu `Balik`, která bude mít tři atributy - `adresa`, `hmotnost` a `doruceno`.
# První dva atributy nastav pomocí parametrů funkce `__init__`. Parametr `doruceno` nastav na začátku jako `False`.
# - Připoj ke třídě funkci `dorucit`, která změní hodnotu parametru `doruceno` na `True`.
# - Přidej metodu `__str__()`, která vypíše `adresu`, `hmotnost` a informaci o tom, zda byl balík již doručen.
# - Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.


class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.dorucen = False

    def dorucit(self):
        self.dorucen = True

    def __str__(self):
        return f"Balik na adresu {self.adresa}, hmotnost {self.hmotnost} - {'doručen' if self.dorucen else 'nedoručen'}"


b1 = Balik("Petr - Praha 10", 10)
print(b1)

b2 = Balik("Andrea - Plzeň", 20)
b2.dorucit()
print(b2)
