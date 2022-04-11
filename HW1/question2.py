def compare_subjects_within_student(

		subj1_all_students,

		subj2_all_students

):
	"""Compare the two subjects with their students and print out the higher-graded subject for each student.



	Single-subject students shouldn't be printed.



	Parameters

	----------

	subj1_all_students: dict, subj2_all_students: dict

		Data structures which contain the grades of all students in a given subject.



	Notes

	-----

	Choice for the data structure of the function's arguments is up to you.



	Returns

	-------
	result: dict, {name: highest grade}
	A data structure with the name of the student and the corresponding subject.

	"""
	result = {}
	for name in subj1_all_students:
		if name in subj2_all_students:
			result[name] = max(subj1_all_students[name], subj2_all_students[name])
	return result
