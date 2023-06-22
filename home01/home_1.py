number = int(input("Введите трехзначное число: "))
number1 = 0

while number > 0:
    sum = number % 10
    number1 += sum
    number //= 10

print(f"Сумма цифр равна {number1}")