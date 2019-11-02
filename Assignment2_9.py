def CountDigits(iNo):
	i=0;
		
	while(iNo>0):
		#iDigit=iNo%10;
		iNo=iNo/10;
		i=i+1;
		
	return i;
	
print("Enter number");
no=input();

ret=CountDigits(no);

print(ret);
