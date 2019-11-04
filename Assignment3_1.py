def Addition(no,length):
	
	sum=0;
	
	for i in range(0,length,1):
		sum=sum+no[i];
		
	return sum;
	

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

	ret=Addition(number,size);
	
	print('Addition is',ret);

if(__name__=="__main__"):
	main();
