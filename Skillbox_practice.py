print("Введите данные рейса: ")
flight = input("ХХХХ - номер рейса: ")
count = 0

for i in flight:
    count += 1
if count != 4:
    flight = input("Номер рейса состоит из четырёх символов."
                   "\nВведите его повторно, так как было введено"
                   "\nбольшее или меньшее количество допустимых символов: ")
else:
    count = 0

flight_date = input("ДД/ММ/ГГГГ - дата рейса: ")

for i in flight_date:
    count += 1
if count != 10:
    flight_date = input("Дата рейса состоит из десяти символов."
                        "\nВведите её повторно, так как было введено"
                        "\nбольшее или меньшее количество допустимых символов: ")
else:
    count = 0

departure_time = input("ЧЧ:ММ - время вылета: ")

for i in departure_time:
    count += 1
if count != 5:
    departure_time = input("Время рейса состоит из пяти символов."
                           "\nВведите его повторно, так как было введено"
                           "\nбольшее или меньшее количество допустимых символов: ")
else:
    count = 0

flight_time = input("ЧЧ.ММ - время перелета: ")

while float(flight_time) < 0:
    flight_time = input("Время перелёта не может быть отрицательным."
                        "\nВведите его повторно: ")

departure_airport = input("XXX - аэропорт вылета: ")

for i in departure_airport:
    count += 1
if count != 3:
    departure_airport = input("Аэропорт указывается тремя символами."
                              "\nВведите его повторно, так как было введено"
                              "\nбольшее или меньшее количество допустимых символов: ")
else:
    count = 0

arrival_airport = input("XXX - аэропорт прилёта: ")

for i in arrival_airport:
    count += 1
if count != 3:
    arrival_airport = input("Аэропорт указывается тремя символами."
                            "\nВведите его повторно, так как было введено"
                            "\nбольшее или меньшее количество допустимых символов: ")
else:
    count = 0

price = float(input(".ХХ - стоимость билета (> 0): "))

while price < 0:
    price = float(input("Стоимость билета не может быть отрицательной."
                        "\nВведите её повторно: "))

print("Информация о рейсе", flight.upper(), flight_date, departure_time, flight_time, departure_airport.upper(),
      arrival_airport.upper(), price, "добавлена")

	



