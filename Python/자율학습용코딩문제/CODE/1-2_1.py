tri_able = False

a = int(input("첫 번째 변의 길이를 입력하세요: "))
b = int(input("두 번째 변의 길이를 입력하세요: "))
c = int(input("세 번째 변의 길이를 입력하세요: "))

if a + b > c and b + c > a and c + a > b:
    tri_able = True
    if a == b == c:
        tri_type = "정삼각형"
    elif a == b or b == c or c == a:
        tri_type = "이등변삼각형"
    else:
        tri_type = "부등변삼각형"
else:
    tri_able = False

if not tri_able:
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다.\n삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")
else:
    print(f"입력하신 변의 길이로는 {tri_type}을 만들 수 있습니다.")