print("MOHAMMED NOORUDHEEN MT , 40 , MCA 2022 - 2024")
print("Armstrong numbers up to 1000 are:")

for num in range(1, 1001):
    num_digits = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10

    if num == sum:
        print(num)
