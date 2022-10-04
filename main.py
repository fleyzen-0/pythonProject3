number1 = int(input("Введіть два числа "))
number2 = int(input())
print("Якщо число кратне 3 -> ")
if number1< 3:
    number1+=3%number1
elif number1> 3:
    number1 = (number1 - (number1%3))+3

if number1 <= number2:
    print(end ="Fizz ")
    number1 += 3

number1 = int(input("Введіть два числа "))
number2 = int(input())
print("Якщо число кратне 5 -> ")
if number1< 5:
    number1+=5%number1
elif number1> 5:
    number1 = (number1 - (number1%5))+5

if number1 <= number2:
    print(end ="Buzz")
    number1 += 5

## По іншому не знаю як ._.