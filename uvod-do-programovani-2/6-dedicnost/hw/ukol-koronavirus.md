## Dedicnost

Prohledni si nasledujici tridu:

```py
class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti
```

Vytvor tridu `Koronavirus` kera dedi ze tridy `Nemoc` a to nasledujicim zpusobem:

Ze tridy `Nemoc` dedi beze zmeny chovani:
 *  Atribut `jmeno`
 *  Metodu `zmen_pocet_obeti`

Navic pridava jeste:
* atribut `varianty`
  * prazdny list v `__init__` metode tridy `Koronavirus`
* metodu `pridej_variantu(self, varianta)`
  * do atributu `varianty` prida novou variantu - varianty muzete specifikovat pomoci retezcu, pripadne i klidne vlastni tridou

Upravuje metodu tridy `Nemoc`:
* `__str__` uprav tak aby zobrazovala obsah atributu `jmeno` a `varianty`
  * v retezci budou varianty oddelene carkami tedy napriklad z listu `['omikron', 'delta']` se stane retezec `'omikron, delta'` - pouzijte metodu `join` podle nasledujicicho prikladu:
```py
seznam = ['a', 'b', 'c']
' ,'.join(seznam)
print(seznam) # 'a, b, c'
```

Hodnoty atributu `inkubacni_doba`, `pocet_obeti` a `sireni` budou v `__init__` metode tridy `Koronavirus` predane `__init__` metode materske tridy (pres `super().__init__(...)`).

![koala inheritance meme](https://pbs.twimg.com/media/EY0QN-KWAAEy1O0?format=jpg&name=small)

---

### Priklad pouziti:

```py
omikron = Koronavirus('Coronavirus', ['omikron'])
print(omikron) # 'Jmeno: Coronavirus (varianty: omikron)'

corona = Koronavirus('Coronavirus')
corona = Koronavirus('Coronavirus', []) # melo by fungovat stejne jako predchozi radek
print(corona) # 'Jmeno: Coronavirus (zadne nalezene varianty)'
print(corona.pocet_obeti) # nejake cislo ktere se da menit pomoci metody zmen_pocet_obeti() - muze byt nacatku nula nebo cislo ktere si zvolite pri vytvoreni objektu
print(corona.sireni) # 'vzduchem' -- muzete reprezentovat i cislem
print(corona.inkubacni_doba) # 12 -- je mi jedno jake cislo - pevne dane ve volani super().__init__(...)
corona.pridej_variantu('omikron')
corona.pridej_variantu('delta')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta)'
corona.pridej_variantu('alpha')
print(corona) # 'Jmeno: Coronavirus (varianty: omikron, delta, alpha)'
```