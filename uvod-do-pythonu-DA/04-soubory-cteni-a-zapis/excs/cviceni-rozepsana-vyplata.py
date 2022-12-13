# 1 Rozepsaná výplata (to dáš)
# Modifikujte program pro počítání výplaty z předchozí sekce tak,
# aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

# Nejprve tyto informace vypište na výstup pomocí funkce print().
# Poté program upravte tak, aby vypsal tyto výsledky do souboru.

with open("data/vykaz.txt", "r", encoding="utf-8") as vstup:
    radky = [int(radek) for radek in vstup.readlines()]

hodinova_mzda = 250
platy = [hodinova_mzda * mesic for mesic in radky]

# for mesic in radky:
#     print(mesic * hodinova_mzda)

print(platy)
platy_k_zapisu = [str(plat) + "\n" for plat in platy]

with open("data/mesicni_platy.txt", "w", encoding="utf-8") as vystup:
    # for plat in platy:
    #     vystup.write(f'{plat}\n')
    # vystup.write(str(plat) + '\n')
    vystup.writelines(platy_k_zapisu)
