from math import sqrt,log,sin      #imported certain function's of the module(math) not entire module
num = float(input("Enter a number: "))   #taking input from user
res1 = sqrt(num)  #squareroot of the input given by user
res2 = log(num)   # Logarithm value of input given by user
res3 = sin(num)   # Sine value of input given by user
print(f"Squareroot: {res1}")
print(f"Logarithm: {res2}")
print(f"Sine: {res3}")