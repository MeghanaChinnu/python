n = int(input("\n   Enter the number to find the table:"))
limit = int(input("\n   Enter limit:")) 
i = 1
for i in range(1,(limit+1)) :
    print("\n\t" + str(n) + "*" + str(i)+"="+str((n*i)))
