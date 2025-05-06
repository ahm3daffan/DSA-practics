sum = 0 
n = 25
while n>0:
    b = n%10
    sum = sum + (b*b*b)
    n = n//10
print(sum)