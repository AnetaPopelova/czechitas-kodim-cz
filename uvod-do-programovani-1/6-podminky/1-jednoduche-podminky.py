# Založte si program prihlaseni.py.

# V tomto nechte uživatele zadat svoje uživatelské jméno a poté heslo.
uzivatelske_jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")

# Pokud se heslo shoduje s heslem simsalabim vypište na výstup "Smíš vstoupit"
if heslo == "simsalabim":
    vek = input("Zadej věk: ")
    vek = int(vek)
    # # Upravte dále program tak, že pokud uživatel zadá správné heslo, program se ho ještě zeptá na věk a pustí jej dál pouze pokud je starší 18ti let.
    if vek > 18:
        print("Smíš vstoupit.")

# Upravte tento program tak, aby vypsal "Vstup nepovolen" pokud uživatel zadá špatné heslo.
else:
    print("Vstup nepovolen!")
    # Pokud uživatel zadá heslo špatně, už se ho na věk neptejte a ukončete program voláním funkce exit().
    exit()


## Nebo poskladane jinak...
uzivatel = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")

if heslo != "simsalabim":
    print("Vstup nepovolen!")
    exit()

vek = int(input("Zadej věk: "))
if vek >= 18:
    print("Smíš vstoupit.")
else:
    print("Vstup nepovolen!")
