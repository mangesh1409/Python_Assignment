def Pattern(no):
	
	if(no>0):
		print(no,end=' ');
		no=no-1;
		Pattern(no);


def Main():
	no=int(input('Enter number '));
	Pattern(no);
	print("");


if(__name__=="__main__"):
	Main();
