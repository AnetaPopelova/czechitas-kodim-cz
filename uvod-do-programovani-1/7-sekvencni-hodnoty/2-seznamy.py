# a
# Vytvořte nějaký seznam celých čísel, například počty diváků na několika po sobě jdoucích představeních.
# Použije metodu append a přidejte do seznamu počet diváků na jednom dalším představení.
pocty_divaku = [120, 100, 95, 78, 100]
pocty_divaku.append(113)


# b
# Vytvořte nějaký seznam desetinných čísel, například zaplněnost divadla v několika po sobě jdoucích představeních.
zaplnenost = [0.9, 0.8, 0.7, 0.65, 0.8, 0.85]


# c
# Vytvořte nějaký seznam řetězců, například seznam názvů několika divadelních představení, která divadlo hraje.
# Uložte tento seznam do proměnné hry.
hry = ["Hra A", "Hra B", "Hra C", "Hra D", "Hra E", "Hra F"]

# Uložte do nějaké proměnné druhou položku tohoto seznamu.
druha_hra = hry[1]

# d
# Do proměnné hodnoceni uložte seznam hodnocení, které obdržela divadelní hra “Plyšáci na útěku” v různých recenzních časopisech.
# Hodnocení je vždy dvouprvkový seznam obsahující název recenzního časopisu jako řetězec a samotné hodnocení jako číslo mezi 1 až 10.

hodnoceni = [
    ["Casopis A", 5],
    ["Casopis B", 8],
    ["Casopis C", 7],
]

## BONUS
# Přidejte na konec tohoto seznamu nové hodnocení z časopisu Divadelní oběžník.
hodnoceni.append(["Divadelni obeznik", 7])
hodnoceni = hodnoceni + [["Divadelni obeznik", 7]]

"""
## Více hraní s indexy 

print(hry[2:5])
print(hry[:3])
print(hry[3:])
print(hry[1::3]) # string[start:end:step]
print([hry[i] for i in [0, 5, 1]])
"""
