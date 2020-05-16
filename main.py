# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
def avg(arr):
	return sum(arr) / len(arr)

# print(average([1, 5, 9]))
arr = [1,5,9]
result = avg(arr)
print(result)

# print(average(range(11)))
print(avg(range(11)))


	