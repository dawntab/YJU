# 제곱미터를 평방피트로 변환하는 함수
def convert_to_square_feet(square_meters):
    # 1 제곱미터는 약 10.7639 평방피트
    result = square_meters * 10.7639
    return result

# 제곱미터를 에이커로 변환하는 함수
def convert_to_acres(square_meters):
    # 1 에이커는 약 4046.86 제곱미터
    result = square_meters / 4046.86
    return result

# 사용자로부터 제곱미터 단위의 토지 면적을 입력받음
square_meters = float(input("토지의 면적을 제곱미터(m²) 단위로 입력하세요: "))

# 입력된 면적이 음수인지 확인
if square_meters < 0:
    print("잘못된 입력입니다.")
else:
    # 제곱미터를 평방피트로 변환한 결과 출력
    print(f"{square_meters} 제곱미터는 {convert_to_square_feet(square_meters)} 평방피트입니다.")
    # 제곱미터를 에이커로 변환한 결과 출력
    print(f"{square_meters} 제곱미터는 {convert_to_acres(square_meters)} 에이커입니다.")