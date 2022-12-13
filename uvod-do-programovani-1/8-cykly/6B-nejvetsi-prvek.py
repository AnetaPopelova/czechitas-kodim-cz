# Napište cyklus, který projde zadaný seznam celých čísel a najde v něm největší hodnotu.

cisla = [10.5, 13.3, 17.2, 11.5]
nejvetsi = cisla[0]

for cislo in cisla:
    if cislo > nejvetsi:
        nejvetsi = cislo
print(nejvetsi)


## Neco extra
list_numbers = [0, 50, 21.3, 54.9, 62.1, 10, 13, 14, 62.2]
print(max(list_numbers))
