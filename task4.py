print("Проверка условия, a - трехзначное и его цифры составляют\nубывающую или возрастающую последовательность")
a = int(input("Введите а: "))
while not 99 < a < 1000:
	a = int(input("Число должно быть трехзначным. Введите а: "))
b = a%10
a = a//10
if b < a%10:
	b = a%10
	a = a//10
	if b < a % 10:
		print("True")
	else:
		print("False")
elif b > a%10:
	b = a%10
	a = a//10
	if b > a%10:
		print("True")
	else:
		print("False")
else:
	print("False")
