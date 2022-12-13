import pymongo

uzivatelskeJmeno = "anetapopelovaczechitas"
heslo = "bpRvEgMb"
adresaServeru = "czechitas.westus2.cloudapp.azure.com"
klient = pymongo.MongoClient(
    f"mongodb://anetapopelovaczechitas:bpRvEgMb@20.38.9.79:27017/anetapopelovaczechitas"
)
databaze = klient["anetapopelovaczechitas"]


# Toto slouží pro test
kolekce = databaze["nakupy"]
nakup = kolekce.find_one()
print(nakup)
