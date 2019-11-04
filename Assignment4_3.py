from functools import reduce;

def MaxMin(no):
	
	if((no>=70)and(no<=90)):
		return True;

def Modify(no):
	
	return no+10;

def Mul(no1,no2):

	ans=no1*no2;
	
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
	
	FilterData=list(filter(MaxMin, RawData));
	print('Filtered Data is');
	print(FilterData);

	MapData=list(map(Modify,FilterData));
	print("Mapped Data is");
	print(MapData);

	if(len(MapData)>0):
		Result=int(reduce(Mul,MapData));
		print('Reduced data is',Result);



if(__name__=="__main__"):
	Main();
