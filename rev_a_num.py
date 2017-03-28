n=int(input("Enter the number: "))
r=0
while(n>0):
  rm=n%10
  r=(r*10)+rm
  n=n//10
 
print("\nReverse of the number is = %d" %r)
