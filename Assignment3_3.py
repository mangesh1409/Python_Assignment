def Smallest(no,length):
	
	minn=no[0];
		
	for i in range(0,length,1):
		if(minn>no[i]):
			minn=no[i];
		
	return minn;
	

def main():
	
	number=list();
	print('Enter number of elements');
	size=int(input());
	print('Enter' ,size, 'elements');
	
	for i in range(0,size,1):
		
		print('Enter',i+1,'element');
		no=int(input());
		number.append(no);
		
	print(number);

	ret=Smallest(number,size);
	
	print('Smallest number is',ret);

if(__name__=="__main__"):
	main();
