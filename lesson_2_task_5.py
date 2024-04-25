def month_to_season(number):
    if (number > 12) or (number < 1):
        print ("Такого месяца не существует")
    elif (number == 1) or (number == 2) or (number == 12):
        print ("Зима")
    elif (number == 3) or (number == 4) or (number == 5):
        print ("Весна")
    elif (number == 6) or (number == 7) or (number == 8):
        print ("Лето")
    elif (number == 9) or (number == 10) or (number == 11):
        print ("Осень")

month_to_season(2)