# Write a recursive function to calculate the sum of all elements in a list.

def summary_of_elements(ls):
	if not ls:
		return 0
	return ls[0] + summary_of_elements(ls[1:])

result = summary_of_elements([1, 2, 3, 4, 5])

print(result)
