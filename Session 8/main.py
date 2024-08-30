# def printHello(nama, *angka):
#     print("Hello!")
#     print(angka)

# printHello("devin", 1, 5, 7, 8, 9, 10, 12, 214, 512)

# def namaAnak(**anak):
#     print("anak 1 adalah", anak['anak1'])
#     print("anak 2 adalah", anak['anak2'])
#     print("anak 3 adalah", anak['anak3'])

# # namaAnak("jojo", "jeje", "juju")
# # namaAnak(anak1 = "jojo", anak2 = "jeje", anak3 = "juju")
# namaAnak(anak2 = "jeje", anak1 = "jojo",  anak3 = "juju")

# a = 10

# def test(nama, test, umur = 21):
#     b = 20
#     print(a)
#     print(b)
#     print(umur)
#     print(nama)

# test("kevin", "anto", umur = 21)

# a = lambda x : f'nama aku adalah {x}'

# b = a("antonio")

# print(b)

# def test(nama, test, umur = 21):
#     print(nama)
    
#     return umur + 10

# umur_test = test("kevin", "anto", umur = 21)

# print(umur_test)

def test(nama):
    return nama

a = lambda nama, umur, tanggal : print(nama)

a("antonio", 21, 31)
