#string manipulation adalah cara cara untuk kita bisa melakukan manipulasi pada string
# contoh
#1 concantenate(concat) adalah suatu fungsi untuk kita bisa gabungin 2 string atau lenih
first_name = "devin"
last_name = "luize"
my_name = first_name + " " + last_name
print(my_name)
#kedua ngitung panjang character yang ada dalam suatu string
#aku mau itung my_name ini panjangnya berapa
print(len(my_name))

#sekarang mau melakukan pengeceakan apakah suata kata ada didalam kata lainnya
#contoh budi mau makan pisang
#apakah budi ada didalam kalimat diatas?
str_main = "budi mau makan pisang"
str_sub = "budi"
status = str_sub in str_main
print(status)
#apakah tidak ada
status = str_sub not in str_main
print(status)

#contoh ke empat
# pengulangan string
print("wkwkwkwkwkwkkwkwkwkwkwk")
print(10*'wk')
print('wk'*10)
str_enter = "devin\tluize"
#kita masuk ke indexing
print("index ke 0 dari str_main : " + str_main[0])
print("index ke 10 dari str_main : " + str_main[10])
#kita bisa juga print index dari sekian ke skian
print("index ke 0 sampai 5 dari str_main : " + str_main[0:6])
#kita bisa print kelipatan
#aku mau print dari 0 -> 12 tapi kelipatan 3 0,3,6,9
print("index ke 0,3,6,9 : ",str_main[0:12:3])
#kita bisa cari character terkecil diitung berdasarkan ascii code
print(min(str_sub))
print(max(str_sub))

#bisa ngitung banyaknya chacracter tertentu didalam kalimat
# contoh aku mau itung ada berapa banyak "a" didalam kalimat bdui mau makan pisang
print(str_main.count("a"))

#kita bisa juga capilatin semua kata yang ada di string tersebut
#ataupun kecilin
# contoh aku mau capilatin semua budi mau makan pisang
str_main = str_main.upper()
print(str_main)
str_main = str_main.lower()
print(str_main)

#is title
# dia bakal cek apakah huruf pertama dari setiap kata adalah kapital
# contoh
judul = "World War History"
print(judul.istitle())
#isalpha
# is alpha adalah function untuk ngecheck apakah string kita ini alphabet aja atau ada yang lain
judul = "WorldWarHistory"
print(judul.isalpha())
#isalnum -> ini untuk ngecek angka dan huruf
# judul.isdecimal()
print("apakah "+my_name+" start with dev? hasilnya : " + str(my_name.startswith("dev")))
