# data type -> adalah tipe data yang bisa kita gunakan dalam python
#  1. tipe data angka (integer)
data_integer = 12
print("data : ",data_integer,"bertipe data", type(data_integer))
#kita ada tipe data float(decimal)
data_float = 11.999999
print("data : ",data_float,"bertipe data", type(data_float))
#tipe data ketiga tipe data string
data_string = "devin luize saan"
print("data : ",data_string,"bertipe data", type(data_string))
#boolean -> True or False
# 0 atau 1
data_bool = True
print("data : ",data_bool,"bertipe data", type(data_bool))

#tipe data double -> mirip sama float tapi dia lebih akurat float
# from ctypes import c_double
# data_double = c_double(3.14)
# print("data : ",data_double,"bertipe data", type(data_double))
import math
#TYPE CAST
#aku mau ngubah dari tipe data integer ke double
data_float_cast = float(data_integer)
print('data cast: ',data_float_cast,"bertipe data", type(data_float_cast))

data_int_cast = int(data_integer)
# data_int_cast = int(math.ceil(data_integer))
print("data cast: ",data_int_cast,"bertipe data", type(data_int_cast))

data_string_cast = str(data_integer)
print("data cast: ",data_string_cast,"bertipe data", type(data_string_cast))

x = 25
y = 20.1
hasil = x + y # ini tipe datanya unt
print("data cast: ",hasil,"bertipe data", type(hasil))

kalimat = "hasil adalah " #ini kan tipe datnaya string
print(kalimat + str(hasil))