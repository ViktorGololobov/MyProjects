def in_out_airport(value, border):
    count = 0
    while count < 3:
        for _ in value:
            count += 1
        if count > border or count < border:
            return False
        else:
            return True

low_high_border = int(input("Введите границу: "))
airport_depo = input("XXX - аэропорт вылета: ")
print(in_out_airport(airport_depo, low_high_border))

airport_arvl = input("XXX - аэропорт прилёта: ")
print(in_out_airport(airport_arvl, low_high_border))