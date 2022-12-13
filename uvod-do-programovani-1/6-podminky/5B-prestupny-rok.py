# Napište program, který po zadání kalendářního roku vypíše, zda jde o rok přestupný, či nikoliv.
# Letopočet je přestupný,pokud je dělitelný čtyřmi.
# Roky, které jsou dělitelné 100 jsou ovšem přestupné pouze tehdy, jsou-li zároveň dělitelné 400.

rok = int(input("Zadej rok: "))

delitelne_4 = rok % 4 == 0
delitelne_100 = rok % 100 == 0
delitelne_400 = rok % 400 == 0

if delitelne_400 or (delitelne_4 and not delitelne_100):
    print("Rok je přestupný.")
else:
    print("Rok není přestupný")

# Alternativni reseni
if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
    print("Rok je přestupný.")
else:
    print("Rok není přestupný")


# Nebo treba takhle:
rok = input("Zadej rok: ")
rok = int(rok)
if rok % 4 == 0:
    if rok % 100 == 0:
        if rok % 400 == 0:
            print("Rok je přestupný.")
        else:
            print("Rok není přestupný")
    else:
        print("Rok je přestupný.")
else:
    print("Rok není přestupný.")
