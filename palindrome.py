str=input('please enter any word: ')
rev_str=reversed(str)
if list(str)==list(rev_str):
	print('it is palindrome')
else:
	print('it is not palindrome')