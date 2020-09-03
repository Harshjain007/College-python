"""
Wap to print sum of 1 to n
"""
n=int(input("Enter a number:"))
sum=0
while(n>=0):
 sum=sum+n
 n=n-1
print(sum)

print("Value using formula")

total = (n*((n+1)/2))
print(sum)
