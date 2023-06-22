def lucky_ticket(ticket_number):
    number = [int(d) for d in str(ticket_number)]
    if len(number) != 6:
        return False
    left_sum = sum(number[:3])
    right_sum = sum(number[3:])
    return left_sum == right_sum

ticket_number = input("Введите номер билета: ")
if lucky_ticket(ticket_number):
    print("Счастливый билет!")
else:
    print("Обычный билет")