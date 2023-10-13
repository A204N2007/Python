#Input two numbers, Num1 and Num2
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))

#Sum of Num1 and Num2
sum = number1 + number2

#Difference of Num1 and Num2
difference = number1 - number2

#Product of Num1 and Num2
product = number1 * number2

#Quotient of Num1 and Num2
quotient = number1 / number2

#Power of Num1 and Num2
power = number1 ** number2

#Input third number, Num3
number3 = int(input("Enter a integer: "))

#Input product1 of num3 and sum
product1= number3 * sum

#Input product2 of num3 and sum
product2= number3 * difference

#Input power of sum and num3
power1= sum ** number3

print("The sum of the two numbers is", sum)
print("The difference of the two numbers is", difference)
print("The product of the two numbers is", product)
print("The quotient of the two numbers is", quotient)
print("The power of the two numbers is", power)
print("The product of the integer and the sum of the two numbers is", product1)
print("The product of the integer and the difference of# the two numbers is", product2)
print("The sum of the two numbers raised to the power of the integer is", power1)