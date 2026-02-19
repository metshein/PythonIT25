# Kirjutage Pythoni skript, mis tervitab kasutajat, kuvab praeguse töökataloogi, loob uusi katalooge vastavalt kasutaja soovile ning küsib, millist kataloogi soovitakse kustutada.
#     Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
print(f"Hello {os.user}")




#     Skript kuvab kasutajale praeguse töökataloogi tee
#     Kataloogide loomine:

#         Skript küsib kasutajalt, mitu kataloogi ta soovib luua
#         Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)
#     Kataloogi kustutamine:
#         Pärast kataloogide loomist küsib skript kasutajalt, millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
#         Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see
#     Kuva kuupäeva kasutas olevad kataloogid


