file_path=input("Введіть шлях до файлу: ")
try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("Вміст файлу:")
        print(content)
except FileNotFoundError:
    print("Файл за шляхом не існує")
except Exception as e:
    print("Сталася помилка під час читання файлу")