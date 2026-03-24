import json
import requests

yl = "arved"
url = f"https://metshein.com/kordamine/json/{yl}.json"
response = requests.get(url)
# print(response)

makstud_arved = 0
maksmata_arved = 0


if response.status_code == 200:
    data = response.json()
    for arve in data['arved']:
        # print(arve['makstud'])
        if arve['makstud']:
            makstud_arved+=1
        else:
            maksmata_arved+=1

else:
    print(response.status_code) 

print(maksmata_arved)
print(makstud_arved)


# kategooriad = []
# koige_odavam = 10000000
# koide_odavam_toode = ""
# koige_kallim = 0
# koide_kallim_toode = ""

# if response.status_code == 200:
#     data = response.json()
#     # print(data['tooted'][0]['nimi'])
#     for toode in data['tooted']:
#         if toode['hind'] < koige_odavam:
#             koige_odavam = toode['hind']
#             koide_odavam_toode = toode['nimi']
#         if toode['hind'] > koige_kallim:
#             koige_kallim = toode['hind']
#         if toode['kategooria'] not in kategooriad:
#             kategooriad.append(toode['kategooria'])
# else:
#     print(response.status_code)

# print(len(kategooriad))





# ametid = {} 


# if response.status_code == 200:
#     data = response.json()
#     for i in data[yl]:
#         if i['amet'] not in ametid:
#             ametid[i['amet']] = 1
#         else:
#             ametid[i['amet']] += 1
# else:
#     print(response.status_code) 

# max_value = max(ametid.values())
# max_projects = [key for key, value in ametid.items() if value == max_value]
# print(f"Projects with max performance: {max_projects}")
