# Домашнее задание по теме "Генераторы".
# Задача c целью более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):  # Длина подпоследовательности от 1 до n
        for start in range(n - length + 1):  # Начальная позиция
            yield text[start:start + length]  # Возврат подпоследовательности


# Пример работы функции
a = all_variants("abc")
for i in a:
    print(i)
