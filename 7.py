#Write a function in Python that determines whether a given number is a power of 2. A number is considered a power#of 2 if it can be expressed as 2^k, where k is a non-negative integer.

def is_power_of_two(n):
	return n > 0 and n & (n - 1) == 0

print(is_power_of_two(0))
print(is_power_of_two(1))
print(is_power_of_two(2))
print(is_power_of_two(3))
print(is_power_of_two(4))
print(is_power_of_two(5))
print(is_power_of_two(6))
print(is_power_of_two(7))
print(is_power_of_two(8))
print(is_power_of_two(9))
print(is_power_of_two(10))
