# Karolína bude mít za půl roku svatbu a právě obdržela od agentury ceník služeb. Cena za kompletní menu pro dospělou osobu je 990 kč, pro dítě je to 50% ceny dospělého.

# Uložte cenu za dospělou osobu do proměnné cena_dospely.
# Pomocí proměnné cena_dospely vypočítejte cenu za dítě, tu uložte do proměnné cena_dite.
# Vypočítejte celkové náklady na jídlo pro 60 dospělých a 8 dětí. Pro výpočet použijte předchozí proměnné.
# V ceníku byla chyba, cena za dospělého je ve skutečnosti 1000 kč. Upravte na základě této informace všechny proměnné.

cena_dospely = 990  # 1000
cena_dite = cena_dospely / 2

celkova_cena = cena_dospely * 60 + cena_dite * 8
print(celkova_cena)
