print("Проверка условия, a - четырехзначное и его цифры зеркально отражены")
a = int(input("Введите а: "))
while not 999 < a < 10000:
	a = int(input("Число должно быть четырехзначным. Введите а: "))
if (a%10 == a//1000%10) and (a//10%10 == a//100%10):
	print("True")
else:
	print("False")
