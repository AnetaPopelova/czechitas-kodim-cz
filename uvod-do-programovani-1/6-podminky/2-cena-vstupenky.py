# Program vstupenky01.py, který jste napsali v předchozí fázi, si uložte jako vstupenky02.py, abychom ho mohli dále rozšířit o výpočet ceny vstupenky.

## vstupenky01.py

print("Divadlo Pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")

# Na dalším řádku požádejte uživatele o jeho uživatelské jméno a poté o jeho věk.
# Ten si uložte to nějaké proměnné jako číslo.
uzivatelske_jmeno = input("Zadej uživatelské jméno: ")
vek = int(input("Zadej věk: "))


## vstupenky02.py
plna_cena = 12

# Vytvořte podmínku, která do proměnné cena uloží cenu spočítanou podle věku uživatele dle následujících pravidel

if vek < 6:  # 0 euro pro návštěvníky mladší 6 let
    cena = 0
elif vek <= 26:  # 65% ze základní ceny pro návštěvníky 6 až 26 let (žák, student)
    cena = plna_cena * 0.65
elif vek <= 64:  # 100% ze základní ceny pro návštěvníky 27 až 64 let (dospělý)
    cena = plna_cena
else:  # 50% ze základní ceny pro ostatní (senior)
    cena = plna_cena * 0.5

# Nezapomeňte na zaokrouhlování, ať nám cena vyjde v celých centech.
cena = round(cena, 2)

# Nakonec spočtenou cenu vypište s nějakou hezkou zprávou na výstup.
print("Cena vstupenky je " + str(cena) + ".")
# print(f"Cena vstupenky je {cena}.")
