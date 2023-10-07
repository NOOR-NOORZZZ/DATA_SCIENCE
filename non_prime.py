print("MOHAMMED NOORUDHEEN MT , 40 , MCA 2022 - 2024 ")
a = int(input("enter lower limit :"))
b = int(input("enter the upper limit :"))
print("prime numbers between", a, "and", b, "are:")
for i in range(a,b+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                print(i)
                break

