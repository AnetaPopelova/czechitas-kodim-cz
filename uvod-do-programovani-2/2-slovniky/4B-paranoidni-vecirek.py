# ořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj.

# Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost.

# Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."

hesla = {
    "Jiří": "tajne-heslo",
    "Natálie": "jeste-tajnejsi-heslo",
    "Klára": "nejtajnejsi-heslo",
}

jmeno_hosta = input("Zadej jmeno: ")
vstup = "Nesmíš projít."

if jmeno_hosta in hesla:
    heslo = input("Zadej heslo: ")
    if heslo == hesla[jmeno_hosta]:
        print("Smíš vstoupit.")
    else:
        print("Nesmíš projít.")
else:
    print("Nesmíš projít.")

## Dalsi reseni

# guest_name = input("Zadej jméno: ")
# if guest_name in password_dict:
#   password = input("Zadej heslo: ")
#   if password == password_dict[guest_name]:
#     print("Smíš vstoupit.")
#   else:
#     password = input("Nesprávné heslo. Zadej heslo znovu: ")
#     if password == password_dict[guest_name]:
#       print("Smíš vstoupit.")
#     else:
#       print("Neznáš heslo, vstup zakázán.")
# else:
#   print("Nejsi na seznamu hostů.")
