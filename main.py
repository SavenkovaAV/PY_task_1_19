numbers_list = input("Введите числа через запятую: ")

# преобразование введенной строки в список чисел
numbers = []
for num in numbers_list.split(','):
    numbers.append(int(num))

# создание словаря для подсчета каждого числа
num_count = {}
for num in numbers:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

# поиск максимального количества повторений числа
max_count = max(num_count.values())

# создание списка чисел, которые встречаются максимальное количество раз
result = []
for num, count in num_count.items():
    if count == max_count:
        result.append(num)

# сортировка списка по возрастанию
result.sort()

print(result)