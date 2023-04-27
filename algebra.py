

# applied algebra 
class graph_calcs:
	def calc_linear():
		pass

	def roc_linear():
		pass



	# determine polynomial degree
	def calc_polynom():
		pass

	def roc_polynom():
		pass




	def calc_exponential():
		pass

	def roc_exponential():
		pass




	def calc_logistic(t, l, y=1, k=0):
		"""
		
		input = calc_logistic(t, L, Y, K) 
		output = [t, logistic calculation]

		Calculates the rate of change between one
 		point in a logistics function. 


		function:
			   L
		f(t) =  --------------
	               1 + y*e^-k(x-x0)

		t = points of time
		L = supremom or curves maximum value
		k = logistic growth rate i.e steepness of curve
		e = eulers number used as constant
		y = eulers multiplier. defaults to one if none
		x = sigmoid midpoint
		"""

		e = float(2.718281828459045)

		y1 = l/(1+y*e**(k*t))
		y1 = round(y1, 6)

		return [t, y1]


	def roc_logistic(t1, t2, l, y=1, k=0):
		"""

		input = roc_logistic(t1, t2, L, Y=1, K=0)  
		output = [t1, t2, rate of change]

		Calculates average rate of change between two
 		points in a logistics function. 
		

		function:
			   L
		f(t) =  --------------
	               1 + y*e^-k(x-x0)

		t = points of time
		L = supremom or curves maximum value
		k = logistic growth rate i.e steepness of curve
		e = eulers number used as constant
		y = eulers multiplier. defaults to one if none
		x = sigmoid midpoint
		"""

		e = float(2.718281828459045)

		y1 = l/(1+y*e**(k*t1))
		y2 = l/(1+y*e**(k*t2))

		y1 = round(y1, 6)
		y2 = round(y2, 6)


		y_out = y2 - y1
		x_out = t2 - t1


		if x_out == 0:
			return [t1,t2,0]

		else:
			outcome = y_out / x_out
			return [t1,t2,outcome]




# applied statistics and probability 
# calculates the mean, median, mode, average and range interquartile range of a list of data
class spread_metrics:

	# average
	def mean(a):
		lst = 0
		alen = len(a)
		for i in a:
			lst += i

		mean = lst/len(a)
		return print(f'\noriginal list: {a}\nlist length: {alen}\nmean/avg of list: {mean}')

	# a = [1,2,8,4,5,6,7,3,13,60,34,12,33,45]
	# print(mean(a))





	def median(lst):
		# sort list
		lst.sort()

		llst = len(lst)
		
		# find middle
		half_lst = llst/2


		if half_lst % 2 == 0:
			half_lst = int(half_lst)
			half_lst2 = half_lst + 1
			median = lst[half_lst] + lst[half_lst2] / 2
			
			return f'original list sorted: {lst}\nlist length: {llst}\nmedian is: {median}'


		
		# if middle point is 2 objects, average them
		elif half_lst % 2 != 0:
			half_lst = round(half_lst)
			median = lst[half_lst]
			
			return f'original list sorted: {lst}\nlist length: {llst}\nmedian is: {median}'	

	# a = [1,2,8,4,5,6,7,3,13,60,34,12,33,45]
	# print(median(a))



	def mode():
		pass

	def listrange():
		pass

	def quartiles():
		pass

	def std_devi():
		pass


