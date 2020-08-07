hour= float(input("Enter the hours: "))
minutes= float(input("Enter the minutes: "))
seconds= float(input("Enter the seconds: "))

if 0<hour>23:
  print("Your time is invalid")

if 0<minutes>59:
  print("Your time is invalid")

if 0<seconds>59:
  print("Your time is invalid")

elif (hour,minutes,seconds):
  print("Your time is valid")