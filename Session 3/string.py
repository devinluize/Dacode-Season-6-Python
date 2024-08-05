data = "ini adalah string"
print(data)
#1. cara membuat string

dev = '''
    1. bisa membuat string dengan single quote '...'
    2. dengan menggunakan double quote "..."
'''
data = 'ini adalah strings menggunakan single quotes'
print(data)

data = "ini adalah string menggunakan double quotes"
print(data)

print('"halo semua"')
print(data)

# 2. menggunakan tnada

#kita bisa membuat tanda ' jadi string escape sequence
print('mari te\'s')
print('the moon is beautiful isn\'t it')


#backlash
print("C:\\user\\devin")

#tab
print("devin \t tes")
#backspace
print("dev \btes")
#newline
print("baris pertama, \n baris kedua") # lf -> line feed -> unix and max os
print("baris pertama, \r baris kedua") # cr classic os acorn
print("baris pertama, \r\n baris kedua") # crlf line eef cariage return
#3 . string literal atau raw string
#hati hati
print("C:\newfolder\\devin") #jadi salah

print("C:\\newfolder\\devin") #bener tapi ini kan banyak
# ada cara
# kita bisa pakai raw string
print(r'C:\newfolder\devin')
#multiline literal string

print("""
Nama:devin
semester:7
""")
#multiline literan + raw
print(r"""
Nama:devin
semester:7
C:\newfolder\devin
""")
