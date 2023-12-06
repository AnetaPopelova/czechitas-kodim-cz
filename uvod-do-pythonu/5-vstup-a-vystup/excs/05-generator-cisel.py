# Napište program generator.py, který si od uživatele vyžádá dvě celá čísla - dolní mez a horní mez - a vypíše na výstup náhodné číslo v zadaných mezích.

import random

dolni_mez = input("Zadej dolní mez: ")
horni_mez = input("Zadej horní mez: ")

cislo = random.randint(int(dolni_mez), int(horni_mez))
print(cislo)
