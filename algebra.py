




class algebra:
	def add(x, y):
		"""
		Simple addition test
		"""

		outcome = x + y
		return outcome


	def roc_logi(t1, t2):
		"""

		Allows the calculations of the rate of change between two 
		points of time in a logistics function. 
		
		The roc_logi(t1, t2) is used for known points of time. 
		   t1 = first point, t2 = second point. 

		function:
			   L
		f(x) =  --------------
	               1 + 1e^-k(x - x0)

		L = supremom or curves maximum value
		k = logistic growth rate i.e steepness of curve
		e = eulers number used as constant
		x = sigmoid midpoint

		
		These variables are prompted after time is added to roc_logi parameters.

		"""
		l = float(input("ENTER max curve:  "))
		y = float(input("ENTER euler's multiplier, 1 if none: "))
		k = float(input("ENTER curves midpoint: "))
		e = float(2.71828)

		y1 = l/(1+y*2.71828**(-k*t1))
		y2 = l/(1+y*2.71828**(-k*t2))

		y_out = y2 - y1
		x_out = t2 - t1

		outcome = y_out / x_out

		return outcome













