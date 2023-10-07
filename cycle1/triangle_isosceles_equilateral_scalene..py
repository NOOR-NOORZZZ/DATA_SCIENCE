print("MOHAMMED NOORUDHEEN MT , 40 , MCA 2022 - 2024 ")

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
if a == b == c:
    print("It's an equilateral triangle.")
elif a == b or b == c or c == a:
    print("It's an isosceles triangle.")
else:
    print("It's a scalene triangle.")

