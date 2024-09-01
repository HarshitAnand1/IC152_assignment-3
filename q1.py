# Part a
import math

n = 15.3245

a = math.ceil(n)
print(a)

b = math.floor(n)
print(b)

c = round(n)
print(c)

d = type(round(n))
print(d)

e = format(n,"2f")
print(e)

f = type(format(n))
print(f)

avg = (a + b + c)/3
print(avg)


# Part b
input_str = input("Enter a string: ")
print(input_str.isalpha())
print(input_str.isnumeric())
print(input_str.isalnum())
print(input_str.isspace())
