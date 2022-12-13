# V tomto programu pomocí funkce print() vypište na obrazovku Divadlo Pěst na oko.
print("Divadlo Pěst na oko")

# Program spusťte na konzoli a vyzkoušejte, že dělá co má.


# Upravte tento program tak, že do proměnné nazev uložíte název nějakého divadelního představení a do proměnné cas uložte čas konání tohoto představení.

nazev = "Zkrocení zlé ženy"
cas = "19:30"


# Nyní pomocí funkce print() nechte program vypsat na obrazovku na jeden řádek název představení a čas konání, např. Zkrocení zlé ženy - 19:30.
print(nazev + " - " + cas)
# print(f"{nazev} - {cas}")


# Upravte dále program tak, že do proměnné hodina uložíte hodinu konání představení (jako celé číslo) a do proměnné minuta minutu konání, také jako celé číslo.
hodina = 19
minuta = 30

# Zařiďte, aby výstup programu vypadal takto: Zkrocení zlé ženy - 19:30.
# Pozor na to, že hodina a minuta je hodnota typu číslo, takže ji budete při výpisu muset převést na řetězec pomocí funkce str().

print(nazev + " - " + str(hodina) + ":" + str(minuta))
# print(f"{nazev} - {hodina}:{minuta}")
# print(f"{nazev} - {hodina}:{minuta:02}")
