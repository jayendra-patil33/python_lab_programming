# Jayendra Patil 
# roll no: 19, gr no: 11810706 
# To check prime till a given number 
n=int(input())
for i in range(1,int(n)): 
    for j in range(2,(i+1)): 
        if i%j==0: 
           if i==j: 
            print(i) 
           break