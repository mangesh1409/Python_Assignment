i=1;

def Pattern(no):
	
	global i;	
	if(i<=no):
		print(i,end=' ');
		i=i+1;
		Pattern(no);


def Main():
	no=int(input('Enter number '));
	Pattern(no);
	print("")


if(__name__=="__main__"):
	Main();
