def Main():
	
	no1=int(input('Enter 1st number  '));
	no2=int(input('Enter 2nd number  '));
	
	ret=lambda no1,no2: no1*no2;
	
	print(ret(no1,no2));

if(__name__=="__main__"):
	Main();
