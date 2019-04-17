year=input('please input yrear and press enter: ')
year=int(year)

if year%100!=0 and year%4==0:
	print(year,' is leap year')
elif year%100==0 and year%400==0:
	print(year,' is leap year')
else:
	print(year,' is not leap year')
