# Napište program, který vypíše na výstup:
#   všechny povinné a nepovinné domácí cvičení
#   z lekce První programy
#   spolu s jejich obtížností.

from requests_html import HTMLSession

URL = "https://kodim.cz/kurzy/python-data/zaklady-programovani/prvni-programy/prvni-programy"

session = HTMLSession()
stranka = session.get(URL)

for uloha in stranka.html.find(".exercise-assign"):
    for nazev in uloha.find("h3"):
        nazev_ulohy = nazev.text
    for obtiznost in uloha.find(".demand-text"):
        obtiznost_ulohy = obtiznost.text
        print(f"Úloha {nazev_ulohy} je {obtiznost_ulohy}.")

# session.close()
