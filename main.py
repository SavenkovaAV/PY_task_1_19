with open('input.txt', 'r') as inputFile: # Открываем файл input.txt в режиме чтения
    lst = inputFile.readline().split()
    newLst = []
    for i in lst:
        newLst.append(int(i))

# создание словаря для подсчета каждого числа
num_count = {}
for num in newLst:
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

with open('output.txt', 'w') as outFile: # Открываем файл output.txt в режиме записи
    for i in result:
        outFile.write(str(i) + ' ')
