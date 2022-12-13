# 2 Hody kostkou (zapni hlavu)
# Napište program, který vytvoří seznam deseti náhodných hodů dvanáctistěnnou kostkou.

# Nejdříve tento seznam vytiskněte na konzoli pomocí funkce print().
# Upravte váš program tak, aby náhodné hody kostkou vypsal do souboru s názvem hody.txt na jeden řádek oddělené čárkou a mezerou.

# (NEDELALI JSME parametry prikazove radky https://kodim.cz/kurzy/python-data/zaklady-programovani/prvni-programy/moduly)
# Upravte váš program tak, aby počet hodů dostal jako parametr na příkazové řádce. Zkuste použitím vašeho programu vyrobit 100, 1000 a 10 000 hodů.

import random

hody = [str(random.randint(1, 6)) for i in range(10)]
print(hody)

hody_zapis = ", ".join(hody)  # musi byt retezce ne cisla

with open("hody.txt", "w", encoding="utf-8") as vystup:
    # for hod in hody:
    #     vystup.write(f'{hod},') # tady je trochu naprd ze i posledni cisl oza sebou bude mit carku

    vystup.write(hody_zapis)
