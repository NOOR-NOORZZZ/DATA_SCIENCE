print("MOHAMMED NOORUDHEEN MT, 40, MCA 2022 - 2024")


def find_absent_digits(mobile_number):
    all_digits = set(range(10))
    mobile_digits = set(map(int, str(mobile_number)))
    absent_digits = all_digits - mobile_digits
    return absent_digits


mobile_number = input("Enter a 10-digit mobile number: ")

if mobile_number.isdigit() and len(mobile_number) == 10:
    result = find_absent_digits(int(mobile_number))

    if result:
        print("Digits absent in the mobile number:", sorted(result))
    else:
        print("All digits are present in the mobile number.")
else:
    print("Invalid input. Please enter a valid 10-digit mobile number.")
