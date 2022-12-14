# Založte si program `hesla.py` a na jeho začátek vložte následující kód obsahující seznam hesel pro přihlášení do nějakého systému.

hesla = [
    "xyz101",
    "punťa",
    "razor-blade",
    "1234",
    "12011986",
    "martin111",
    "trhnisi",
    "hokuspokus",
    "jeník15",
    "kristus-te-spasi",
    "beruška",
    "strčprstskrzkrk",
]

# Pomocí cyklu vypište všechny hesla na obrazovku, každé na jeden řádek.

for heslo in hesla:
    print(heslo)


# Bezpečná hesla, tedy taková, jež jsou delší než 8 znaků.

for heslo in hesla:
    if len(heslo) > 8:
        print(heslo)

# Neco extra
# Upravte váš program tak, aby vypisoval jen ta hesla, jež obsahují znak pomlčky `-`.

for heslo in hesla:
    if "-" in heslo:
        print(heslo)
