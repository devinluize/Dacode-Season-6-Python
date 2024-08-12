#contoh aku mau validasi jika namanya yang aku input "devin" maka bilang hai devin
#elif -> else if
nama = input("masukan nama anda : ")
#indentation adalah spasi didepan yang menandakan block dari suatu codingan
#else kondisi juga if nya tidak memenuhi kondisi
# if kondisi : proses
if nama == "devin":
    print("Hai Devin")
elif nama == "luize":
    print("Hai luize")
elif nama == "dacode":
    print("Hai dacode")
else:
    print("Kamu siapa???")

# if terus if terus if lagi dia akan ngecek semua kondisi 33 nya

# operations = {
#     "devin" : "Hai Devin Switch case",
#     "luize" : "Hai luize Switch case",
#     "dacode" : "Hai dacode Switch case"
# }
#
# # dictionary adalah suatu "kamus" dengan kaca kunci pairing
#
# # result = operations[nama]
# result = operations.get(nama ,"name not found")
# print(result)

# value = nilai_jika_true if kondisi else nilai_jika_salah

a = 10
b = 20
#aku mau cari mana yang lebih besar antar a dan b
value = b if b > a else a
print(value)