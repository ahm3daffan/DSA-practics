n = 121
b = n
new = 0
while b>0:
    digit :int = b%10
    new = new*10+digit
    b = b//10
if n == new:
    print("true")
else:
    print("false")



