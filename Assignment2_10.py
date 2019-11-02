def CountDigits(iNo):
	iSum=0;
		
	while(iNo>0):
		iDigit=iNo%10;
		iNo=iNo/10;
		iSum=iSum+iDigit;
		
	return iSum;
	
print("Enter number");
no=input();

ret=CountDigits(no);

print(ret);
