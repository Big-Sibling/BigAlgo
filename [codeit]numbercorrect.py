import random

def guessing_game():
    answer = random.randint(1, 20)
    attempts = 4

    while attempts > 0:
        print(f"기회가 {attempts}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:")
        guess = int(input())

        if guess == answer:
            print(f"축하합니다. {4 - attempts + 1}번 만에 숫자를 맞히셨습니다.")
            return

        if guess < answer:
            print("Up")
        else:
            print("Down")

        attempts -= 1

    print(f"아쉽습니다. 정답은 {answer}입니다.")

guessing_game()


