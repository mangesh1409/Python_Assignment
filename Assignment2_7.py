def Pattern(no):
	for i in range (1,no+1,1):
		for j in range (1,no+1,1):
			print(j),
		print("\n");
		
print("Enter number");
no=input();

Pattern(no);
