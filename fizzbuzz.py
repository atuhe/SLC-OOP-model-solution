def fizz_buzz(arg):
	if arg % 5 == 0 and arg % 3 == 0: return 'FizzBuzz'
	if arg % 3 == 0: return 'Fizz'
	if arg % 5 == 0: return 'Buzz'
	else:
		return arg
	
#print (fizz_buzz(15))