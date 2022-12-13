# Káva na Mall.cz

# Jedna ze stránek, která má pěknou strukturu pro scrapování, je například Mall.cz.
# Můžete si zde v bezpečí potrénovat své scrapovací schopnosti dříve, než budete zkoušet vytáhnout data z nějaké webovky, která je napsaná trošku víc prasácky.

# Vaším úkolem v tomto cvičení je napsat program, který stáhne všechny nabízené instantní kávy ze stránky www.mall.cz/instantni-kava.
# Výstupem vašeho programu bude CSV soubor, který bude obsahovat tři sloupečky: název produktu, cena a zda je produkt skladem.

from requests_html import HTMLSession
import csv

URL = "https://www.mall.cz/instantni-kava"

session = HTMLSession()
stranka = session.get(URL)

seznam_produktu = []

for produkt in stranka.html.find(".pbcr"):
    for nazev in produkt.find(".pbcr__title"):
        nazev_produktu = nazev.text
    for cena in produkt.find(".pbcr__price"):
        cena_produktu = cena.text.replace("\xa0", " ")
    for dostupnost in produkt.find(".pbcr__availability"):
        dostupnost_produktu = dostupnost.text
    zaznam_produktu = [nazev_produktu, cena_produktu, dostupnost_produktu]
    seznam_produktu.append(zaznam_produktu)

# toto reseni zanedbava problematiky strankovani (pagination),
# tedy nacitani dalsich produktu po dosazeni "konce stranky"
with open("ceny-kavy.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["nazev", "cena", "dostupnost"])
    writer.writerows(seznam_produktu)

# session.close()
