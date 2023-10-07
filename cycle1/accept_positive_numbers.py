print("MOHAMMED NOORUDHEEN MT, 40, MCA 2022 - 2024")


def sum_of_digits(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum


def process_number(number):
    while number > 0:
        digit_sum = sum_of_digits(number)
        number -= digit_sum
        print(f"{number + digit_sum} - {digit_sum} = {number}")


positive_number = int(input("Enter a positive number: "))
process_number(positive_number)
