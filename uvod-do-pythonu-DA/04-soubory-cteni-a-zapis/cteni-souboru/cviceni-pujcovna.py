# 3 Půjčovna (zavařovačka)

# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ.
# Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů.
# V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok.
# Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# V souboru s daty je ještě jeden problém, který není na první pohled vidět.
# Dá se vyřešit pomocí list comprehension s podmínkou uvedeném v předchozím čtení na doma.

# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().

# NEDELALI JSME - https://kodim.cz/kurzy/python-data/zaklady-programovani/prvni-programy/moduly
# Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce,
# abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.

with open("data/auta.txt", encoding="utf-8") as soubor:
    radky = soubor.readlines()

modifikovane_radky = []
for radek in radky:
    if radek.strip() != "":  # pokud radek obsahuje alespon jeden 'nebily' znak
        hodnoty = radek.split(" ")
        # spz, km = radek.split(' )
        spz = hodnoty[0]
        km = float(hodnoty[1].replace(",", "."))
        modifikovane_radky.append([spz, km])

jen_km = [radek[1] for radek in modifikovane_radky]

km_celkem = sum(jen_km)
print(km_celkem)


# osklivy one liner pomoci list comprehension
print(
    f"{sum([float(radek.split()[1].replace(',','.')) for radek in radky if radek.strip() != ''])} tisic kilometru"
)
