# Mějme seznam hodnocení divadelní hry Plyšáci na útěku , který vypadá takto:

hodnoceni = [7, 9, 6, 7, 9, 8]

# Vytvořte program, který projde tento seznam a vypíše každé hodnocení na nový řádek.

for prvek in hodnoceni:
    print(prvek)


# Upravte program tak, aby vypisoval
# výstup v tomto formátu:

#     7/10
#     9/10
#     6/10
#     7/10
#     9/10
#     8/10

hodnoceni = [7, 9, 6, 7, 9, 8]
for prvek in hodnoceni:
    print(f"{prvek}/10")
    # print(str(prvek) + "/10")
