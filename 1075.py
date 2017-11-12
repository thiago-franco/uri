n = int(input())

for i in range(1, 10000+1):
    if i % n == 2:
        print(i)
    
#[print(i) for i in range(1,10001) if i % n == 2]
