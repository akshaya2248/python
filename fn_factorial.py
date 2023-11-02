
def factorial(n):
    if n==1:
        return 1
    else:
         return n*factorial(n - 1)
fact=int(input("enter the number to find the factorial:"))
fact=factorial(fact)    
print("the factorial of the given number:",fact)
    
