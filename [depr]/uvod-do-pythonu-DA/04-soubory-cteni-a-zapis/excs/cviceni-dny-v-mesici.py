# 3 Dny v měsíci (zavařovačka)
# Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.
# Upravte váš program tak, aby zároveň s počtem dnů vypisoval i název měsíce. Oddělte v souboru název měsíce a počet dnů pomocí tabulátoru.
# Upravte váš program tak, aby jako první řádek výsledného souboru obsahoval nadpisy pro jednotlivé sloupce, tedy měsíc a počet dní.

with open("kalendar.txt", "w", encoding="utf-8") as vystup:
    for dny in pocty_dni:
        vystup.write(f"{dny}\n")

# Mohly byste si klidne udelat i slovnik misto listu
# mesice = [
#     "Jan",
#     "Feb",
#     "Mar",
#     "Apr",
#     "May",
#     "Jun",
#     "Jul",
#     "Aug",
#     "Sep",
#     "Oct",
#     "Nov",
#     "Dec",
# ]

# with open("kalendar.txt", "w", encoding="utf-8") as vystup:
#     vystup.write("Month\tDays\n")  # nadpisy sloupcu
#     for i in range(len(mesice)):
#         vystup.write(f"{mesice[i]}\t{pocty_dni[i]}\n")
