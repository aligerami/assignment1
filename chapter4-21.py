year=int(input("Enter year: (e.g. 2009): "))
month=int(input("Enter month: 1-12 : "))
day_of_month=int(input("Enter the day of the month: 1-31 : "))
days = [ 'Monday', 'Tuesday', 'Wednesday', 
         'Thursday', 'Friday','Saturday','Sunday']
year=2013
month=1
day_of_month=25

century=year//100
year_of_the_century=year%100
h=(day_of_month+((26*(month+1))//10)+year_of_the_century+(year_of_the_century//4)+(century//4)+(5*century))%7

print("Day of the week is ",days[h])