# Palgastatistika – palgad.txt
#     Kirjuta Pythoni skript, mis loeb failist palgad.txt töötajate andmed ja arvutab eraldi
#         meeste keskmised töötunnid, töötasu ning palk
#         naiste keskmised töötunnid, töötasu ning palk
#     Tulemused prindi konsooli

mehed_kokku = 0
mehed_tootunnid_kokku = 0
mehed_palk = 0

with open("palgad.txt") as fail:
    rida = fail.readlines()
    for i in rida:
        tykeldus = i.split(",")
        if tykeldus[3] == "Mees":
            mehed_kokku+=1

print(mehed_kokku)

