import random
user = input ("masukan pilihan [gunting, batu, kertas] : ")

pilihan = ["gunting", "batu", "kertas"]
indeks_comp = random.randint (0, 2)
komputer = pilihan[indeks_comp]
print ("pilihan komputer adalah", komputer)

if user == komputer:
    print ("seri")
else:
    if user == "kertas":
        if komputer == "gunting":
            print("user kalah")
        elif komputer == "batu":
            print ("user menang")
    if user ==  "batu":
        if komputer == "kertas":
            print("user kalah")
        elif komputer == "gunting":
            print("user menang")
    if user == "gunting":
        if komputer == "batu":
            print("user kalah")
        elif komputer == "kertas":
            print("user menang")