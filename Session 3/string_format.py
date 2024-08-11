my_name = "dacode"
print("apakah "+ my_name +" start with dev?")
# kita bisa pakai yang namanya format string kata kunci f

my_string = f"apakah {my_name} start with dev?"
print(my_string)

#angka
angka = 123.123456789
format_angka = f"angka = {angka}"
print(format_angka)

#aku mau ambil 2 angka belakang coma
format_angka = f"angka = {angka:.5f}" #artinya untuk pring 5 angka dibelakang coma f itu float
print(format_angka)
#gimana caranya kalau aku mau limir printnya
# dia untuk nampilin leading zero
format_angka = f"angka = {angka:20.5f}" # ini artinya print maksimal angknya 5 angka dan maksimal 2 angka dibelakang coma
print(format_angka)

format_angka = f"angka = {angka:020.5f}" # ini artinya print maksimal angknya 5 angka dan maksimal 2 angka dibelakang coma
print(format_angka)

#format percent
# contoh aku punya decimal
persen = 0.065 #= #6.5%
fromat_persen = f"format presen = {persen:.5%}"
print(fromat_persen)

angka = 255
print(f"binary = {bin(angka)}") #-> basis 2
print(f"octal = {oct(angka)}")  # octal basis 8
print(f"hexa = {hex(angka)}") #hexa basis 16
