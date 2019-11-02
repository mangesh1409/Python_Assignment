def AddFactors(no):
	sum=0
	
	for i in range (1,no/2+1,1):
		if(no%i==0):
			sum=sum+i
		
	return sum;
	
print("Enter number");
no=input();

ret=AddFactors(no);

print(ret);
