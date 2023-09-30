num=int(input("enter the number"))
factorial=1
if(num<0):
        print("the factorial doesnot exist in -ve number")
elif(num==0):       
        print("the factorial of zero is one")
else:
    for i in range(1,num+1):
         factorial=factorial*i
    print("the factorial is",factorial)
    
