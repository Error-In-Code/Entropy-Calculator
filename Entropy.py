import math


def calculate(length, char_amount):
    return math.log2(char_amount) * length


def find_chars(password):
    char_amount = 0
    char_sets = [False, False, False, False]
    char_nums = [26, 26, 10, 32]
    for i in password:
        if i.islower():
            char_sets[0] = True
        if i.isupper():
            char_sets[1] = True
        if i.isdigit():
            char_sets[2] = True
        if not i.isalnum() and i.isascii():
            char_sets[3] = True

    for x in range(4):
        if char_sets[x]:
            char_amount += char_nums[x]

    return len(password), char_amount


if __name__ == "__main__":
    password = input("Enter A Password: ")
    length, amount = find_chars(password)
    print("Entropy: ", calculate(length, amount))
