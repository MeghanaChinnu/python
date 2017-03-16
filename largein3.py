print("Enter the numbers")
a=input()
b=input()
c=input()

if (a>b) and (a>c):
 num= a
elif (b>a) and (b>c):
 num= b
else:
 num= c
print("The largest number is",num)
