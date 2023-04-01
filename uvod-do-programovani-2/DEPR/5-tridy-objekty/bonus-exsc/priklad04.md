# Výplata

Uvažujme nyní opět třídu `Employee`, kterou jsme si ukázali v lekci. Pro zjednodušení nyní nebudeme pracovat s dovolenou, proto nám stačí třída, která je v ukázce níže.

```python
class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position
```

Nyní se budeme zabývat platem. Přidej třídě atribut `salary` (výše hrubého platu) a `children` (počet dětí), jejichž výši nastavíš v metodě `__init__()`. Dále přidej metodu `get_net_salary()`, která vypočte a vrátí výši čisté mzdy. Uvažuj zjednodušený výpočet: sazba daně je 15 % a sleva na jedno dítě 1500 Kč. Vzorec pro výpočet daně tedy je: daň = hrubá mzda * 0.15 - počet dětí * 1500. Metoda vrátí výši čisté mzdy, tj. čistá mzda = hrubá mzda - daň. Daň může vyjít i záporná.

## Pokročilé zadání

Pokud máš zájem, můžeš zkusit pokročilejší verzi. Rozlož výpočet do dvou metod. Přidej metodu `get_tax()`, která vypočte výši daně, a poté metodu `get_net_salary()`. Výpočet daně bude ve metodu `get_tax()`. Metoda `get_net_salary()` zavolá metodu `get_tax()`, aby zjistila výši daně, a poté vrátí čistou mzdu. Volání metody proveď pomocí klíčového slova, tj. např.:

```python
net_salary = self.salary - self.get_tax()
```
