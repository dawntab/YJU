import sys

# 이벤트 코드가 유효한지 확인하는 함수
def event_code_check(code):
    # 유효한 이벤트 코드는 "E1", "E2", "E3"임
    return False if not code in ["E1", "E2", "E3"] else True
    
# 날짜가 유효한 범위 내에 있는지 확인하는 함수
def date_range(date):
    # 날짜는 1일부터 30일까지 유효함
    return False if not 1 <= date <= 30 else True

# 이벤트 E1에 대한 나이 제한을 확인하는 함수
def E1(age):
    # 이벤트 E1은 18세 이상만 참여 가능
    return False if not age >= 18 else True

# 이벤트 E2에 대한 날짜 조건을 확인하는 함수
def E2(date):
    # 이벤트 E2는 짝수 날짜에만 예약 가능
    return False if not date % 2 == 0 else True

# 이벤트 E3에 대한 나이 및 날짜 조건을 확인하는 함수
def E3(age, date):
    # 이벤트 E3은 16세 이상만 참여 가능
    age_check = False if not age >= 16 else True
    # 이벤트 E3은 7의 배수 날짜에만 예약 가능
    date_check = False if date % 7 != 0 else True
    return age_check, date_check

# 사용자로부터 나이를 입력 받음
age = int(input("나이를 입력하세요: "))
# 사용자로부터 이벤트 코드를 입력 받음
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
# 사용자로부터 원하는 예약 날짜를 입력 받음
date = int(input("원하는 예약 날짜를 입력하세요: "))

# 이벤트 코드와 날짜가 유효한지 확인
if event_code_check(event_code) and date_range(date) == True:
    # 이벤트 코드가 E1인 경우
    if event_code == "E1":
        # 나이 제한을 확인하고 예약 완료 여부 출력
        print("예약이 완료되었습니다!") if E1(age) else print("나이 제한으로 인해 예약할 수 없습니다.")
    # 이벤트 코드가 E2인 경우
    elif event_code == "E2":
        # 날짜 제한을 확인하고 예약 완료 여부 출력
        print("예약이 완료되었습니다!") if E2(date) else print("선택하신 날짜에는 예약할 수 없습니다.")
    # 이벤트 코드가 E3인 경우
    elif event_code == "E3":
        age_F, date_F = E3(age, date)

        # 나이와 날짜 조건을 모두 만족하는지 확인하고 예약 완료 여부 출력
        if age_F == True and date_F == True:
            print("예약이 완료되었습니다!")
        else:
            # 나이 조건만 불만족하는 경우
            if age_F == False and date_F == True:
                print("나이 제한으로 인해 예약할 수 없습니다.")
            # 날짜 조건만 불만족하는 경우
            elif date_F == False and age_F == True:
                print("선택하신 날짜에는 예약할 수 없습니다.")
            # 나이와 날짜 조건을 모두 불만족하는 경우
            else:
                print("나이 제한으로 인해 예약할 수 없습니다.\n선택하신 날짜에는 예약할 수 없습니다.")
# 입력된 이벤트 코드 또는 날짜가 유효하지 않은 경우
else:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    sys.exit()