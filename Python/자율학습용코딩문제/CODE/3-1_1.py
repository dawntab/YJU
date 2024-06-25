import sys

def event_code_check(code):
    return False if not code in ["E1", "E2", "E3"] else True
    
def date_range(date):
     return False if not 1 <= date <= 30 else True

def E1(age):
    return False if not age >= 18 else True

def E2(date):
    return False if not date % 2 == 0 else True

def E3(age, date):
    age_check = False if not age >= 16 else True
    date_check = False if date % 7 != 0 else True
    return age_check, date_check

age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
date = int(input("원하는 예약 날짜를 입력하세요: "))

if event_code_check(event_code) and date_range(date) == True:
    if event_code == "E1":
        print("예약이 완료되었습니다!") if E1(age) else print("나이 제한으로 인해 예약할 수 없습니다.")
    elif event_code == "E2":
        print("예약이 완료되었습니다!") if E2(date) else print("선택하신 날짜에는 예약할 수 없습니다.")
    elif event_code =="E3":
        age_F, date_F = E3(age, date)

        if age_F == True and date_F == True:
            print("예약이 완료되었습니다!")
        else:
            if age_F == False and date_F == True:
                print("나이 제한으로 인해 예약할 수 없습니다.")
            elif date_F ==False and age_F == True:
                print("선택하신 날짜에는 예약할 수 없습니다.")
            else:
                print("나이 제한으로 인해 예약할 수 없습니다.\n선택하신 날짜에는 예약할 수 없습니다.")
else:
    print("잘못된 입력입니다. 프로그램을 종료합니다.")
    sys.exit()

