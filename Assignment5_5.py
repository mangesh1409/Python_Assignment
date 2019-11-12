fact=1;

def Factorial(no):
	
	global fact;
	if(no>0):
		fact=fact*no;
		no=no-1;
		Factorial(no);
	
	return fact;

def Main():
	no=int(input('Enter number '));
	ret=Factorial(no);
	print('Factorial of',no,'is',ret);
	

if(__name__=="__main__"):
	Main();
