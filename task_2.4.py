custom_str = input("Введите слова через пробел: ").split()
for i, word in enumerate(custom_str, 1):
    print(f"{i}.{word[:10]}")
