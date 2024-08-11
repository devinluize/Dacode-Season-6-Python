#  string adalah suatu tipe data kalimat/kata/paragraf -> kumpulan huruf
#  contoh devin luize
#  dacode

#  gimana cara kita buat string
#  ada banyak cara buat string
#cara pertama ini cara yang sering dipakai
#cara pertama pakai petik 2"

str = "ini string pakai petik 2"
print(str)
#cara kedua kita pakai '
str = 'ini string pakai petik 1'
print(str)
str = "ini adalah hari jum'at"
str_Test = 'ini adalah "hari" jumat'
print(str_Test)

# cara ketiga kita bisa bikin pakai "escape sequence"
#escape sequence adalah suatau cara agar kita melakukan print special character '," -> special character [\]
str = "budi bilang \"hari ini dia ada kelas\""
print(str)
str = 'budi bilang hari ini hari jum\'at'
print(str)

#gimana cara kita bisa print \
str_with_back_slash = "C:\\Users\\devin Luize\\Pictures\\DacodeS 6\\Python\\Class\\Session 3"
print(str_with_back_slash)

#pengunaan [\] backslash ada banyak banget
#bisa buat tab [\t]
print("devin\tluize")
# bisa buat backspace [\b]
print("devin\bluize")
# bisa buat enter/new line [\n]
print("ini adalah kalimat pertama \ndan ini adalah kalimat kedua")
#kalau aku mau orintnya gini
print("C:\\newfolter\\devin")
#ada yang namanya string raw jadi apa yang akan kita tulis daialam itu akan di print semuanya
#caranya kita tinggal perlu tambahin "r" didepan kalimat
print(r"C:\Users\Devin Luize\Pictures\DacodeS 6\Python\Class\Session 3")
print(r"hari ini hari jum'at")
# print(r"budi bilang "hari ini hari jumat"") # ini gacoleh sama raw
# untuk lakuin print diatas kita bisa pakai namanya string literal
#string literal adalah string yang kita bisa kita buias bilang dia dia kumpulan kata kata didalemnyayang bisa kita format

# tetep bikinnya bisa pakai ' atau " kita print dengan 3x single quotes 3x double quotes
print("""
nama : devin
semester : 7
""")

print('''
nama : devin
semester : 7
''')


#string literal bisa kita gabung juga dengan raw string
print(r"""
nama : devin
semester : 7
C:\Users\Devin Luize\Pictures\DacodeS 6\Python\Class\Session 3
""")
