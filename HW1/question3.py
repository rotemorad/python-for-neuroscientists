def is_palindrome(number, first_digit = 0, last_digit = None):
	"""Receives a number and converts it to string.
	   The parameters: first_digit and last_digit are the indexes for the first_digit and last_digit and default values are set for convenience.
	"""
	string = str(number)[first_digit:last_digit]
	return string == string[::-1]


def check_palindrome():
	"""Runs through all 6-digit numbers and checks the mentioned conditions.



	The function prints out the numbers that satisfy this condition.



	Notes

	-----

	It should print out the first number (with a palindrome in its last 4 digits),not all four "versions" of it.

	"""

	result = []
	for num in range(100000, 1000000):
		if (
				is_palindrome(num, 2) and
				is_palindrome(num + 1, 1) and
				is_palindrome(num + 2, 1, 5) and
				is_palindrome(num + 3)
		):
			result.append(num)
	return result
