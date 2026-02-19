# Ülesanne 12

#     Loo funktsioon, mis võimaldab kasutajal teisendada temperatuuri Celsiusest Fahrenheitiks ja vastupidi.
#     Funktsioon võtab kaks argumenti: temperatuuri väärtuse ja teisendamise suuna, kus ‘C’ tähendab Celsiusest Fahrenheitiks teisendamist ja ‘F’ vastupidi.
#     Vaikimisi on teisendamise suund Celsiusest Fahrenheitiks.
#     Funktsiooni peab kaasnema selge dokumentatsioon, mis kirjeldab selle ülesannet, parameetreid ja mida tagastab.
#     Implementeeri loogika temperatuuri teisendamiseks kasutades vastavaid valemeid:
#         Celsiusest Fahrenheitiks: C ×59​+32
#         Fahrenheitidest Celsiuseks: (F−32)×59

def temp(t,v):
    """
    Teisendab C->F või F->C.

    Parameetrid:
    t (int): Kraadid.
    v (string): Vali teisendus F või C.

    Tagastab:
    string: teisenduse või veateate.

    Näide:
    >>> temp(20,"C")
    -6.66
    """
    if v=="F":
        vastus = t * 9/5 + 32 
    elif v=="C":
        vastus = (t - 32) / (9/5) 
    else:
        vastus = "Vale sisestus!"
    return vastus

print(temp(20,"C"))
print(temp(20,"F"))
print(temp(20,"sdfsdfsf"))
print(temp.__doc__)

#     Loo lambda funktsioon nimega, mis arvutab vajaliku kütuse koguse teatud vahemaa läbimiseks, kasutades sõiduki kütusekulu normi (liitrit 100 km kohta).
#     Funktsioon võtab kaks argumenti: kütusekulu norm (kytusekulu) ja läbitava vahemaa (vahemaa).
#     Tagastab kütuse koguse liitrites, arvutatuna valemiga (kytusekulu / 100) * vahemaa.
#     Näiteks, kui sõiduki kütusekulu norm on 5 liitrit 100 kilomeetri kohta ja soovite läbida 150 kilomeetrit, kasutage funktsiooni kytusekulu(5, 150), mis tagastab vajaliku kütusekoguse liitrites.

#10L/100 ja 200km (200/100*10)
kytus = lambda kytusekulu, vahemaa: (vahemaa/100) * kytusekulu 
print(kytus(5, 150))


#     Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt.
#     Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone: deposiit (raha lisamine) ja väljavõte (raha eemaldamine). Tagastage peale igat toimingut konto jääk.
#     Funktsiooni parameetrid:

#         algne_saldo: Algse saldo väärtus.
#         toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote').
#         summa: Summa, mida soovitakse lisada või eemaldada.

#     Näide: Alustades algse saldoga 100, deposiidi toiminguga 50, peaks funktsioon konto_haldur tagastama uue saldo 150. Väljavõtte toiminguga 20 uus saldo oleks siis 130.
#     Kirjutage selge dokumentatsioon, mis kirjeldab, kuidas algset saldot seada, kuidas toiminguid teostada ja millist tüüpi väärtusi tagastatakse.

konto = 500

def depo(raha, konto):
    '''
        siin suurepärane dokumentatsioon
    '''
    summa = konto+raha
    return summa

def valja(raha, konto):
    '''
        siin suurepärane dokumentatsioon
    '''
    summa = konto - raha
    return summa

konto = depo(10, konto)
konto = depo(100, konto)
konto = valja(500, konto)
konto = valja(500, konto)
konto = depo(1, konto)
konto = depo(17, konto)

print(depo.__doc__)

print("Kontoseis: ", konto)