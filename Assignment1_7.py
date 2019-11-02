def DivFive(No):
	if(No%5==0):
		return True;
	else:
		return False;
		
print("Enter number");
x=input();

ret=DivFive(x);

if(ret==True):

	print("Divisibel by 5");

else:
	
	print("Not divisibel by 5");
