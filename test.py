import random
def monte_carlo(n):
	t=0
	for i in range(n):
		(x,y)=(random.random(),random.random())
		a=((x**2)+(y**2))**0.5
		if a<=1:
			t=t+1
	b=4*(t/n)
	return(b)
print(monte_carlo(123456))
