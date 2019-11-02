def Factorial(no):
	fact=1;
	
	for i in range (1,no+1,1):
		fact=fact*i;
		
	return fact;
	
print("Enter number");
no=input();

ret=Factorial(no);

print(ret);
