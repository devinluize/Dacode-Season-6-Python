#1 menyambung string (concatenate)
nama_pertama = "devin"
nama_kedua = "luize"

nama_lengkap = nama_pertama + nama_kedua
print(nama_lengkap)

#menghitung panjang string
length  = len(nama_lengkap)
print(length)
#3. operator untuk string
# A. mengcek apakah ada suatu komponen di string

d = "dev"
status = d in nama_kedua
print("apakah", d, "ada di",nama_lengkap,"= ",status    )

d = "dev"
status = d not in nama_kedua
print("apakah", d, "tidak ada di",nama_lengkap,"= ",status    )
#mengulang string
print('wkwkwkwkwkwkwkw')
print('wk'*10)
#indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-0:3 : " + nama_lengkap[0:3])
print("index ke-0,2,4,6,8 : " + nama_lengkap[0:11:2]) #0 sampai 11 dengan increment 2

#item paling kecil
print("paling kecil : "+min(nama_lengkap))
#nilai paling besar
print("paling besar : " + max(nama_lengkap))
ascii_code = ord(" ")# -> one character string
print("ascii code dari spasi adalah" ,ascii_code)

data = 117
print("character untuk ascii " + str(data) + " adalah : "+ chr(data))

#operator dalam bentuk method -> method method yang bisa kita pakai untuk operasi string tersebut

# kalau misalkan method dia nempel sama string
data = "stirng data"
jumlah = data.count("a")
print("jum: = ", jumlah)