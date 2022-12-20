# калькулятор v 0.2
# не забыть про деление на ноль

i = 1

while i > 0:  # бесконечный цикл №1
    if i == 1:  # вывод приветствия один раз в первую итерацию
        print('Добро пожаловать в калькулятор Андрея! v_0.2')  # приветствие
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-']  # массив допустимых символов
    symbols_2 = ['.', '-']  # массив допустимых символов при вводе чисел
    operations = ['+', '-', '*', '/']  # массив доступных операций с числами
    state_base = 0  # для бесконечного цикла №2
    state = 0  #

    # дать выбор пользователю, решать примеры через строковое выражение или по вопросам(на будущее для v0.3)
    # операция
    while state_base == 0:
        operation = input('Выбери операцию: + - * /\n')

        # защита от ввода более одного символа в выборе операции
        if len(operation) > 1:
            print('Выбор операции осуществляется вводом одного символа!\nДавай начнём сначала...')
            break
        if operation in operations:  # проверка правильного ввода +, -, *, /
            first_num = input('Так-с, теперь введи первое число.\n')  # ввод 1 числа
            numbers = []
            numbers = numbers + [first_num]
            first_num = numbers[0]
            index_num = 0
            state = 0
            while state == 0:

                # защита от ввода символов вместо цифр
                counter_crash = 0  # счётчик для выявления ошибок
                # last_counter_crash = -1 #отстающий счётчик для выявления ошибок
                symbols_2_crash = []  # массив для сбора символов
                while counter_crash < len(numbers[index_num]):  # пока счётчик меньше длины введенного числа
                    if index_num == 0 or index_num == 1:
                        number = numbers[index_num]
                    if number[counter_crash] in symbols:  # если индекс числа есть в symbols
                        if number[counter_crash] in symbols_2:  # если индекс числа есть в symbols_2
                            symbols_2_crash = symbols_2_crash + [number[counter_crash]]  # то добавляем символ в массив

                            if len(symbols_2_crash) > 2:  # если длина массива с ошибками больше 2
                                print('Ошибка №1. Неверный ввод данных из-за точки или минуса.')
                                state_base = 1
                                state = 1
                                counter_crash = len(number)
                                symbols_2_crash = []

                            if len(symbols_2_crash) == 2:  # если длина массива с ошибками == 2
                                if symbols_2_crash[0] == symbols_2_crash[1]:
                                    print('Ошибка №2. Неверный ввод данных из-за точки или минуса.')
                                    state_base = 1
                                    state = 1
                                    counter_crash = len(number)
                                    symbols_2_crash = []

                        counter_crash = counter_crash + 1
                        # last_counter_crash = last_counter_crash +1
                    else:
                        print('Ошибка №3. Принимаю только числа!')
                        number = input('Теперь попробуй ещё раз ввести первое число.\n')  # ввод 1 числа
                if index_num == 1:
                    break
                if state == 1:  # выход из цикла из-за наличия выведенной ошибки
                    state = 0
                    break
                if index_num == 0:
                    index_num = index_num + 1
                second_num = input('Вводи второе число.\n')  # ввод 2 числа
                numbers = numbers + [second_num]
                second_num = numbers[1]

                # выполнение операции
                state = 0  # обнуляем статус перед следующей операцией
                if operation == '+':
                    plus = float(numbers[0]) + float(numbers[1])
                    print(f'\n{numbers[0]} + {numbers[1]} = {plus}')
                    state = 1
                if operation == '-':
                    minus = float(numbers[0]) - float(numbers[1])
                    print(f'\n{numbers[0]} - {numbers[1]} = {minus}')
                    state = 1
                if operation == '*':
                    umnoj = float(numbers[0]) * float(numbers[1])
                    print(f'\n{numbers[0]} * {numbers[1]} = {umnoj}')
                    state = 1
                if operation == '/':
                    delen = float(numbers[0]) / float(numbers[1])
                    print(f'\n{numbers[0]} / {numbers[1]} = {delen}')
                    state = 1

        # вывод ошибки
        else:
            print('Ошибка №4. Неверно выбрана операция!\nВыбери 1 из 4 операций, напиши + или другую операцию')
            state = 1

    # счетчик бесконечного цикла
    i = i + 1
