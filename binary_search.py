def binary_search(objective, epsilon = 0.00001):
	"""	Function to apply the binary search to a square root operation in a number

	:param objective: Number you want to know the square root
	:type objective: float
	:param epsilon: Precision that would have the method
	:type epsilon: float
	"""
	lower_limit = 0.0
	upper_limit = max(1.0, objective)
	answer = (upper_limit + lower_limit) / 2

	while abs(answer ** 2 - objective) >= epsilon:
		if answer ** 2 < objective:
			lower_limit = answer
		else:
			upper_limit = answer
		answer = (upper_limit + lower_limit) / 2

	print(f'The square root of {objective} is {answer}')



def run():
	number = float(input('Please enter a number: '))
	binary_search(number)


if __name__ == '__main__':
	run()