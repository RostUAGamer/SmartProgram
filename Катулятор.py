print("Привіт, це калькулятор")
while True:
    print("Введи свою дію")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")
    operation = input("Введи свою дію: ")
    if operation == "5":
        print("До побачення!")
        break


    if operation == "1":
        num1 = float(input("Введи перше число: "))
        num2 = float(input("Введи друге число: "))
        print("Результат: ", num1 + num2)
    elif operation == "2":
        num1 = float(input("Введи перше число: "))
        num2 = float(input("Введи друге число: "))
        print("Результат: ", num1 - num2)
    elif operation == "3":
        num1 = float(input("Введи перше число: "))
        num2 = float(input("Введи друге число: "))
        print("Результат: ", num1 * num2)
    elif operation == "4":
        num1 = float(input("Введи перше число: "))
        num2 = float(input("Введи друге число: "))
        if num2 == 0:
            print("Ділення на нуль неможливе")
        else:
            print("Результат: ", num1 / num2)

    else:
        print("Неправильна дія")
