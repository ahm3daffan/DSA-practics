n = 34
newdigit = 0
while n>0:
    
    digit = n%10
    newdigit = newdigit*10 + digit
    n= n//10
print(newdigit)

