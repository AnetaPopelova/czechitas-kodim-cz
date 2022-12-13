# V tombole bylo prodáno celkem 1000 lístků.
# Naším úkolem je vylosovat náhodně tři výherce.
# Napište program, který vygeneruje a vypíše tři čísla mezi 1 a 1000.
# Využijte funkci randint, nezapomeňte ale, že si ji musíte importovat z modulu random.
# Neřešte, že jedno číslo může být vygenerováno dvakrát.

import random

stop = 3
for i in range(stop):
    print(random.randint(0, 1000))

# Slo by i pridat cisla do listu a pak vypsat list
vyherci = []
for i in range(3):
    vyherci.append(random.randint(1, 1000))
print(vyherci)
