sum=0;

def DigitAdd(no):
	
	global sum;
	if(no!=0):
		digit=int(no%10);
		sum=sum+digit;
		no=int(no/10)
		DigitAdd(no);
	
	
	return sum;

def Main():
	no=int(input('Enter number '));
	ret=DigitAdd(no);
	print('Additionof digit is',ret);
	

if(__name__=="__main__"):
	Main();
