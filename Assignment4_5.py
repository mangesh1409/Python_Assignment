from functools import reduce;

def ChkPrime(no):
	
	if(no>1):
		for i in range(2,(no//2)+1,1):
			if(no%i==0):
				break;
		else:
			return True;
		
		
def Mul(no):
	
	return no*2;


def Max(no1,no2):
	
	if(no1>no2):
		Max=no1;
	else:
		Max=no2;
		
	return Max;
	

def Main():
	
	RawData=list();
	size=int(input('Enter number of elements   '));
	print('Enter',size,'elements');	
	
	for i in range(0,size,1):
		print('Enter',i+1,'element');
		no=int(input());
		RawData.append(no);
		
	print('Raw Data is');
	print(RawData);
	
	FilterData=list(filter(ChkPrime, RawData));
	print('Filtered Data is');
	print(FilterData);

	MapData=list(map(Mul,FilterData));
	print("Mapped Data is");
	print(MapData);

	if(len(MapData)>0):
		Result=int(reduce(Max,MapData));
		print('Reduced data is',Result);


if(__name__=="__main__"):
	Main();
