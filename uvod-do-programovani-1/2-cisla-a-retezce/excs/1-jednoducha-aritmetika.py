# Jeden lístek do divadla “Pěst na oko” stojí 12 euro.

# 1 a
# Spočítejte měsíční příjem divadla ze vstupného přichází-li průměrně 174 návštěvníků na jedno představení a divadlo hraje 15 představení měsíčně.

print(12 * 174 * 15)

# 1 b
# Divadlo se rozhodlo prodávat studentské vstupné ve výši 65% plného vstupného.
# Jak se změní měsíční příjem divadla pokud víme, že polovina návštěvníků jsou studenti?

# Takže měsíční příjem divadla ze studentského vstupného je 19215.6 euro.
print(87 * 7.8 * 15)

## Nebo celkem:
print(12 * 174 / 2 * 15 + 12 * 174 / 2 * 15 * 0.65)

## S použitím závorek
print(12 * 15 * 174 / 2 * (1 + 0.65))

## Nebo
print(((12 * 174 / 2) + (12 * 0.65 * 174 / 2)) * 15)
