lw = int(input("Enter lower range: "))
upr = int(input("Enter upper range: "))

print("Prime numbers between",lw,"and",upr,"are:")

for x in range(lw,upr+1):                                 
     if x>1:                     #prime nos are greater than 1
       for i in range(2,x):
           if ((x%i) == 0):
               break
       else:
           print(x)
