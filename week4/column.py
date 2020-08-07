n = int(input("Enter a number: "))
if -6<n<2:
  col= list(range(n, n+42, 7))
print(*col, sep = " ")
