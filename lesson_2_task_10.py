def bank (x, y):
    for i in range (y):
        x = (0.1 * x) + x
    return x

a = bank (10000, 5)
print (a)

