import json 

# Kuva mitu õpilast õpib 10, 11 ja 12 klassis
# Kuva millistes trennides 12. klassi õpilased käivad
# Kuva 12 klassi õpilaste hinneteleht (nimi, ained, punktid)

with open('haridustulemused.json', 'r', encoding='utf-8') as file:
    tulemused = json.load(file)

klass12 = 0
klass11 = 0
klass10 = 0
tegevused = []

for tulem in tulemused:
    # print(tulem['klass'])
    if tulem['klass'] == "12":
        print(tulem['nimi'])
        klass12 +=1
        for tegevus in (tulem['tegevused']):
            if tegevus not in tegevused:
                tegevused.append(tegevus)
    elif tulem['klass'] == "11":
        klass11 += 1
    else:
        klass10 += 1

print(f"12. klassis {klass12} õpilast")
print(f"11. klassis {klass11} õpilast")
print(f"10. klassis {klass10} õpilast")
for t in tegevused:
      print(t, end=", ")               