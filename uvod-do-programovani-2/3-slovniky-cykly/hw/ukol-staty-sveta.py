# V kódu níže na stránce vidíš seznam slovníků s informacemi o státech světa. O každém státu tam vidíš následující
# informace:

# * název státu (`name`),
# * hlavní město (`capital`),
# * region (`region`),
# * subregion (`subregion`),
# * populace (`population`),
# * rozloha (`area`),
# * Giniho koeficient (`gini`).

# Vytvoř program, který se uživatele zeptá na region, který ho zajímá. Následně projdi seznam a vypiš všechny státy, které leží v regionu.
# Pokud program žádný stát pro daný region nenajde, vypiš text `"Neznámý region"`.

from seznamstatu import staty  ## ja jsem si seznam ulozila do zvlastniho souboru

list_of_countries = []
my_region = input("Jaký region tě zajímá? ")
# my_region = "Europe"

for country in staty:
    if country["region"] == my_region:
        list_of_countries.append(country["name"])
        # print(country["name"])

if list_of_countries:
    print(list_of_countries)
else:
    print("Neznámý region")

## BONUS
population_dict = {}

for country in staty:
    if country["region"] == my_region:
        subregion = country["subregion"]
        pupulation = country["population"]
        if subregion in population_dict:
            population_dict[subregion] += country["population"]
        else:
            population_dict[subregion] = country["population"]

        # Take muzete vyuzit metody ge a zbavit se tak podminky
        # population_dict[subregion] = population_dict.get(subregion, 0) + country['population']


print(population_dict)
