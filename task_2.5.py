my_rating = [4, 3, 2, 1, 5]
new_number = int(input('Введите место в рейтинге: '))
i = 0
for n in my_rating:
    if new_number <= n:
        i += 1
my_rating.insert(i, new_number)
print(my_rating)
