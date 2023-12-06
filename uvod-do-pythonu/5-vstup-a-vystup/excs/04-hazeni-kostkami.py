# Napište program kostky.py, který bude simulovat hod dvěma klasickými šestistěnnými kostkami.
# Jeho výstupu bude součet bodů na těchto dvou kostkách.

# Generování náhodných čísel dělá funkce random.randint().
# Pokud chcete ve vašem programu použít modul random, musíte na jeho úplném začátku napsat příkaz import random

import random

cislo = random.randint(1, 6) + random.randint(1, 6)
print(cislo)
