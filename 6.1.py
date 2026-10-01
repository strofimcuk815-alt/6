Andriy="Andriy"
Anna="Anna"
David="David"
Mike="Mike"
Name=input("Введіть ім`я: ")
try:
    if Name==Andriy:
        Andriy = "Child"
        print(Andriy)
    elif Name==Anna:
        Anna = "Teenage"
        print(Anna)
    elif Name==David:
        David = "Adult"
        print(David)
    elif Name==Mike:
        Mike = "Grandfather"
        print(Mike)
    else:
        print(error)
except NameError:
    print("Такого ім`я в списку нема")