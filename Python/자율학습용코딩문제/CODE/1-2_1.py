# 삼각형을 만들 수 있는지 여부를 나타내는 변수입니다. 초기값은 False입니다.
tri_able = False

# 첫 번째 변의 길이를 입력받습니다.
a = int(input("첫 번째 변의 길이를 입력하세요: "))
# 두 번째 변의 길이를 입력받습니다.
b = int(input("두 번째 변의 길이를 입력하세요: "))
# 세 번째 변의 길이를 입력받습니다.
c = int(input("세 번째 변의 길이를 입력하세요: "))

# 삼각형의 조건을 만족하는지 확인합니다.
if a + b > c and b + c > a and c + a > b:
    # 삼각형을 만들 수 있음을 나타내기 위해 tri_able 변수를 True로 설정합니다.
    tri_able = True
    # 세 변의 길이가 모두 같은 경우
    if a == b and b == c:
        tri_type = "정삼각형"
    # 두 변의 길이가 같은 경우
    elif a == b or b == c or c == a:
        tri_type = "이등변삼각형"
    # 세 변의 길이가 모두 다른 경우
    else:
        tri_type = "부등변삼각형"
# 삼각형의 조건을 만족하지 않는 경우
else:
    # 삼각형을 만들 수 없음을 나타내기 위해 tri_able 변수를 False로 설정합니다.
    tri_able = False

# tri_able 변수가 False인 경우
if not tri_able:
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.\n삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")
# tri_able 변수가 True인 경우
else:
    print(f"입력하신 변의 길이로는 {tri_type}을 만들 수 있습니다.")