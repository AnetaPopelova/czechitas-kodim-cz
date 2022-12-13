# 1 Výplata přesněji (to dáš)
# Zatím jsme výplatu počítali za předpokladu,
# že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické.
# Vytvořte proto textový soubor vykaz.txt, který bude obsahovat 12 řádků a na
# každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz.
# Vytiskněte tento seznam na konzoli funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu.
# Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

with open("vykaz.txt", encoding="utf-8") as soubor:
    hodiny = soubor.readlines()


hodina_mzda = int(input("Zadej hodinovou mzdu: "))

platy = [int(mesic) * hodina_mzda for mesic in hodiny]

# platy = []
# for mesic in hodiny:
#     platy.append(int(mesic) * hodina_mzda)

vydelek_rok = sum(platy)
prumerny_mesicni_plat = vydelek_rok / 12

print(vydelek_rok)
print(prumerny_mesicni_plat)
