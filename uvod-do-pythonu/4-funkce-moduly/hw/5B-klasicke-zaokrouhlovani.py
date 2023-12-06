# Zkuste vymyslet (za použití funkcí, které už znáte) příkaz, který zaokrouhlí číslo v proměnné cislo na celé číslo klasickým zaokrouhlováním.

import math
import random

cislo = 2.5
zaokrouhlene = math.floor(cislo + 0.5)


# Pokud si chcete svoje řešení otestovat, můžete si obsah proměnné cislo vygenerovat náhodně funkcí random.uniform().
# Ta má stejné vstupy jako funkce random.randint(), generuje ale desetinná čísla.

cislo = random.uniform(0, 10)
zaokrouhlene = math.floor(cislo + 0.5)
