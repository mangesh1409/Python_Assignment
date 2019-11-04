def Frequency(no,length,num):
	
	count=0;
	
	for i in range(0,length,1):
		if(num==no[i]):
			count=count+1;
		
	return count;
	

def main():
	
	number=list();
	print('Enter number of elements');
	size=int(input());
	print('Enter' ,size, 'elements');
	
	for i in range(0,size,1):
		
		print('Enter',i+1,'element');
		no=int(input());
		number.append(no);
	
	print('Enter number to search');
	no=int(input());
	
	print(number);

	ret=Frequency(number,size,no);
	
	print('Frequency of',no,'is',ret);

if(__name__=="__main__"):
	main();
