#ЗАВДАННЯ 1

def caching_fibonacci():
    # Створюємо порожній словник для кешу
    cache = {}
    
    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Перевірка наявності значення в кеші
        if n in cache:
            return cache[n]
        
        # Обчислюємо значення та зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]

    return fibonacci

# Приклад використання
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610