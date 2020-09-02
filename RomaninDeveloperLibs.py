def calculate_whole_percentage(var, max_var):
	import math
	one_percentage = max_var/100
	not_whole_output = var/one_percentage
	whole_output = math.ceil(not_whole_output)
	if whole_output >= 100:
		output = 100
	else:
		output = whole_output
	return output