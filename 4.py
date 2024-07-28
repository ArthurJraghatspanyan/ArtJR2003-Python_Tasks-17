# Write a function that takes an integer as input and returns True if the number is prime, False otherwise.

def is_prime(n):
	if n == 0 and n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

result = is_prime(6)
print(result)

result = is_prime(17)
print(result)
