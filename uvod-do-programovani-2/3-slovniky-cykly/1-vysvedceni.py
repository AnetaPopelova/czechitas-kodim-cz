# Uvažujme vysvědčení, které máme zapsané jako slovník.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělešná výchova": 3,
    "Chemie": 4,
}


# Napiš program, který spočte průměrnou známku ze všech předmětů.

prumerna_znamka = sum(school_report.values()) / len(school_report)
print(f"Průměrná známka je: {prumerna_znamka}")

suma_znamek = 0
for znamka in school_report.values():
    suma_znamek += znamka

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
# print("Předměty s jedničkou:")
# for predmet, znamka in school_report.items():
#     if znamka == 1:
#         print("\t" + predmet)
