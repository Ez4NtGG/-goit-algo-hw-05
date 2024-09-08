#ЗАВДАННЯ 2

import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Використовуємо регулярні вирази для пошуку дійсних чисел, які чітко відокремлені пробілами.
    # Дійсні числа відображаються у форматі "число.число", наприклад "1000.01".
    numbers = re.findall(r'(?<= )\d+\.\d+(?= )', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable) -> float:
    # Використовуємо генератор для обчислення загальної суми чисел у тексті.
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")