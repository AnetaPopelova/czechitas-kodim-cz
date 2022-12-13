# Ověřování hesla se někdy dělá tak, že se vás systém ptá pouze na některé jeho znaky.
# Napište program, který má uloženo heslo, které musí uživatel zadat.
# Pak se jej postupně zeptejte například na druhý, pátý a sedmý znak hesla.
# Propusťte uživatele pouze tehdy, zadá-li všechny tyto znaky správně.

heslo = "superTajneHeslo123."

znak = input("Zadej 2. znak hesla: ")
if znak != heslo[1]:
    print("Chyba ověření.")
    exit()
znak = input("Zadej 5. znak hesla: ")
if znak != heslo[4]:
    print("Chyba ověření.")
    exit()
znak = input("Zadej 7. znak hesla: ")
if znak != heslo[6]:
    print("Chyba ověření.")
    exit()
print("Ověření bylo úspěšné!")
