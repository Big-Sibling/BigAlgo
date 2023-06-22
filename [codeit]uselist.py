numbers = []
print(numbers)
num_list = [1, 7, 3, 6, 5, 2, 13, 14]
count = 0
while count < len(num_list):
    numbers.append(num_list[count])
    count +=1
print(numbers)

# 홀수 : num_list[index] %2 == 1
count =0
while count <len(numbers):
    if numbers[count] %2 == 1:
        del numbers[count]

print(numbers)

numbers.insert(0, 20)
print(numbers)

numbers.sort()
print(numbers)
