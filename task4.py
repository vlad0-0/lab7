print("Проверка условия, a - трехзначное и его цифры составляют\nубывающую или возрастающую последовательность")
a = int(input())
while not 99 < a < 1000:
	a = int(input())
a = str(a)
if (int(a[0]) > int(a[1]) > int(a[2])) or (int(a[0]) < int(a[1]) < int(a[2])):
	print("True")
else:
	print("False")
