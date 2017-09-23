today=int(input("Enter today's day:"))
number_of_elapse_day=int(input("Enter the number of days elapsed since today :"))

future_day=(today+number_of_elapse_day)%7

def get_Day_by_number(day):
  
    if(day==1):
        return "Monday"
    elif(day==2):
        return "Tuesday"
    elif(day==3):
        return "Wednesday"
    elif(day==4):
        return "Thursday"
    elif(day==5):
        return "Friday"
    elif( day==6):
        return "Saturday"
    elif(day==7):
        return "Sunday"

print("Today is ",get_Day_by_number(today)," and future day is ", get_Day_by_number(future_day))
    