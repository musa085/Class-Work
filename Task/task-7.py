#tapsiriq-7 coin vermeyi unutmayin:)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  

numbers = [1, 3, 5, 7, 9, 11, 13, 15]


target = int(input("Axtardiginiz ededi daxil edin: "))

result = binary_search(numbers, target)

if result != -1:
    print(f"Eded Tapildi İndeksi: {result}")
else:
    print("Eded Tapilmadi")
