def calc(x):
    sum = 0
    y = len(x)

    for i in range(y):
        y = x[i]
        fpa = y[2]/100*y[1]
        sum = sum + y[1] + fpa

    print ("the payment sum is:", sum)
