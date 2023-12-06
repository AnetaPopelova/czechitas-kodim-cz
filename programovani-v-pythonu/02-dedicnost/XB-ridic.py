# Pokračuj ve své práci pro zásilkovou společnost.
# Společnost nyní eviduje jednotlivé řidiče a eviduje balíky, které má každý řidič doručit.

# - Vytvoř třídu `Ridic`, která má dva atributy: `jmeno` (jméno řidiče) a `seznam_baliku` (seznam balíků k doručení, na
#   začátku je prázdný).
# - Přidej třídě metodu `prirad_balik`, která bude mít jeden parametr - `balik` (balík k doručení, může se jednat i o
#   cenný balík). Funkce nejprve zkontroluje, zda balík již nebyl doručen. Pokud ano, vypíše funkce text: "Nelze přiřadit,
#   balík již byl doručen." Pokud balík ještě nebyl doručen, je přidán do seznamu balíků `seznam_baliku` (použij
#   funkci `append`).
# - U řidiče chceme sledovat, kolik by měl ještě doručit balíků. Napiš funkci `zbyva_baliku`, která vrátí počet balíků,
#   které má řidič přiřazené a ještě je nedoručil.


class Ridic:
    def __init__(self, jmeno, seznam_baliku=None):
        self.jmeno = jmeno
        # osetruje priprad "mutable default argument"
        self.seznam_baliku = seznam_baliku or []

    def prirad_balik(self, balik):
        if balik.dorucen:
            print("Nelze přiřadit, balík již byl doručen.")
        else:
            self.seznam_baliku.append(balik)

    def zbyva_baliku(self):
        """Vrať počet balíků, které ejště nejsou doručnené.

        Výpočet využívá toho, že bool hodnoty True a False v proměnné balik.dorucen
         se v metodě sum budou chovat jako 1 a 0.
        """
        return sum(not balik.dorucen for balik in self.seznam_baliku)


b1 = CennyBalik("Pepa - Praha 10", 10, 200)
b2 = CennyBalik("Anna - Praha 1", 12, 50)
b3 = Balik("Josef - Plzeň", 5)
b4 = Balik("Tereza - Olomouc", 7)

b1.dorucit()
b3.dorucit()

r = Ridic("Karel", seznam_baliku=[b1, b2])
r.prirad_balik(b3)  # nepůjde. již byl doručen
r.prirad_balik(b4)

print(f"Zbývá doručit {r.zbyva_baliku()} balíků.")
