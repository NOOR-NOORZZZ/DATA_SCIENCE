print("MOHAMMED NOORUDHEEN MT, 40, MCA 2022 - 2024")


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


n = int(input("Enter the number of elements: "))
elements = []

print("Enter the elements:")
for _ in range(n):
    element = int(input())
    elements.append(element)

bubble_sort(elements)

print("Sorted array:", elements)
