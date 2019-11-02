def Pattern(no):
	for i in range (no,0,-1):
		for j in range (0,i,1):
			print("* "),
		print("\n");
		
print("Enter number");
no=input();

Pattern(no);
