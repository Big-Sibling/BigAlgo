N, M = map(int,input().split())
A = []
B = []
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
C = []
for i in range(N):
    C_i = [A[i][j] + B[i][j] for j in range(M)]
    print(*C_i)
