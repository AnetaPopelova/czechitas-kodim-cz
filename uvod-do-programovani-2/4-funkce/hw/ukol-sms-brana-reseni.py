"""
# ukol-03: SMS brána

Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

- Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
- Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
  
Tvůj program bude obsahovat dvě funkce:
- První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být
devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, 
zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pokud je číslo platné, funkce vrátí hodnotu `True`, jinak vrátí hodnotu `False`.
- Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné,
vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou
vypíše uživateli.

## Nápověda
Pokud chcete zkontrolovat předvolbu, stačí využít podmínku`+420 in cislo`, alternativně můžete využít
indexy: Python umožňuje kromě jednoho znaku z řetězce získat i více znaků, a to
pomocí dvojtečky. Pokud budete chtít získat první čtyři znaky, napište `cislo[0:4]`. Pak můžete vytvořit podmínku
`cislo[0:4] == "+420"`.

---

## Bonus:
Zkus svoji první funkci vytunit tak, že si bude umět poradit s mezerami
v telefonním čísle. Mezer se zbavíš tak, že použiješ `replace()` a tečkovou notaci.
První parametr je znak, který chceš nahradit, a druhý parametr nový znak. Níže je příklad
použití.

```python
tel_cislo = "+420 734 123 456"
tel_cislo = tel_cislo.replace(" ", "")
```
"""


## TEST VALUES
phone_number_input = "+420 123 456 789"

message_text_input = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


import math


def check_phone_number(phone_number):
    phone_number = phone_number.replace(" ", "")  # BONUS
    is_valid = False
    if len(phone_number) == 13:
        if phone_number[0:4] == "+420":
            is_valid = True
    elif len(phone_number) == 9:
        is_valid = True
    return is_valid


def get_message_price(message):
    price_per_unit = 3
    max_characters_per_unit = 180
    count_units = len(message) / max_characters_per_unit
    total_price = math.ceil(count_units) * price_per_unit
    return total_price


# phone_number_input = input("Phone number: ")
if check_phone_number(phone_number_input):
    # message_text_input = input("Your message: ")
    message_price = get_message_price(message_text_input)
    print(f"Message price is {message_price} CZK.")
else:
    print(f"Phone number is invalid.")


# Dalsi mozne reseni
# import math

# def overeni_cisla(cislo):
#     cislo = cislo.replace(' ','')
#     delka = len(cislo)
#     return delka == 9 or (delka == 13 and cislo[:4] == '+420')

# def cena_zpravy(zprava):
#     return math.ceil(len(zprava) / 180) * 3

# tel_cislo = input('Prosim zadej telefonni cislo: ')

# if overeni_cisla(tel_cislo):
#     zprava = input('Zadej text zpravy: ')
#     print(f'Cena zpravy: {cena_zpravy(zprava)}')
# else:
#     print('Telefonni cislo neplatne')
