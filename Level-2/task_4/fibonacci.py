num = int(input("Enter a number: "))
a = 0
b = 1
c = 0
print(a,b,end=" ")
while a+b <= num+1:
    c = a + b
    print(c,end=" ")
    a = b
    b = c

