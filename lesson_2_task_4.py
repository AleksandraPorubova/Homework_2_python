def fizz_buzz (n):
    for i in range (1, n):
        if (i % 3 == 0) and (i % 5 != 0):
            i = "Fizz"
        elif (i % 5 == 0) and (i % 3 != 0):
            i = "Buzz"
        elif (i % 3 == 0) and (i % 5 == 0):
            i = "FizzBuzz"
        print(i)

fizz_buzz(50)
