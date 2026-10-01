import math
func_name = "non_existent_function"
try:
    func = getattr(math, func_name)
    func()
except AttributeError:
    print("Функцію не знайдено у модулі")