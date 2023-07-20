def in_out_airport(airport):
    count = 0
    while count < 3:
        for _ in airport:
            count += 1
            if count > 3:
                count = 0
                _ = ''
                airport = input("Аэропорт указывается тремя символами."
                                          "\nВведите его повторно, так как было введено"
                                          "\nбольшее или меньшее количество допустимых символов: ")


airport_depo = input("XXX - аэропорт вылета: ")
print(in_out_airport(airport_depo))

airport_arvl = input("XXX - аэропорт прилёта: ")
print(in_out_airport(airport_arvl))