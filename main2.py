import time
from multiprocessing import Pool, cpu_count

# Синхронна версія функції factorize
def factorize_sync(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result

# Асинхронна версія функції factorize
def factorize_async(*numbers):
    def factorize_number(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors

    with Pool(cpu_count()) as pool:
        results = pool.map(factorize_number, numbers)
    
    return results

# Функція для вимірювання часу виконання
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Вхідні дані для функції factorize
numbers = [128, 255, 99999, 10651060]

# Вимірюємо час виконання синхронної версії
result_sync, execution_time_sync = measure_time(factorize_sync, *numbers)

# Вимірюємо час виконання асинхронної версії
result_async, execution_time_async = measure_time(factorize_async, *numbers)

# Виводимо результати та час виконання для обох версій
print("Синхронна версія:")
print("Результати:", result_sync)
print("Час виконання:", execution_time_sync, "секунд")


print("Асинхронна версія:")
print("Результати:", result_async)
print("Час виконання:", execution_time_async, "секунд")
