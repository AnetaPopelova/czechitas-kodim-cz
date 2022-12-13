# 2 Počet slov (zapni hlavu)
# Stáhněte si odevzdanou slohovou práci.
# Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě.
# Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno.

# Nechte se vést následujícím návodem.

# Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu.
# Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem.
# Vypište na výstup seznam hodnot udávající počty slov na každém řádku.
# Vypište na výstup celkový počet všech slov v souboru.

with open("data/praha.txt", encoding="utf-8") as soubor:
    radky = soubor.readlines()

print(radky)
radky_slov = [radek.split() for radek in radky]
print(radky_slov)
radky_pocet_slov = [len(radek.split()) for radek in radky]
print(radky_pocet_slov)

print(sum(radky_pocet_slov))
