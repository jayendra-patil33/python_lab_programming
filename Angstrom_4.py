# Jayendra Patil 
# roll no: 19, gr no: 11810706 
# To test for angstrom number 
# question: 4
num=int(input("Enter a number:"))
sum = 0
temp = num
while temp > 0:
    digit =temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"is an Angstrom number")
else:
    print(num,"is not an Angstrom number")


