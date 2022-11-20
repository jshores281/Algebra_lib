


class functions:



	def calc_linear():
		pass

	def roc_linear():
		pass



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
















