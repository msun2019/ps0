# Problem 0
def is_even(number):
	if number % 2 == 1:
		answer = "False"
	else:
		answer = "True"
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
	numberList = []
	answer = 0 
	for item in list:
		real_number -= 1
		numberList.append(real_number)
	for value in numberList:
		answer += int(value)
	return answer 
	
#Problem 4
def factorial(number):
	list = ["Value"] * number
	numberList = []
	answer = 1
	for item in list:
		numberList.append(number)
		number -= 1
	for value in numberList:
		answer *= int(value)
	return answer 

#Problem 5
def factor(x, y):
	if x % y == 0:
		answer = "True"
	else:
		answer = "False"
	return answer 

#Problem 6
def test_prime(number):
	root = number ** .5
	list = range(2, int(root) + 1)
	answer = " "
	for item in list:
		if number % int(item) == 0:
			answer = "Not Prime"
			break 
		if number % int(item) > 0:
			answer = "Prime"
	if number == 2:
		answer = "Prime"
	if number == 1:
		answer = "Not Prime"
	return answer
	
#Problem 7
def perfect(number):
	list = range(1, number)
	number_list = []
	value = 0
	for item in list:
		if number % item == 0:
			number_list.append(item)
	for item in number_list:
		value += item 
	if value == number:
		answer = "Perfect Number"
	else:
		answer = "Not a Perfect Number"
	return answer
	
#Problem 8 
def sum_digits_divide(number):
	if number % sum_digits(number) == 0:
		answer = "True"
	else:
		answer = "False"
	return answer



















		
	


