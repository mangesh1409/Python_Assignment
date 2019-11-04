def Largest(no,length):
	
	max=no[0];
		
	for i in range(0,length,1):
		if(max<no[i]):
			max=no[i];
		
	return max;
	

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

	ret=Largest(number,size);
	
	print('Largest number is',ret);

if(__name__=="__main__"):
	main();
