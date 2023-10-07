print("MOHAMMED NOORUDHEEN MT , 40 , MCA 2022 - 2024 ")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a < b:
    smaller = a
else:
    smaller = b

for i in range(2, smaller + 1):
    if (a % i == 0) and (b % i == 0):
        print(f"{a} and {b} are not coprime.")
        break
else:
    print(f"{a} and {b} are coprime.")
