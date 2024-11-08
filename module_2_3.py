# Исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Начальное значение индекса
index = 0

# Цикл while, который работает, пока индекс меньше длины списка
while index < len(my_list):
    # Получаем текущее число по индексу
    num = my_list[index]

    # Если число отрицательное, завершаем цикл
    if num < 0:
        break

    # Если число ноль, пропускаем эту итерацию и увеличиваем индекс
    if num == 0:
        index += 1
        continue

    # Если число положительное, выводим его
    print(num)

    # Увеличиваем индекс для перехода к следующему числу
    index += 1
