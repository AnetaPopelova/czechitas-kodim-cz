# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl.
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

total_pages = 0

for book in books:
    total_pages += book["pages"]
print(f"Gustav celkem přečetl {total_pages} stran.")

# nebo lépe
# total_pages = sum(kniha['total_pages'] for book in books)


good_books = 0
for book in books:
    if book["rating"] >= 8:
        good_books += 1
print(f"Gustav ohodnotil {good_books} knihy 8 body.")


# Neco extra

# Ktere knihy to jsou?
# print("Knihy, které hodnocení 8 a více:")
# for book in books:
#   if book["rating"] >= 8:
#     print(book["title"])
