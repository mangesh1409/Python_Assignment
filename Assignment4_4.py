from functools import reduce;

def ChkEven(no):
	
	if(no%2==0):
		return True;

def Squre(no):
	
	return no**2;

def Sum(no1,no2):

	ans=no1+no2;
	
	return ans;
	

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
	
	FilterData=list(filter(ChkEven, RawData));
	print('Filtered Data is');
	print(FilterData);
	
	MapData=list(map(Squre,FilterData));
	print("Mapped Data is");
	print(MapData);

	if(len(MapData)>0):
		Result=int(reduce(Sum,MapData));
		print('Reduced data is',Result);



if(__name__=="__main__"):
	Main();
