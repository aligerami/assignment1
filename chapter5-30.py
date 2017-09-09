import calendar
year=int(input("Enter the year :"))
first_day_of_year=int(input("Day on January 1 "+str(year)+" is:"))

months_lenght=[ 31,28,31,30,31,30,31,31,30,30,31] 
months=["January","February","March","April","May","June","July","August","September","October","December"]
week_day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

if calendar.isleap(year):
    months_lenght[1]=29
print("\n")  
print('{:12}'.format("1-"+months[0]),", ",str(year)," is ",week_day[first_day_of_year])        
passed_days=0
for i in range (1,11):
    passed_days=passed_days+months_lenght[i-1]
    print('{:12}'.format(str(i+1)+"-"+months[i]),", ",str(year)," is ",week_day[(passed_days+1+first_day_of_year)%7])        
    