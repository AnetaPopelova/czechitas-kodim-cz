# Založte si program prihlaseni.py.

# V tomto nechte uživatele zadat svoje uživatelské jméno a poté heslo.

uzivatel = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")

# Pokud se heslo shoduje s heslem simsalabim vypište na výstup "Smíš vstoupit"
if heslo != "simsalabim":
    print("Vstup nepovolen!")
    # Pokud uživatel zadá heslo špatně, už se ho na věk neptejte a ukončete program voláním funkce exit().
    exit()

# Upravte dále program tak, že pokud uživatel zadá správné heslo, program se ho ještě zeptá na věk.
# Pustí jej dál pouze pokud je starší 18ti let.
vek = int(input("Zadej věk: "))
if vek >= 18:
    print("Smíš vstoupit.")
else:
    print("Vstup nepovolen!")
