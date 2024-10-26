# Домашнее задание по теме "Списковые, словарные сборки".
# Задача по закреплению знаний о списочных и словарных сборках.

# Исходные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Шаг 1: Создание first_result
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Шаг 2: Создание second_result
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Шаг 3: Создание third_result
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
