def number_sum(numbers):
	result=0
	for number in numbers:
		result+=number
	average=result/len(numbers)
	return average

avg=number_sum([1,2,30,4,5,9])
print(avg)