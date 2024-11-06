# Домашнее задание по теме "Декораторы".
# Задание: Декораторы в Python.

def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Проверка, является ли результат простым числом
        if result < 2:
            print(f'{result} не является простым числом.')
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print(f'{result} не является составным числом.')
                    break
            else:
                print(f'{result} является простым числом.')

        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования функции
result = sum_three(2, 3, 6)
print(result)
