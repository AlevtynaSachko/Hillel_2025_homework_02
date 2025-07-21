user_input = input("Введіть новий рядок: ")
unique_chars = set(user_input)

if len(unique_chars) > 10:
    print(True)
else:
    print(False)


