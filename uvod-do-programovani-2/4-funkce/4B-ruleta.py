# Napiš funkci, která bude jednoduchou simulací rulety.
# Budeme uvažovat pouze možnost sázení na řady.
# Uživatel si může vybrat jednu ze tří řad:

# - první řada (hodnoty 1, 4, 7 atd.),
# - druhá řada (hodnoty 2, 5, 8 atd.),
# - třetí řada (hodnoty 3, 6, 9 atd.).


# Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.
# Vytvoř funkci `roulette`, která bude mít parametry číslo řady a výši sázky.
# Pomocí funkce `randint` z modulu `random` vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.
# Vyhodnoť, do které řady číslo náleží.
# Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.
# Funkce `roulette` vrací hodnotu výhry.
# Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá.

import random

row = int(input("Na kterou řadu sázíš? (1-3): "))
bet = int(input("Kolik sázíš?: "))


def ruleta(row, bet):
    rows = [
        range(1, 37, 3),  # 1, 4, 7, ...
        range(2, 37, 3),  # 2, 5, 8, ...
        range(3, 37, 3),  # 3, 6, 9, ...
    ]
    number = random.randint(0, 36)
    print(f"{number = }")
    return 2 * bet if number in rows[row - 1] else 0  # "- 1" kvůli indexování od nuly


# Nebo
def roulette(row, bet):
    number = random.randint(0, 36)
    # kontrolní výpis
    print(f"Padlo číslo {number}.")
    if number == 0:
        return -bet
    if number % 3 == 1 and row == 1:
        return bet * 2
    if number % 3 == 2 and row == 2:
        return bet * 2
    if number % 3 == 0 and row == 3:
        return bet * 2
    return -bet


win = roulette(int(row), float(bet))
print(win)

# alternativní řešení
# def roulette(row, bet):
#   number = random.randint(0, 36)
#   print(f"Padlo číslo {number}.")
#   if number == 0:
#     return - bet
#   rowModified = row % 3
#   if number % 3 == rowModified:
#     return bet * 2
#   return - bet
