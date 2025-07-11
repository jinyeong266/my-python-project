import random

n = random.randint(1, 31)

for attempt in range(7):
    try:
        guess = int(input(f"{attempt + 1}번째 시도: 1부터 31사이의 수를 입력하세요: "))
        if not(1 <= guess <= 31):
            print("범위에 맞게 입력하세요.")
            continue
    except ValueError:
        print("범위 내의 정수만 입력하세요.")
        continue
    if n == guess:
        print("정답입니다.")
        break
    else:
        print("틀렸습니다.")
else:
    print(f"아쉽네요. 정답은 {n}이었습니다.")
