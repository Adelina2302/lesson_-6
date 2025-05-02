import string


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


def main():
    password = input("Введите пароль: ")
    score = 0
    checks = [
        has_digit,
        is_very_long,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    for check in checks:
        if check(password):
            score += 2

    print(f"Рейтинг пароля: {score}")

# Блок if __name__ == "__main__"
if __name__ == "__main__":
    main()
