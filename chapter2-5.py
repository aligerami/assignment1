

subtotal =float(input("please enter the subtotal amount :"))
gratuity =float(input("please enter the gratuity amount :"))
print("")
result = subtotal + (gratuity*subtotal)/100
print("The gratuaity is", "{0:.2f}".format((gratuity*subtotal)/100 ), " and the total amount is","{0:.2f}".format(result))
