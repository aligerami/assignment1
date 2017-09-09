tuition=10000
rate=5/100

for i in range (0,10):
    tuition=tuition*(1+rate)

print("{:0.2f}".format(tuition))