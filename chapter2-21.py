money=int(input("please enter your money amount : "))
interest = (0.05)/12
account_balance_after_six_month=0
print()

temp=6
while temp>0:
    temp=temp-1
    account_balance_after_six_month=(account_balance_after_six_month+money)*(1+interest)
    
print(" account balance is : ","{0:.2f}".format(account_balance_after_six_month))

        