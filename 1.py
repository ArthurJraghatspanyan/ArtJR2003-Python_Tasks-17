# Write a recursive function to flatten a list that may contain nested lists.

def flatten_list(nested_list):
	if not nested_list:
		return []
	if type(nested_list[0]) == list:
		return flatten_list(nested_list[0]) + flatten_list(nested_list[1:])
	else:
		return [nested_list[0]] + flatten_list(nested_list[1:])

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flattened = flatten_list(nested_list)
print(flattened)
