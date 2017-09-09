second=int(input("please enter number of minutes :"))

year=second//(60*24*365)
second= second- year*60*24*365
month=second//(60*24)
print("number of years is :",year,"number of month is :",month )