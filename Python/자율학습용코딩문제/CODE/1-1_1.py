# 나이를 입력받습니다.
age = int(input("사용자의 나이를 입력해주세요: "))

# 나이가 12세 이하인 경우
if age <= 12:
    # 어린이 이용권을 사용할 수 있다는 메시지를 출력합니다.
    print("어린이 이용권을 사용할 수 있습니다.")
# 나이가 19세 이상인 경우
elif age >= 19:
    # 성인 이용권을 사용할 수 있다는 메시지를 출력합니다.
    print("성인 이용권을 사용할 수 있습니다.")
# 나이가 13세 이상 18세 이하인 경우
else:
    # 청소년 이용권을 사용할 수 있다는 메시지를 출력합니다.
    print("청소년 이용권을 사용할 수 있습니다.")