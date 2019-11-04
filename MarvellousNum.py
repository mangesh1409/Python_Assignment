def ChkPrime(no,length):
	add=0;

	for i in range(0,length,1):
		num=no[i];
		if(num>1):
			for j in range(2,(num//2)+1,1):
				if(num%j==0):
					break;
		
			else:
					add=add+num;
			
	return add;
