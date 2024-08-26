def linear_search(arr, xtarget):
    for i in range(len(arr)):
        if arr[i] == int(xtarget):
            return i
    return -1

arr = [2, 3, 4, 10, 40, 34, 14, 123, 34, 67]
target = input("Masukan Angka yang ingin kalian cari ")
position = linear_search(arr, target)
if position == -1:
    print("Target Not Found")
else:
    print(f"Target Found On Index {position}")


