#list copy 
# a = ['a', 'b', 'c']

# b = a # DONT DO THIS
# DO THIS
# b = a.copy()
# b = list(a)
# b = a[:]

# a.remove('a')

# print(b)

# TUPLE
# b = ('a', 'b', 'c')

# # print(b[0:2])

# # update tuple
# c = list(b)
# c.append('anto')

# b = tuple(c)

# print(b)

# b = ('a', 'b', 'c', 'd', 'e', 'f')

# data1, *data2, data3, data4 = b

# print(data1, data2, data3, data4)

# a = ('a', 'b', 'c', 'd', 'e', 'f')
# b = (1,2,3,4,5)

# c = a + b

# print(len(c))

# for i in range(len(c)) : 
#     print(c[i])
    
# for i in c :
#     print(i)

# SET
# a = {"anto", "test", "devin", 2, 3,4,10, 10}
    
# a.add("elysa")

# print(a)

# a.remove("elysa")

# print(a)

# a = {"Anto", "devin", "cel", "elys", "vincen", "test", 1, 2}
# b = {1, 2, 3, 4, 5, 6, 7, 8}

# a.update(b)

# print(a)

# c = a.union(b)

# print(c)

# c = a | b
# print(c)

# c = a.intersection(b)

# a.intersection_update(b)

# print(c)
# print(a)

# c = a.difference(b)
# a.difference_update(b)

# print(c)
# print(a)

# c = a.symmetric_difference(b)
# a.symmetric_difference_update(b)
# print(c)
# print(a)

# Copy
# c = a.copy()
# print(c)

# d = set(a)
# print(d)

# manusia = {
#     "tangan": 2,
#     "nama": "antonio",
#     "teman": "devin", 
#     "umur": 21
# }

# print(manusia)

# print(manusia["nama"])
# print(manusia["teman"])

# print(manusia["tangan"]) #ini 2 equal
# print(manusia.get("tangan"))

# print(manusia.keys()) # munculin keys
# print(manusia.values()) # munculin value
# print(manusia.items()) # munculin 22nya

# manusia = {
#     "tangan": 2,
#     "nama": "antonio",
#     "teman": "devin", 
#     "umur": 21
# }

# manusia.update({"tangan": 4})
# manusia["nama"] = "ryanlie"

# print(manusia.get("tangan"))
# print(manusia.get("nama"))

# manusia.update({"kaki": 4})
# manusia["nama_belakang"] = "ryanlie"

# print(manusia)

manusia = {
    "tangan": 2,
    "nama": "antonio",
    "teman": "devin", 
    "umur": 21
}

# manusia.pop("tangan") # pop berdasarkan keys
# manusia.popitem()
# manusia.clear()

# del manusia["umur"]

# print(manusia)

# manusia2 = manusia.copy()
# manusia2 = dict(manusia)
# print(manusia2)

#  
    
    