from MarvellousNum import *;

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

	ret=ChkPrime(number,size);
	
	print('Addition of prime number is',ret);

if(__name__=="__main__"):
	main();
