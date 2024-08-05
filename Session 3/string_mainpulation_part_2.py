#operator dalam bentuk methods
## merubah case dari string
#   uppercase atau lowercase
salam = "hai selamat malam"
print("normal : "+ salam)
salam = salam.upper()
print("upper : "+ salam)
salam = salam.lower()
print("lower : "+ salam)

##pengecekan dengan is x method
# contoh untuk pengecekan lower case

statsu = salam.islower()
print(statsu)

statsu = salam.isupper()
print(statsu)

#isalpha -> ngecek apakah semua huruf
#isalnum -> is untuk cek apaah huruf dan angka alpha numerik
#isdecimal
#isspalce -> spasi tab newline
#istile = semua kata dimualai huruf besar

judul = "Adasd Jdasdsa Adasdas"
print("title",judul.istitle())
alpha = "asdas123"
isalpha = alpha.isalpha()
print(isalpha)
isalnum = alpha.isalnum()
print(isalnum)
isdecimal = alpha.isdecimal()
print(isdecimal)

cek_start = "Devin luize"
print("start" + str(cek_start.startswith("Dev")))

## pengabungkan kkomponen join() split()

pisah = ['aku','tes','dev'] #list
print(pisah)
gabung = ', '.join(pisah)
print(gabung)
gabungan ="devinasdluizeasdsaanasddasda"
print(gabungan.split("asd"))

## alokasi karakter rjust,ljust,center

kanan = "kanan".rjust(10,"@")
print("'" + kanan + "'")