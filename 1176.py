t = int(input())
for i in range(t):
    n = int(input())
    if n == 0:
        print("Fib(0) = 0")
    elif n == 1:
        print("Fib(1) = 1")
    else:
        a = 0
        b = 1
        f = 1
        i = 2
        while i < n:
            a = b
            b = f
            f = a + b
            i += 1
        print("Fib(%d) = %d" % (n,f))
