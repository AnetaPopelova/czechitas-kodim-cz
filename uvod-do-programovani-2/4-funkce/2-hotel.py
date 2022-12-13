# Napiš funkci total_price, která vypočte cenu noci v hotelu.
# Funkce bude mít dva parametry - persons a breakfast.
# Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč.
# Funkce vrátí výslednou cenu.
# Parametr breakfast je nepovinný a výchozí hodnota je False.


def total_price(persons, breakfast=False):
    price_per_person = 850
    if breakfast:
        price_per_person += 125
    return price_per_person * persons


print(total_price(3))
print(total_price(3, True))


# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

print(f"Cena za tři lidi: {total_price(3)}")
print(f"Cena za dva lidi se snidani: {total_price(2, True)}")


# Uplne genialni kod co vymyslela Paja Vencovska
# def total_price(persons, breakfast=False):
#     breakfast *= 125 * persons
#     persons *= 850
#     return breakfast + persons


# print(total_price(persons=3, breakfast=False))

# # Nebo jeste jina varianta
# def total_price(persons, breakfast=False):
#     night_price = 850
#     breakfast_price = 125

#     nights_total = night_price * persons
#     breakfast_total = 0
#     if breakfast:
#         breakfast_total += breakfast_price * persons
#     return nights_total + breakfast_total


# print(total_price(3, False))
