# Write a function that takes three numbers as input and returns the maximum of the three.

def maximum(a, b, c):
	if a > b and a > c:
		return a
	elif b > a and b > c:
		return b
	return c

a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))
c = int(input("Please enter third number: "))

result = maximum(a, b, c)
print(result)
