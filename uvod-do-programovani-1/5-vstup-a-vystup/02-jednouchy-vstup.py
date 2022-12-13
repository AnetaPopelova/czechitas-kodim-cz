# Napište program jmeno.py, který získá jméno a příjmení od uživatele voláním funkce input().

jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej příjmení: ")

# Vypište je na obrazovku podobně jako v předchozím cvičení.

print(jmeno + " " + prijmeni)

# Nechte uživatele zadat také věk.

vek = input("Zadej věk: ")

# Pozor na to, že funkce input() vždy vrací řetězec, ale my chceme v proměnné vek mít číslo.
# Použijte tedy funkci int(), abyste převedli uživatelem zadaný řetězec na číslo.

vek = int(vek)

# Opět vypište na obrazovku jméno, příjmení a věk tak jako v předchozí verzi.

print(jmeno + " " + prijmeni + ", věk: " + str(vek))
# print(f"{jmeno} {prijmeni}, věk: {vek}")
