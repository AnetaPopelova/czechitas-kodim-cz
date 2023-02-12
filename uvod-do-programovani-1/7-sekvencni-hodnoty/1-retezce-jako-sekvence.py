# Uložte si v Python konzoli do proměnné jmeno svoje celé jméno a nechte vypsat jeho třetí, pátý a sedmý znak.

jmeno = "Aneta Popelova"
print(jmeno[2], jmeno[4], jmeno[6])

print([jmeno[i] for i in [2, 4, 6]])  ## bonusova varianta


# # Vyzkoušejte, co se stane, když budete chtít znak na pozici, která překračuje délku řetězce.
print(jmeno[14])

# # Jak zjistím délka svého řetězce?
print(len(jmeno))
