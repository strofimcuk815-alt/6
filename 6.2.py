try:
    Numb = float(input("Введіть число: "))
    print(round(Numb))
except ValueError:
    print("Помилка!")