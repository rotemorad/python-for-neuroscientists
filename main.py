from question1 import trifeca
from question2 import compare_subjects_within_student
from question3 import check_palindrome

##############

# Question 1 #

##############


inputs = [

	'aabbcc',

	'abccddee0123',

	'llkkbmm',

	'aaaazz',

	'bbcCdd',

]

for inp in inputs:
	print(trifeca(inp))

##############

# Question 2 #

##############
subj1 = {'Rotem': 100, 'Ina': 70, 'Oren': 80, 'Inbar': 90, 'Lotem': 98}
subj2 = {'Rotem': 99, 'Ina': 65, 'Oren': 80, 'Inbar': 100}

print(compare_subjects_within_student(subj1, subj2))

##############

# Question 3 #

##############

print(check_palindrome())
