def trifeca(word):
	"""Checks whether word contains three consecutive double-letter pairs.

	Parameters
	----------
	word : string
		Input to check

	Returns
	-------
	result : bool
		True if three consecutive double-letter pairs were found,
		False otherwise
	"""

	for i in range(len(word) - 5):
		if word[i] == word[i + 1] and word[i + 2] == word[i + 3] and word[i + 4] == word[i + 5] and word[i]:
			return True
	return False
