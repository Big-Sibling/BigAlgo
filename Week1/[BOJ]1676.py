N = int(input())
def factorial(n):
    if(n==1):
        return 1
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
a = []
for i in str(factorial(N)):
    a.append(i)
a.reverse()
for i in range(len(a)):
    if a[i] != '0':
        print(i)
        break