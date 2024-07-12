def cal(hours_per_week, absence_hours, tardy_count):
    total = hours_per_week * 15
    total_div = total / 4
    absence_hours = absence_hours + int(tardy_count % 3)
    if  absence_hours > total_div:
        return "F (학점 미부여)"
    else:
        return round((20 - (20 * absence_hours / total)), 2)

hours_per_week = int(input("주당 수업 시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))

receive = cal(hours_per_week, absence_hours, tardy_count)

print(f"당신의 출석 점수는 {receive}점입니다.")