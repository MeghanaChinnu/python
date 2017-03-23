lwrl=int(input("Enter the lower limit:"))
uprl=int(input("Enter the upper limit:"))

odd=[]
for i in range(lwrl,uprl):
  if i%2==1:
    odd.append(i)
    
print(odd)
