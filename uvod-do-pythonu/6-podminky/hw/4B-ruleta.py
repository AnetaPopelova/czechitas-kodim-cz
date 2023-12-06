# Na obrázku vidíte rozložení čísel na klasické Francouzské ruletě.

# Ruleta obsahuje čísla 0 - 36.

# Každé číslo s výjimkou nuly je buď sudé nebo liché a zároveň červené nebo černé.

# Pro čísla 1 až 10 a 19 až 28 platí, že lichá čísla jsou červená a sudá jsou černá.

# Pro zbytek platí obrácené pravidlo, tedy lichá jsou černá a sudá červená.

# Nula není ani lichá ani sudá, ani černá ani červená.


cislo = int(input("Zadej čislo: "))

if cislo == 0:
    print("Číslo je 0.")
    exit()

je_sude = cislo % 2 == 0
sude_liche_text = "sudé" if je_sude else "liché"

if 1 <= cislo <= 10 or 19 <= cislo <= 28:
    barva = "černé" if je_sude else "červené"
else:
    barva = "červené" if je_sude else "černé"

print(f"Číslo je {sude_liche_text} a {barva}.")


## Nebo jinak:
cislo = input("Zadej čislo: ")
cislo = int(cislo)

if cislo == 0:
    print("Číslo je 0.")
else:
    if cislo % 2 == 0:
        print("Číslo je sudé.")
    else:
        print("Číslo je liché.")
    if cislo <= 10 or (cislo >= 19 and cislo <= 28):
        if cislo % 2 == 0:
            print("Číslo je černé.")
        else:
            print("Číslo je červené.")
    else:
        if cislo % 2 == 1:
            print("Číslo je černé.")
        else:
            print("Číslo je červené.")
