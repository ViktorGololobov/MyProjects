print("Сервис поиска авиабилетов")


def main_menu():
    return "\nГлавное меню:\n" \
           "\n1 - ввод рейса" \
           "\n2 - вывод всех рейсов" \
           "\n3 - поиск рейса по номеру" \
           "\n0 - завершение работы\n"


print(main_menu())
choice = int(input("Введите номер пункта меню: "))

string = ""
all_strings = ""
count = 0


def length_validate(value, valid_length):
  count = 0
  for _ in value:
    count += 1
  if count != valid_length:
    return False
  else:
    return True


def in_out_airport(value):
    count = 0
    for _ in value:
        count += 1
    if count != 3:
        return False
    else:
        return True


def string_delimiter(long_string):
    count = 0
    main_string = ''

    for i in long_string:
        count += 1
        main_string += i
        if count == 4:
            main_string += ' '
        elif count == 14:
            main_string += ' '
        elif count == 19:
            main_string += ' '
        elif count == 24:
            main_string += ' '
        elif count == 27:
            main_string += ' '
        elif count == 30:
            main_string += ' '
    return main_string + "*"


def uniq_flight_check(long_string, all_flights):
    if string_delimiter(long_string) in all_flights:
        return False
    else:
        return True


def all_flights_show(all_planes, one_of_flying):
    for all_flyings in all_planes:
        one_of_flying += all_flyings
        if all_flyings == "*":
            print("Информация о рейсе:", one_of_flying)
            one_of_flying = ""


def get_number_from_race_inf(user_number, race_inf):
    flying_ticket = ""
    for symbol in race_inf:
        if symbol == " ":
            return flying_ticket == user_number
        flying_ticket += symbol
    return False


def one_way_ticket(user_number, all_races):
    result = ""
    flight = ""
    for symbol in all_races:
        flight += symbol
        if symbol == "*":
            if get_number_from_race_inf(user_number, flight):
                result += "Информация о рейсе: "
                result += flight
                result += '\n'
                flight = ""
                continue
            else:
                flight = ""
                continue
    return result


while choice != 0:
    string = ""
    if choice == 1:
        print("Введите данные рейса: ")

        flight_number = input("ХХХХ - номер рейса: ")
        length = 4

        while length_validate(flight_number, length) == False:
            flight_number = input("Номер рейса состоит из четырёх символов."
                                  "\nВведите его повторно, так как было введено"
                                  "\nбольшее или меньшее количество допустимых символов: ")
        else:
            string += flight_number.upper()

        flight_date = input("ДД/ММ/ГГГГ - дата рейса: ")
        length = 10

        while length_validate(flight_date, length) == False:
            flight_date = input("Дата рейса состоит из десяти символов."
                                "\nВведите её повторно, так как было введено"
                                "\nбольшее или меньшее количество допустимых символов: ")
        else:
            string += flight_date

        departure_time = input("ЧЧ:ММ - время вылета: ")
        length = 5

        while length_validate(departure_time, length) == False:
            departure_time = input("Время рейса состоит из пяти символов."
                                   "\nВведите его повторно, так как было введено"
                                   "\nбольшее или меньшее количество допустимых символов: ")
        else:
            string += departure_time

        flight_time = input("ЧЧ.ММ - время перелета: ")
        length = 5

        while length_validate(flight_time, length) == False:
            flight_time = input("Время рейса состоит из пяти символов."
                                   "\nВведите его повторно, так как было введено"
                                   "\nбольшее или меньшее количество допустимых символов: ")
        else:
            string += flight_time

        airport_depo = input("XXX - аэропорт вылета: ")
        length = 3

        while length_validate(airport_depo, length) == False:
            airport_depo = input("Аэропорт вылета состоит из трех символов."
                                 "\nВведите его повторно, так как было введено"
                                 "\nбольшее или меньшее количество допустимых символов: ")
        else:
            string += airport_depo.upper()

        airport_arvl = input("XXX - аэропорт прилёта: ")
        length = 3

        while in_out_airport(airport_arvl) == False:
            airport_arvl = input("Аэропорт прилета состоит из трех символов."
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

        if uniq_flight_check(string, all_strings) == True:
            all_strings += string_delimiter(string)
            print(f"Информация о рейсе {string_delimiter(string)} добавлена")
        else:
            print("Введенный рейс уже есть в списке")

        print(main_menu())
        choice = int(input("Введите номер пункта меню: "))
    elif choice == 2:
        this_flying = ""

        all_flights_show(all_strings, this_flying)

        print(main_menu())
        choice = int(input("Введите номер пункта меню: "))
    elif choice == 3:
        user_flying = input("Введите номер рейса: ")
        result = one_way_ticket(user_flying, all_strings)

        if result == "":
            print("Рейс не найден\n")
        else:
            print(result)

        print(main_menu())
        choice = int(input("Введите номер пункта меню: "))
    elif choice == 0:
        break
    else:
        print("Такой команды не существует. Пожалуйста, введите одну из следующих команд:")
        print(main_menu())
        choice = int(input("Введите номер пункта меню: "))