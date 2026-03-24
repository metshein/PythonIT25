import datetime
# # Lihtne kuupäev
# #     Kuva praegune päev, kuu, aasta, tund, minut
# kp = datetime.datetime.now()
# print(kp)
# #     Vorminda praegune kuupäev järgmiselt: d.m Y,  H:M:S
# print(kp.strftime('%d.%m %Y,  %H:%M:%S'))

# #     Lisa oma sünniaeg, arvuta ja kuva, mitu päeva vana oled
# sp = datetime.datetime(1980,11,6)
# vanus_paevades = kp - sp
# print(f"Vanus päevades: {vanus_paevades.days}")
# #     Kuva vanus aastates
# vanus_aastates = vanus_paevades.days // 365
# print(f"Vanus aastates: {vanus_aastates}")
# #     Kuva, kas tegemist on juubeliaastaga
# if vanus_aastates%5 == 0:
#     print("Sul on juubel")
# else:
#     print("Sul pole juubel!")

import csv
# Autorent
#     Kasuta seda faili: rentals.csv
autode_arv = 0
kliendid = []
faili_nimi = 'rentals.csv'
open
    reader
    skipi_esimene
    kuva testimiseks read, kommi välja
        suureanda autode arvu
        kui id pole, siis 
            lisan 8 tulba klientidesse


#     Rendite arv – leia mitu renditehingut on tehtud
print(f"Rendide arv kokku: {autode_arv}")
#     Unikaalsed kliendid ja keskmine vanus – arvutage, mitu unikaalset klienti (customer ID) andmetes esineb ja mis on teie klientide keskmine vanus
# print(kliendid) 951
print(f"Unikaalseid kliente: {len(kliendid)}")

#     Tagastamine – milline osakaal broneeringutest hõlmab risti-kontori rentimist, kus klient võtab auto ühest kohast ja tagastab selle teise kontorisse?
#     Keskmine rentimise kestus – mis on keskmine rentimise kestus?

