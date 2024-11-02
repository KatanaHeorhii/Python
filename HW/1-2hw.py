name = input("Ваше ім'я:")
age = input("Ваш вік:")
print(f"Привіт {name}, тобі {age}")

age = int(input("Ваш вік:"))
if age >= 18:
  print("Вхід дозволено")
else:
  print("Вхід заборонено")



import random
number = random.randint(1, 10)
num = 3
for a in range(1, num + 1):
    g = int(input(f"Спроба {a}: Введіть число: "))
    if g == number:
        print("Ви вгадали")
        break
    elif g < number:
        print("Більше")
    else:
        print("Менше")
else:
    print("Ви програли")


a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))
for number in range(a, b + 1):
  print(number)


a1 = int(input("Введіть число: "))
for num in range(a1, 0, -1):
  if num % 2 == 0:
      print(num, " ")


n = int(input("Введіть число:"))
f = 1
for i in range(1,n+1):
  f *= i
print(f)