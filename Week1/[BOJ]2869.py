# 값 받기
A, B, V = map(int,input().split())
res = 0
# 5 1 6 같은 케이스 생각해보자
if (V-A) % (A-B) != 0:
    res = 1
result = res + ((V-A) // (A-B)) + 1

print(result)