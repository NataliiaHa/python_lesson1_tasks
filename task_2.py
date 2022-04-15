# Task_2
sec = int(input("Пожалуста, введите время в секундах:"))
hrs = sec // 3600
min = sec % 3600 // 60
sec = sec % 60
print(f"{hrs}:{min}:{sec}")
