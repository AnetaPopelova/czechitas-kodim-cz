# Maturita

Uvažuj funkci `ohodnot_studenta()`, která bude pracovat s výsledky z maturitní zkoušky. Vstup funkce bude
slovník s názvy předmětů a známkami studenta, např:

```python
{"Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1}
```

Výstupem funkce bude informace o celkovém výsledku maturity. Možné výstupy jsou následující:
- "Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
- "Neprospěl", pokud má alespoň jednu pětku.
- "Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.

## Rozšířené zadání

Napiš cyklus, který projde seznam `vysledky` a pomocí funkce
`ohodnot_studenta()` zjistí prospěch studenta. Následně pro každého studenta vypíše jeho
jméno a informaci o tom, zda prospěl, neprospěl či prospěl s vyznamenáním.

Zpracuj následující skupinu studentů:

```python
vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]
```

Nezapomeň před odesláním do funkce `ohodnot_studenta()` odebrat ze slovníku jméno studenta.

Výstup tvého programu by mohl vypadat např. takto:

```
Mirek Dušín: Prospěl s vyznamenáním
Jarka Metelka: Neprospěl
Jindra Hojer: Prospěl
Červenáček: Prospěl s vyznamenáním
Rychlonožka: Prospěl
```