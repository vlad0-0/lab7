print("Проверка условия, a - четырехзначное и его цифры зеркально отражены")
a = int(input("Введите а: "))
while not 999 < a < 10000:
	a = int(input())
a = list(a)
if a == reversed(a):
	print("True")
else:
	print("False")
