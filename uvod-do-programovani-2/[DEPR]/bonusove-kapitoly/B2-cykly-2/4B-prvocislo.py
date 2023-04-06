# Požádej uživatele o zadání celého čísla. Následně urči, zda je toto číslo prvočíslo.
# Prvočíslo je číslo, které je dělitelné beze zbytku pouze 2 čísly - 1 a sebou samotným.
# Například 5 je prvočíslo, protože je dělitelná pouze 1 a 5.
# Naoapk 4 není prvočíslo, protože je dělitelná 1, 2 a 4.

num = int(input("Zadej cislo: "))
je_prvocislo = True

if num > 1:
    # kontrola nasobku (delitelnosti cisel ktere jsou mensi nez cislo samotne ale vetsi nez 1)
    for i in range(2, num):
        # Pokud je delitelne nejakym cislem z rozsahu
        if (num % i) == 0:
            je_prvocislo = False
            # nemusime zkouset dal, uz vime ze neni prvocislo
            break

if je_prvocislo:
    print("Je prvocislo")
else:
    print("Neni prvocislo")
