def sumNumber(number):
    number_as_string=str(number)
    sum=0
    for i in number_as_string:
        sum=sum+int(i)
    return sum

print(sumNumber(919191000123))