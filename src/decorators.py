import time
from typing import Any, Callable, Optional
from functools import wraps


def log(filename: Optional[str] = None) -> Callable:
    """
     Декоратор log, который будет автоматически логировать начало и конец выполнения функции,
     а также ее результаты или возникшие ошибки
    """
    def decorate(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                log_message = f"{func.__name__} started at {start_time} and finished at {end_time} with result: {result}"
                if filename is not None:
                    with open('../filename.txt', 'a', encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(log_message)

                    return result
            except Exception as e:
                if filename:
                    with open('../filename.txt', 'a', encoding="utf-8") as file:
                        file.write(f"{func.__name__} error {e.__class__.__name__}.Inputs: {args}, {kwargs}")
        return wrapper
    return decorate


@log(filename='mylog.txt')
def my_function(x, y):
    """
    Получение результат суммирования двух чисел
    """
    return x + y

my_function(1, 2)





