a = int(input("Введите трехзначное число: "))

c = a % 10 + a // 100 + a // 10 % 10

print(f"Сумма цифр равна {c}")