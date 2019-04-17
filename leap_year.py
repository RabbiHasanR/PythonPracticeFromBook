year=input('Please input year and press enter: ')
year=int(year)
if year%4!=0:
	print(year,' is not leap year')
else:
	if year%100==0:
		if year%400==0:
			print(year,'is leap year')
		else:
			print(year,' is not leap year')
	else:
		print(year,'is leap year')

print('program terminated')