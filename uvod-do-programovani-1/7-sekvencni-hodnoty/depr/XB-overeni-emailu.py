# Upravte program registrace.py tak, že bude kromě uživatelského jména chtít také e-mailovou adresu.

# Ověřte, že adresa je v platném formátu, tedy že obsahuje zavináč, tečku a má alespoň pět znaků.

uzivatel = input("Zadej uživatelské jméno: ")
email = input("Zadej emailovou adresu: ")

if "@" not in email or "." not in email or len(email) < 5:
    print(
        "Emailova adresa není v platném formátu. Musí obsahovat zavináč, tečku a mít alespoň 5 znaků."
    )
    exit()

# Alternativni reseni
email = input("Zadej email: ")

if "." not in email:
    print("Chybí tečka.")
if "@" not in email:
    print("Chybí zavináč.")
if len(email) < 5:
    print("Email je moc krátký.")

# Alternativni reseni
email = input("Zadej email: ")

if len(email) > 5:
    if "." in email:
        if "@" in email:
            print("Email je ok.")
        else:
            print("Chybí zavináč.")
    else:
        print("Chybí tečka.")
else:
    print("Email je moc krátký.")
