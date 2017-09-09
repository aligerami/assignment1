

subtotal =float(input("please enter the subtotal amount :"))
gratuity =float(input("please enter the gratuity amount :"))

result = subtotal + (gratuity*subtotal)/100
print("{0:.2f}".format(result))
