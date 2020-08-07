month= input("Enter the month('January', ...,'December'): \n")

day= input("Enter the start day ('Monday, ..., 'Sunday'): \n")

if month in ["January", "March", "May", "July", "August", "October", "December"]:
    x = 31
elif month in ["February"]:
    x = 28
elif month in ["April","June","September","November"]:
    x = 30

DAY_OFF = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
off = DAY_OFF.index(day)

print(month)
print("Mo Tu We Th Fr Sa Su")

for i in range(off):
    print("  ", end=' ')

for i in range(x):
    print("%2d" % (i+1), end=' ')
    if (i + off) % 7 == 6:
      print()
print()
