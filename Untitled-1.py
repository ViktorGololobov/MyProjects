print("Сервис поиска авиабилетов\n"
        "\nГлавное меню:\n"
        "\n1 - ввод рейса"
        "\n2 - вывод всех рейсов"
        "\n3 - поиск рейса по номеру"
        "\n0 - завершение работы\n")
choice = int(input("Введите номер пункта меню: "))

if choice == 1:

    string = ""

    def flight(value):
        count = 0
        for _ in value:
            count += 1
        if count != 4:
            return False
        else:
            return True


    flight_number = input("ХХХХ - номер рейса: ")

    while flight(flight_number) == False:
        flight_number = input("Номер рейса состоит из четырёх символов."
                       "\nВведите его повторно, так как было введено"
                       "\nбольшее или меньшее количество допустимых символов: ")
    else:
        string += flight_number.upper()

    def date(value):
        count = 0
        for _ in value:
            count += 1
        if count != 10:
            return False
        else:
            return True


    flight_date = input("ДД/ММ/ГГГГ - дата рейса: ")

    while date(flight_date) == False:
        flight_date = input("Дата рейса состоит из десяти символов."
                            "\nВведите её повторно, так как было введено"
                            "\nбольшее или меньшее количество допустимых символов: ")
    else:
        string += flight_date

    def time(value):
        count = 0
        for _ in value:
            count += 1
        if count != 5:
            return False
        else:
            return True


    departure_time = input("ЧЧ:ММ - время вылета: ")

    while time(departure_time) == False:
        departure_time = input("Время рейса состоит из пяти символов."
                               "\nВведите его повторно, так как было введено"
                               "\nбольшее или меньшее количество допустимых символов: ")
    else:
        string += departure_time

    flight_time = input("ЧЧ.ММ - время перелета: ")

    while time(flight_time) == False:
        departure_time = input("Время рейса состоит из пяти символов."
                               "\nВведите его повторно, так как было введено"
                               "\nбольшее или меньшее количество допустимых символов: ")
    else:
        string += flight_time

    def in_out_airport(value):
        count = 0
        for _ in value:
            count += 1
        if count != 3:
            return False
        else:
            return True


    airport_depo = input("XXX - аэропорт вылета: ")

    while in_out_airport(airport_depo) == False:
        departure_time = input("Время рейса состоит из пяти символов."
                               "\nВведите его повторно, так как было введено"
                               "\nбольшее или меньшее количество допустимых символов: ")
    else:
        string += airport_depo.upper()

    airport_arvl = input("XXX - аэропорт прилёта: ")

    while in_out_airport(airport_arvl) == False:
        departure_time = input("Время рейса состоит из пяти символов."
                               "\nВведите его повторно, так как было введено"
                               "\nбольшее или меньшее количество допустимых символов: ")
    else:
        string += airport_arvl.upper()

    price = input(".ХХ - стоимость билета (> 0): ")
    minus = "-"

    while minus in price:
        price = input("Стоимость билета не может быть отрицательной."
                            "\nВведите её повторно: ")
    else:
        string += price


    def string_delimiter(long_string):
        count = 0
        main_string = ''

        for i in long_string:
            count += 1
            main_string += i
            if count == 4:
                main_string += ' '
            if count == 14:
                main_string += ' '
            if count == 19:
                main_string += ' '
            if count == 24:
                main_string += ' '
            if count == 27:
                main_string += ' '
            if count == 30:
                main_string += ' '
        return main_string

    print(f"Информация о рейсе {string_delimiter(string)} добавлена")
