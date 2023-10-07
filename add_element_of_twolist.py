print("MOHAMMED NOORUDHEEN MT , 40 , MCA 2022 - 2024 ")
input_str1 = input("Enter elements list1 separated by spaces: ")
list1 = input_str1.split()

input_str2 = input("Enter elements list2 separated by spaces: ")
list2 = input_str2.split()

if len(list1) != len(list2):
    print("Error: Lists must have the same length for element-wise addition.")
else:
    list1 = [int(item) for item in list1]
    list2 = [int(item) for item in list2]

    result = [a + b for a, b in zip(list1, list2)]

    print("Element-wise sum of the two lists:", result)

