n = int(input())
def count(n):
    cnt = 0
    while n !=0:
         n //=5
         cnt += 5
    return cnt

print(count(n))
