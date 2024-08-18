# import random

# print(random.randint(0, 2)) # range 0 - 2 (0 and 2 included)
import random

inputUser = input("masukkan input yang kamu mau [gunting, batu, kertas]: ")

databaseKecil = ["gunting", "batu", "kertas"]

indexKomputer = random.randint(0, 2)
jawabanKomputer = databaseKecil[indexKomputer]

print("jawaban komputer adalah ", jawabanKomputer)

if inputUser == jawabanKomputer :
    print("seri bro")
else :
    if inputUser == "gunting" :
        if jawabanKomputer == "kertas" :
            print("Player menang")
        elif jawabanKomputer == "batu" :
            print("player kalah")
    if inputUser == "batu" :
        if jawabanKomputer == "gunting" :
            print("Player menang")
        elif jawabanKomputer == "kertas" :
            print("player kalah")
    if inputUser == "kertas" :
        if jawabanKomputer == "batu" :
            print("Player menang")
        elif jawabanKomputer == "gunting" :
            print("player kalah")
