N = int(input())
result = 0 
while N>=0:
    if(N%5==0):
        result += N//5
        break
    elif N == 1 or N ==2:
        result = -1
        break
    else:
        N -= 3
        result += 1
print(result)