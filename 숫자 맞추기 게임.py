import random

n = random.randint(1, 10)
correct_answer = "정답"
while True:
    try:
        answer = int(input("1부터 10사이의 숫자를 추측해서 입력하세요: "))
        if not (1 <= answer <= 10):
            print("1부터 10사이의 숫자만 입력하시오.")
            continue
        break
    except ValueError:
        print("1부터 10사이의 정수만을 입력하시오.")
print(f"{answer}(을)를 입력하셨습니다.")
print("결과를 공개하겠습니다.")

if answer == n:
    print(f"{correct_answer}입니다.")
else:
    print(f"틀렸습니다, {correct_answer}(은)는 {n}입니다.")