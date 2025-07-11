try:
    num = int(input("구구단을 출력할 수를 입력하시오: ")) 
except ValueError:
    print("정수만 입력해주세요.")
else:
    print(f"{num}단을 입력하셨습니다.")
finally:
    print("구구단 출력을 실행합니다.")

if num is not None:
    for i in range(2, 10):
        print(f"{num} * {i} = {num * i}")