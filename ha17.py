import os
# Pangakonto – pangakonto.txt
#     Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. 
#   Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. 
# Skript peab arvutama ja väljastama:
#         kogu tehingute arvu
#         positiivsete tehingute arvu
#         positiivsete tehingute kogusumma
#     Tulemused tuleb väljastada konsooli

tehingute_arv = 0
pos_tehingute_arv = 0
pos_tehingute_summa = 0

with open("pangakonto.txt") as fail:
    for rida in fail:
        tehingute_arv+=1
        if float(rida.strip()) > 0:
            pos_tehingute_arv+=1
            pos_tehingute_summa+=float(rida.strip())
            print(rida.strip())

print(f"Tehingute arv: {tehingute_arv}")
print(f"Pos. tehingute arv: {pos_tehingute_arv}")
print(f"Pos. tehngute summa: {pos_tehingute_summa:.2f}")
