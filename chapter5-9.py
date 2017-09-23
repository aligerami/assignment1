tuition=10000
rate=5/100

for i in range (0,10):
    tuition=tuition*(1+rate)
sum=0
for i in range (0,4):
    tuition=tuition*(1+rate)
    sum+=tuition    


print("Tuition after 10 years is :" "{:0.2f}".format(tuition))
print("Sum of tuition from 11th years to 14th is" ,"{:0.2f}".format(sum))
