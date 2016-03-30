# Problem 0
def is_even(number):
	if number % 2 == 1:
		answer = "Odd"
	else:
		answer = "Even"
	return answer 
	
#Problem 1
def digits(number):
	answer = len(str(number))
	return answer 
	
#Problem 2 
def sum_digits(number):
	answer = 0 
	string = str(number)
	for item in list(string):
		new_number = int(item)
		answer += new_number
	return answer

#Problem 3 
def sum_less_ints(number):
	real_number = number
	number -= 1
	list = ["Value"] * number 
	print(list)
	numberList = []
	answer = 0 
	for item in list:
		real_number -= 1
		numberList.append(real_number)
	for value in numberList:
		answer += int(value)
	return answer 
	


		
	


