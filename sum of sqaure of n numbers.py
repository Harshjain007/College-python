"""
Wap to print sum of sq. 1 to n
"""
n=int(input("Enter numbers till which sum of square to print:"))
sum=0
while(n>=0):
    sum=sum+(n*n)
    n=n-1
print("Sum of sq. of 1 to n:", sum)
