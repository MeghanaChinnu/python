lwrl=int(input("Enter the lower limit:"))
uprl=int(input("Enter the upper limit:"))

even=[]
for i in range(lwrl,uprl):
  if i%2==0:
    even.append(i)
    
print(even)
  
