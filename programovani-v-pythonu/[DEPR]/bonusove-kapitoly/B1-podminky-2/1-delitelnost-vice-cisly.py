# Požádejme uživatele, ať zadá celé číslo.
# Napiš program který zjistí, zda je číslo dělitelné 3 i 4 současně.

# Tip: nezapomeňte si zadané číslo převést na int.
# Tip 2: K ověření dědičnosti použij operátor % - zbytek po celočíselném dělení a zkontroluj, zda je výsledek 0.
# Například 15 % 5 vrací 0, protože 15 je dělitelné 5.

number = int(input("Zadej číslo: "))
if number % 3 == 0 and number % 4 == 0:
    print("Číslo je dělitelné 3 i 4 zároveň.")
else:
    print("Číslo není dělitelné 3 i 4 zároveň.")
