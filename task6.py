print("Введите стороны треугольника. Проверка условия на наличие прямого угла в треугольнике.")
a = []
for i in range(3):
    a.append(float(input()))
a.sort()
if a[0]**2+a[1]**2 == a[2]**2:
    print("True")
else:
    print("False")
