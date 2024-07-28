# Write a function that takes an integer n and returns a list of the first n Fibonacci numbers.

def fibonacci_of_n(n):
	if n <= 0:
		return []
	elif n == 1:
		return [0]
	elif n == 2:
		return [0, 1]

	ls = [0, 1]
	for i in range(2, n):
		next_num = ls[-1] + ls[-2]
		ls.append(next_num)

	return ls

res = fibonacci_of_n(5)
print(res)

res = fibonacci_of_n(10)
print(res)

res = fibonacci_of_n(15)
print(res)
