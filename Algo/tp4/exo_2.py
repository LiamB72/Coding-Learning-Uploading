def calcul(x,coefficients):
	a,b=coefficients
	y=a*x+b
	return y

coefficients=(2,1)
print("La valeur de y pour x=2 est: y=",calcul(2,coefficients))
