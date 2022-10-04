number1 = int(input("Введіть два числа "))
number2 = int(input())
print("Усі числа кратні 7 -> ")
if number1< 7:
    number1+=7%number1
elif number1> 7:
    number1 = (number1 - (number1%7))+7

while number1 <= number2:
    print(number1, end =" ")
    number1 += 7