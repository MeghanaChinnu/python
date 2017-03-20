num=int(input("Enter a number:"))
 
if num > 1: #prime no is always greater than one
  for i in range(2,num):
  	if ((num % i) == 0):
   		print (num,"is not a prime number")
   		break
  else:
  		print(num,"is a prime number")
       
# if input number is negative
# or equal to 1, it is not prime
else:
   	print (num,"is not a prime number")
