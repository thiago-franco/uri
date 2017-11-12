X = input().split()
A = int(X[0])
B = int(X[1])
C = int(X[2])
D = int(X[3])
if B > C and D > A and C+D > A+B and C*D > 0 and A%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
        
    
