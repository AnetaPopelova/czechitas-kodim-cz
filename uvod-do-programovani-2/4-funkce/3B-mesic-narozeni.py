# Napiš funkce `month_of_birth`, která bude mít jeden parametr - rodné číslo.
# Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

# _Příklad:_
# _Pro hodnotu 9207054439 vrátí 7._
# _Pro hodnotu 9555125899 vrátí 5._


def month_of_birth(birth_number):
    month = int(str(birth_number)[2:4])
    # month = month % 50
    if month > 50:  # nebo month > 12
        month = month - 50
    return month


print(f"9207054439 -> {month_of_birth(9207054439)}")
print(f"9555125899 -> {month_of_birth(9555125899)}")
