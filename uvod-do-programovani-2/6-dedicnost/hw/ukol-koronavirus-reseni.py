class Nemoc:
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f"Jmeno: {self.jmeno}"

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti


class Koronavirus(Nemoc):
    def __init__(self, jmeno, varianty=[]):
        super().__init__(jmeno, 12, 0, "vzduchem")
        self.varianty = varianty

    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)

    def __str__(self):
        return f'{super().__str__()}, má varianty: {", ".join(self.varianty)}'


# Priklad pouziti:
omikron = Koronavirus("Coronavirus", ["omikron"])
print(omikron)  # 'Jmeno: Coronavirus (varianty: omikron)'
corona = Koronavirus("Coronavirus")
corona = Koronavirus("Coronavirus", [])  # melo by fungovat stejne jako predchozi radek
print(corona)  # 'Jmeno: Coronavirus (zadne nalezene varianty)'
print(
    corona.pocet_obeti
)  # nejake cislo ktere se da menit pomoci metody zmen_pocet_obeti() - muze byt nacatku nula nebo cislo ktere si zvolite pri vytvoreni objektu
print(corona.sireni)  # 'vzduchem' -- muzete reprezentovat i cislem
print(
    corona.inkubacni_doba
)  # 12 -- je mi jedno jake cislo - pevne dane ve volani super().__init__(...)
corona.pridej_variantu("omikron")
corona.pridej_variantu("delta")
print(corona)  # 'Jmeno: Coronavirus (varianty: omikron, delta)'
corona.pridej_variantu("alpha")
print(corona)  # 'Jmeno: Coronavirus (varianty: omikron, delta, alpha)'
