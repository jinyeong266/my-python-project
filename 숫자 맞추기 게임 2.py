# 라이브러리
import random

#변수 선언
correct_answer = "정답"
right_answer = None

# 입력과 예외처리
while True:
    try:
        right_answer = random.randint(1, 31)
        guess = int(input("1에서 31사이의 정수를 입력하세요: "))
        if not (1 <= guess <= 31):
            print("1에서 31사이의 정수만을 입력하세요.")
            continue
        break
    except ValueError:
        print("알파벳과 특수문자등이 아닌 오직 정수만을 입력하실 수 있습니다.")

print(f"{guess}를 입력하셨습니다.")
print(f"{correct_answer} 을(를) 공개합니다.")

if right_answer == guess:
    print(f"{correct_answer}입니다.")
else:
    print(f"틀렸습니다, {correct_answer}은(는) {right_answer}입니다.")