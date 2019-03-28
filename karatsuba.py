   #method to multiply any two numbers other than grade school #Karatsuba Multiplication
   #This method is more efficient than grade school
def RecIntMult(FirstNum,SecondNum):
   #base case	 
	if len(str(FirstNum)) == 1 or len(str(SecondNum)) == 1:    
                return FirstNum * SecondNum
	else:
		n = max(len(str(FirstNum)),len(str(SecondNum)))
		k = n / 2
		
	        b = FirstNum % 10**(k)
                a = (FirstNum - b ) / 10**(k)
                d = SecondNum % 10**(k)
                c = (SecondNum - d ) / 10**(k)
		ac = RecIntMult(a,c)
		bd = RecIntMult(b,d)
		s = RecIntMult(a+b,c+d) - ac - bd             #ad_plus_bc = (a+b)(c+d) - ac - bd
        
        	
		Result = ac * 10**(2*k) + (s * 10**k) + bd

		return Result
print("Enter the number of test cases")
t=input()   #number of test cases
while t>0 :
                                                   # Now,enter the two numbers to be multiplied 
   m=input("Enter first number")
   n=input("Enter second number")
   r=RecIntMult(m,n)
   print('The multiplication of the numbers is =')
   print(r)
   t-=1
