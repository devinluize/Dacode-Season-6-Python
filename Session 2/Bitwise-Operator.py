#bitwise operator adalah operator yang kita gunakan untuk mengmanipulasi suatu biner dari bilangan tertentu
import ctypes

# bilangan biner adalah bilangan yang berbasis 2 dia cuman ada angka 0 dan 1
# bilangan decimal -> dia basis 10 0,1234556789

# print(str(97))
# string()

a = 20  # 1010
b = 4  # 0100
#operasi bitwise yang pertama adalah & -> and
print(a & b) # 0000 -> 0
#operasi bitwise kedua | -> or
print(a | b) #1110 -> decimal = 2+4+8 = 14
#left shit dan right shift
#dia ngegeser binary kita ke kanan atau ke kiri
print(a<<2) #geser bitnya 2 kekiri #010100 # = 40
print(a>>2)
# xor xclusive or
#dia akan menghasilkan 1 jika binernya beda tapi klaau binernya sama dia akan hasilin 0
print(a^b)
# not ~
from ctypes import c_uint
x = ctypes.c_uint(~a)
print(x)
print(~a) #-11
# -(a+1)

#1010
#0100
#0

