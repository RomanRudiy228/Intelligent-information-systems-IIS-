#1 Факторіал числа, яке вводить користувач
num = int(input("Введіть число: "))
factorial = 1

if num < 0:
    print("Факторіал визначений тільки для не від'ємних чисел.")
elif num == 0:
    print("Факторіал числа 0 = 1.")
else:

    for i in range(1, num + 1): 
        factorial *= i


    print(f"Факторіал числа {num} = {factorial}") 

#2 Обчислення суми усіх елементів у списку 
nums = input("Введіть елементи списку, розділені пробілами: ")

elements = nums.split() 

sum = 0 

for element in elements:
    sum += int(element)

print(f"Сума всіх елементів у списку: {sum}")  