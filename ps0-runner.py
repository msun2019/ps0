import ps0
#Problem 0
print("\n") * 20
print("Problem 0:")
print("Is 2 even?")
print(ps0.is_even(2))
print("Is 5 even?")
print(ps0.is_even(5))
advance1 = raw_input("Type 'Y' to move on to the next problem ")
if advance1 == "Y" or advance1 == "y":
	print("\n") * 20
	print("Problem 1:")
	print("128 has {} digits in it. ".format(ps0.digits(128)))
	print("12345 has {} digits in it. ".format(ps0.digits(12345)))
	advance2 = raw_input("Type 'Y' to move on to the next problem ")
	if advance2 == "Y" or advance2 == "y":
		print("\n") * 20
		print("Problem 2:")
		print("The sum of the digits of 999 are:")
		print(ps0.sum_digits(999))
		print("The sum of the digits of 360 are:")
		print(ps0.sum_digits(360))
		advance3 = raw_input("Type 'Y' to move on to the next problem ")
		if advance3 == "Y" or advance3 == "y":
			print('\n') * 20
			print("Problem 3:")
			print("The sum of the numbers that are less than 9 are: ")
			print(ps0.sum_less_ints(9))
			print("The sum of the numbers that are less than 4 are: ")
			print(ps0.sum_less_ints(4))
			advance4 = raw_input("Type 'Y' to move on to the next problem ")
			if advance4 == "Y" or advance4 == "y":
				print('\n') * 20
				print("Problem 4: ")
				print("The factorial of 5 is: ")
				print(ps0.factorial(5))
				print("The factorial of 3 is: ")
				print(ps0.factorial(3))
				advance5 = raw_input("Type 'Y' to move on to the next problem ")
				if advance5 == "Y" or advance5 == "y":
					print('\n') * 20
					print("Problem 5:")
					print("Does 5 divide perfectly into 10?")
					print(ps0.factor(10, 5))
					print("Does 3 divide perfectly into 41?")
					print(ps0.factor(41, 3))
					advance6 = raw_input("Type 'Y' to move on to the next problem ")
					if advance6 == "Y" or advance6 == "y":
						print('\n') * 20
						print('Problem 6:')
						print("10 is a {} number.".format(ps0.test_prime(10)))
						print("5 is a {} number.".format(ps0.test_prime(5)))
						advance7 = raw_input("Type 'Y' to move on to the next problem ")
						if advance7 == "Y" or advance7 == "y":
							print('\n') * 20
							print('Problem 7')
							print('6 is a {}'.format(ps0.perfect(6)))
							print('43 is {}'.format(ps0.perfect(43)))
							advance8 = raw_input("Type 'Y' to move on to the next problem ")
							if advance8 == "Y" or advance8 == "y":
								print('\n') * 20
								print('Problem 8')
								print('Is the sum of the number 18 a perfect divisor of itself?')
								print(ps0.sum_digits_divide(18))
								print('Is the sum of the number 32 a perfect divisor of itself?')
								print(ps0.sum_digits_divide(32))
