# Домашнее задание по теме "Генераторные сборки".
# Задача с целью понять механизм создания генераторных сборок и использования встроенных функций-генераторов.

# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Шаг 1: Генераторная сборка first_result
first_result = (abs(len(first) - len(second)) for first, second in zip(first, second) if len(first) != len(second))

# Шаг 2: Генераторная сборка second_result
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))  # [1, 2]
print(list(second_result))  # [False, False, True]