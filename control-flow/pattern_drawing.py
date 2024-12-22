rows = int(input("Enter the size of the pattern: "))

col = 0
while col != rows:
    col = col + 1
    for i in range(1, rows + 1):
        print("*", end="")
    print()
        
