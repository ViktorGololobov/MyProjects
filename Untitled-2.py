flight = input("ХХХХ - номер рейса: ")
flight_date = input("ДД/ММ/ГГГГ - дата рейса: ")
departure_time = input("ЧЧ:ММ - время вылета: ")
flight_time = input("ЧЧ.ММ - время перелета: ")
departure_airport = input("XXX - аэропорт вылета: ")
arrival_airport = input("XXX - аэропорт прилёта: ")
price = input(".ХХ - стоимость билета (> 0): ")
string = ''

def exam_string(a):
    string = ''
    while True:
        string += a
        return string

main_string = exam_string(flight) + exam_string(flight_date) + exam_string(departure_time) + exam_string(flight_time) + exam_string(departure_airport) + exam_string(arrival_airport) + exam_string(price)
print(main_string)