import os
from datetime import date
# Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
print("Tere",os.getlogin())

# Skript kuvab kasutajale praeguse töökataloogi tee
print(os.getcwd())

# Kataloogide loomine:
#     Skript küsib kasutajalt, mitu kataloogi ta soovib luua
#     Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)

mitu = int(input("Mitu kataloogi tahad: "))
today = str(date.today())

try:
    os.mkdir(today)
    for i in range(mitu):
        os.mkdir(today+"/"+str(i+1))
except FileExistsError:
    print(f"Kataloog {today} juba eksisteerib.")

# Kataloogi kustutamine:

# Pärast kataloogide loomist küsib skript kasutajalt, 
# millist äsja loodud või olemasolevat kataloogi soovitakse kustutada, esitades kataloogi nime 1, 2 jne
# Kui sisestatud kataloogi nimi eksisteerib, kustutatakse see

kustuta = int(input(f"Millist kataloogi kustutad 1-{mitu}: "))

if os.path.isdir(f"{today}/{kustuta}"):
    os.rmdir(f"{today}/{kustuta}")
    print(f"Kustutatud kataloog: {today}/{kustuta}")
else:
    print(f"Selline kataloog puudub: {today}/{kustuta}")

# Kuva kuupäeva kasutas olevad kataloogid
kausta_tee = os.getcwd()+"/"+today
print(os.listdir(kausta_tee))






