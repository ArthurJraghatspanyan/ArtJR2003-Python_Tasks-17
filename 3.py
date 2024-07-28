#Write a recursive function to check if a list is sorted in ascending order.

def sorted_or_notsorted(ls):
	if len(ls) <= 1:
		return True
	if ls[0] > ls[1]:
		return False
	return sorted_or_notsorted(ls[1:])

result1 = sorted_or_notsorted([1, 2, 3, 4, 5])
print(result1)

result2 = sorted_or_notsorted([1, 2, 3, 5, 4])
print(result2)
