def binary_search(arr, xtarget):
    left, right = 0, len(arr)-1
    print(arr)
    arr.sort()
    print(arr)

    #left selalu posisi 0 dan right panjang dari arraynya karna 0 based makanya dikurang 1
    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == int(xtarget):
            return mid
        elif arr[mid] < int(xtarget):
            left = mid + 1
        elif arr[mid] > int(xtarget):
            left = mid - 1
    return -1
    #kita maunya dia bukan jdai float tapi jadi int // artinya floow division dia selalu buletin kebawa

arr = [2, 3, 4, 10, 40, 34, 14, 123, 34, 67]
target = input("Masukan Angka yang ingin kalian cari ")
position = binary_search(arr, target)
if position == -1:
    print("Target Not Found")
else:
    print(f"Target Found On Index {position}")


