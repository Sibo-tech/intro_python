Year = eval(input('Enter the first year: \n'))
sy = eval(input('Enter the second year: \n'))
week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

while Year < sy + 1:
    import math

    a = 5 * (math.fmod((Year - 1), 4))
    b = 4 * (math.fmod((Year - 1), 100))
    c = 6 * (math.fmod((Year - 1), 400))
    day = math.fmod((1 + a + b + c), 7)
    day = int(day)
    print("The 1st of January " + str(Year) + " falls on a " + str(week[day]) + ".")
    Year += 1