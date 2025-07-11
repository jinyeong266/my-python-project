while True:
    try:
        num = int(input("구구단을 출력할 2~9 사이의 수를 입력하세요: "))
        if not (2 <= num <= 9):
            print("구구단 범위 내의 수를 입력하세요.")
            continue
    except ValueError:
        print("2에서 9사이의 정수만 입력하세요.")
        continue
    break
for i in range(2, 10):
    print(f"{num} * {i} = {num * i}")