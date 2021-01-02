print("Print leap year between two given years")
print("Enter start year")
startYear = int(input())
print("Enter last year")
endYear=int(input())

print("List of leap years:")
for year in range(startYear,endYear):
 if((year%4==0)and(year%100!=0)or
    (year%400==0)):
     print(year)
