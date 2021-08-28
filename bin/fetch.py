'''
	here is the initiation process of the program.
	we need to create ranges that request can send to glpi so we create
	a list with all ranges possible with the items_range and max_range options
	the user added to the config file
'''
def range_fetch(step, max_range, iterator, rest):
	# declare
	range_list = []
	begin = 0
	ending = 0
	# for loop:	iterate and append ranges to list
	for i in range(iterator):
		temp = ""
		ending += step
		temp = str(begin) + '-' + str(ending)
		range_list.append(temp)
		begin += step
	# if the modulo gave no rest
	if rest == 0:
		return range_list
	else:
		# appending the rest to our ranges list
		range_list.append(str(begin) + '-' + str(begin + rest))
		return range_list