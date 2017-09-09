employee_name="Smit"
hours=10 
hourly_per_rate=9.75
federal_tax_withholding_rate=0.20
state_tax_withholding_rate=0.09

employee_name=input("Please enter employee's name : ")
hours=int(input("Please enter number of hours worked in a week : "))
hourly_per_rate=float(input("Please enter hourly per rate : "))
federal_tax_withholding_rate=float(input("Please enter federal tax withholding rate : "))
state_tax_withholding_rate=float(input("Please enter state tax withholding rate : "))

gross_pay=hours*hourly_per_rate
print("Employee Name :" +employee_name)
print("Hours Worked :$",hours)
print("Pay Rate :$",hourly_per_rate)
print("Gross Pay :$",gross_pay)
print("Deductions :")
print(" \t Federal Withholding (","{0:.2f}".format(federal_tax_withholding_rate*100),"): $",
      "{0:.1f}".format((gross_pay*federal_tax_withholding_rate)))
print(" \t State Withholding (","{0:.2f}".format(state_tax_withholding_rate*100),"): $",
      "{0:.1f}".format((gross_pay*state_tax_withholding_rate)))
print("\t Total Deduction:","{0:.2f}".format(gross_pay*state_tax_withholding_rate+gross_pay*federal_tax_withholding_rate))
print("Net Pay:","{0:.2f}".format(gross_pay-(gross_pay*state_tax_withholding_rate+gross_pay*federal_tax_withholding_rate)))