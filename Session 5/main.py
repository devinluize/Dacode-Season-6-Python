# ada 2 cara melakukan looping
#cara 1 menggunakan for loop
#cara 2 menggunakan while loop
import random

#while kita pake kalau kita gatau kapan dia bakal berhenti contoh aku
#ngerandom angka pokoknya sampe angkanya ga 20 dia gabakal berhenti

#forloop kita pake kalau kita uda tau kita mau looping sebanyak berapa kali atau kita uda tau apa yang mau kita iterasi

#contoh pengunaan for loop 1
# aku mau iterasi sebanyak 10x
# diantara 10
for x in range(10):
    print(f"x sekarang adalah {x}")

print("               ")
#cara kedua kita bisa menentukan x kita bisa jalan dari breapa sampai berapa
for x in range(-10, 10):
    print(f"x sekarang adalah {x}")

#cara ketiga kita bisa melakukan iterasipada suatu "slice/array" -> kumpulan data
data = [2,432,42,34,34,5,74,675,65,3,123,"ini","str"] #ini namanya list
print(data)
for x in data:
    print(f"data sekarang adalah {x}")

#cara ke 4 data string
str = "halo semua jangan lupa join dacode"
print(str)

index = 0
for x in str:
    if index >= 5 and index <= 21:
        print(f"data sekarang adalah {x}")
    index += 1

#cara looping yang kedua yaitu pakai while

# while -> selama
# while x masih kurang dari 10 maka jalankan
#     while kondisi:
#         proses
i = 0
print("===========WHILE====================")
while i<10:
    print(f"data sekarang adalah {i}")
    pass
    i += 2

#break adalah suatu kondisi yang kita gunakan untuk stop looping tersebut
#continye adalah suatu syntax untuk kita ngelakuin skip 1x dalam loopingan
while True:
    #misalkan aku mau random angka dari 1->20
    # kalau angkanya 15 kita stop
    random_number = random.randint(5, 100)
    print(f"random_number sekarang adalah {random_number}")
    if random_number == 15:
        break
    # print("===========WHILE===================")

#contoh continue
for i in range(10):

    if i == 5:
        continue

    print(f"Halo semuanya ke {i}")