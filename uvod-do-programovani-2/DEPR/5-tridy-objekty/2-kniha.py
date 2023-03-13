# Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Kniha, která reprezentuje knihu.
# Každá kniha bude mít atributy nazev, pocet_stran a cena.
# Hodnoty nastav ve funkci __init__.

# Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.
# Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou.
# Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech.
# Funkce sníží cenu knihy o dané procento.


class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena

    def sleva(self, procent):
        self.cena *= 1 - (procent / 100)

    def __str__(self):
        return f"{self.nazev}, {self.pocet_stran} stran - {self.cena} Kč"


k = Kniha("Motýlek", 300, 100)
print(k)
k.sleva(20)
print(k)
