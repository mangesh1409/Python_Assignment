def ChkPrime(no):
	if(no>1):
		for i in range (2,no/2+1,1):
			if(no%i==0):
				return False;
							
		return True;
	else:
		return False;
		
	
print("Enter number");
no=input();

ret=ChkPrime(no);

if(ret==True):

	print(no,"is prime number");

else:

	print(no,"is not prime number");

