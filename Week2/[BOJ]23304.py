input_lst = list(input())
# print(input_lst)
def is_palindrome(st):
    if len(st) == 1:
        return True
    total = len(st)
    mid = len(st) // 2
    for i in range(mid):
        if st[i] != st[total-1-i]:
            return False
    return True

def recurse(st,idx):
    # print(st)
    if len(st) == 1:
        return 1
    else:
        if is_palindrome(st) == False:
            return 0
        else:
            new_idx = idx // 2
            new_st = st[:new_idx]
            return recurse(new_st,new_idx)

result = recurse(input_lst,len(input_lst))
if result == 1:
    print("AKARAKA")
else:
    print("IPSELENTI")
