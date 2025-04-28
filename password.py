import string


def check_password(password):
    if any(char.isdigit() for char in password):
        print("Есть цифры")
    else:
        print("Нет цифр")


def has_digit(password):
    return any(char.isdigit() for char in password)


def is_very_long(password):
    return len(password) > 12


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(char in string.punctuation for char in password)


password = input("Введите пароль: ")

length = len(password)
print("Длина пароля:", length)

print("Короткий" if length <= 12 else "Длинный")

for char in password:
    if char.isdigit():
        print(f"{char} - Цифра")
    else:
        print(f"{char} - Буква")

check_password(password)

score = 0
checks = [has_digit, is_very_long, has_upper_letters, has_lower_letters, has_symbols]

for check in checks:
    if check(password):
        score += 2

print(f"Рейтинг пароля: {score}")
