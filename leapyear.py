year=int(input("enter the year"))
if(year%4==0 and year%100!=0) or (year%100==0 and year%400==0):
    print(" it is leap year")
else:
     print(" it not is leap year")
    
