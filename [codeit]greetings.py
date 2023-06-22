greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
# 순서대로 출력되어야 한다. 
# count = 0 선언 뒤 -> while조건문 언제까지? count < greetings.lenth 일때까지! 출력함

count = 0
while len(greetings) >count :
    print(greetings[count])
    count +=1