print("Проверка условия, a - трехзначное и его цифры составляют\nубывающую или возрастающую последовательность")
a = int(input("Введите а: "))
while not 99 < a < 1000:
	a = int(input("Число должно быть трехзначным. Введите а: "))
r1 = a%10
a = a//10
r2 = a%10
a = a//10
if (r1 > r2 > a) or (r1 < r2 < a):
	print("True")
else:
	print("False")
