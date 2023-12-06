# Takzvané Shannonovo číslo má hodnotu 10  na 123 a udává kolik nejméně lze odehrát různých šachových partií.
# Vytvořte řetězec, který obsahuje toto číslo zapsané běžným způsobem pomocí cifer.
# Například 103 je 1000, 106 je 1000000 atd.

print("1" + "0" * 123)


# Čísla s mnoha nulami je v Česku zvykem zapisovat tak, že každé tři nuly následuje mezera.
# Jeden milión se tedy zapíše jako 1 000 000.
# Vytvořte řetězec, který obsahuje Shannonovo číslo z předchozího cvičení zapsané v tomto formátu.

print("1 " + "000 " * (123 // 3))
