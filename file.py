num_w=0
w="this"
k=0
with open("/home/alekhya/file.txt","r") as f: 
    for line in f:
         words=line.split()
        for i in words:
            if(i==word):
	    k=k+1
print("occurances of the word")
print(k)
