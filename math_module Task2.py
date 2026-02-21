from math import sqrt,log,sin      #imported certain function's of the module(math) not entire module
num = float(input("Enter a number: "))   #taking input from user
if num <= 0:
    print("Enter a number greater than zero to calculate Logarithm value")
else:
    res1 = sqrt(num)
    res2 = log(num)
    res3 = sin(num)
    print(f"Square root of {num} is {res1}")
    print(f"Logarithm of {num} is {res2}")
    print(f"Sine of {num} is {res3}")

print("Thank you!!")


