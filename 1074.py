n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        print("NULL")
    elif x > 0 and x % 2 == 0:
        print("EVEN POSITIVE")
    elif x < 0 and x % 2 == 0:
        print("EVEN NEGATIVE")
    elif x > 0 and x % 2 != 0:
        print("ODD POSITIVE")
    elif x < 0 and x % 2 != 0:
        print("ODD NEGATIVE")
