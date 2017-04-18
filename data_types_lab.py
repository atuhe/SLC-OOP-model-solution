def data_type(arg):
	if not arg:
		return 'no value'
	if isinstance(arg, str):
		return len(arg)
	if isinstance(arg, bool):
		return arg
	if isinstance(arg, int):
		if arg > 100:
			return 'more than 100'
		elif arg < 100:
			return 'less than 100'
		else:
			return 'equal to 100'
	if isinstance(arg, list):
		try:
			if arg[2]:
				return arg[2]
		except:
			return None


#print data_type([1])

