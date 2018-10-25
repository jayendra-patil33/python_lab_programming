# Jayendra Patil 
# roll no: 19, gr no: 11810706 
# To find fibonacci series
# question: 2
def fibo(n):
 if n == 1:
     return 1
 elif n == 0: 
     return 0 
 else: 
     return fibo(n-1) + fibo(n-2) 
a=int(input("enter the index of term you want to find: "))
print ("The number is :",fibo(a))


