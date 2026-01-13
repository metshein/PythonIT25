import random
# #Koosta programm, mis genereerib ja kuvab korrutustabeli,
# kus iga number korrutatakse iseendaga:
#9.8
# for i in range(11):
#     print(f"{i} * {i} = {i*i}")
    
#9.9
# tehe = ["+","-","*","/"]
# punktid = 0
# kysimuste_arv = 5
# for _ in range(kysimuste_arv):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
#     
#     if t=="+":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1+arv2 == v:
#             punktid+=1
#     elif t=="-":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1-arv2 == v:
#             punktid+=1
#     elif t=="*":
#         print(f"{arv1}{t}{arv2}=")
#         v = int(input("Vastus: "))
#         if arv1*arv2 == v:
#             punktid+=1
#     else:
#         print(f"{arv1}{t}{arv2}=")
#         v = float(input("Vastus: "))
#         if round(arv1/arv2,1) == v:
#             punktid+=1
#          
# if punktid/kysimuste_arv >= 0.5:
#     print(f"A - {punktid}/{kysimuste_arv}")
# else:
#     print(f"MA - {punktid}/{kysimuste_arv}")

#1
arv = 5
for i in range(1,6):
    print(" " * i + "*" * arv)
    arv-=1

#2
arv = 5
for i in range(1,6):
    print("*" * arv)
    arv-=1
#

#3
arv = 5
for i in range(1,6):
    print(" " * arv + "*" * i)
    arv-=1

#4
for i in range(1,6):
    print("*" * i)

