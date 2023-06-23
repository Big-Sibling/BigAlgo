numbers = [2, 3, 5, 7, 11, 13, 17, 19]
for i in range(len(numbers) //2):
    reversed_index = len(numbers)-numbers[i]-1
    numbers[i] = numbers[reversed_index]
    numbers[i], numbers[reversed_index] = numbers[reversed_index], numbers[i]

print("뒤집어진 리스트:" + str(numbers))

