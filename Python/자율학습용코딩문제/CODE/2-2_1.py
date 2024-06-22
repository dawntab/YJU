# 평균 점수와 학점을 계산하는 함수
def calculate(math, science, english):
    # 세 과목의 평균 점수 계산
    avg = (math + science + english) / 3
    
    # 평균 점수에 따른 학점 부여
    if avg >= 90:
        grade = "A"
    elif 90 > avg >= 80:
        grade = "B"
    elif 80 > avg >= 70:
        grade = "C"
    elif 70 > avg >= 60:
        grade = "D"
    else:
        grade = "F"

    # 평균 점수와 학점을 반환
    return avg, grade

# 사용자로부터 수학, 과학, 영어 점수를 입력받음
math = float(input("수학 점수를 입력하세요: "))
science = float(input("과학 점수를 입력하세요: "))
english = float(input("영어 점수를 입력하세요: "))

# 평균 점수와 학점을 계산
avg, grade = calculate(math, science, english)

# 평균 점수와 학점을 출력
print(f"평균 점수는 {avg}점이고, 학점은 {grade}입니다.")