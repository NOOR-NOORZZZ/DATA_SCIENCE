print("MOHAMMED NOORUDHEEN MT, 40, MCA 2022 - 2024")


def count_vowels(input_string):
    input_string = input_string.lower()

    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in input_string:
        if char in vowel_count:
            vowel_count[char] += 1

    return vowel_count


user_input = input("Enter a string: ")

result = count_vowels(user_input)

print("Count of each vowel in the string:")
for vowel, count in result.items():
    print(f'{vowel}: {count}')
