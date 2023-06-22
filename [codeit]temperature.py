def fahrenheit_to_celsius(fahrenheit) :
    return format((fahrenheit-32) * 5 /9)

fahrenheit_list = [40, 15, 32, 64, -4, 11]

count = 0
print("화씨 온도 리스트 : {}".format(fahrenheit_list))
#선언 함수 호출 
while count <len(fahrenheit_list):
    print(fahrenheit_to_celsius(fahrenheit_list[count]))
    count +=1

