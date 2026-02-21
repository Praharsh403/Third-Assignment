def factorial(n):
    if n == 1:         #condition1- where we know factorial of 1 is 1 as n!= n*(n-1)*... hence proving that condition
        return 1
    else:
        fact = n * factorial(n-1)  #factorial through recursion(function inside a function)
        return fact

number = int(input("Enter the number: "))
print(f"Factorial of number {number} is {factorial(number)} ")

#Similar factorial can be done also by other method:
#where we can take two values num and factorial using loop

""""def facto(num):
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial
print (facto(3))"""
