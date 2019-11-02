def DivFive(No):
	if(No%5==0):
		return True;
	else:
		return False;
		
print("Enter number");
x=input();

ret=DivFive(x);

print(ret);

