#랜덤함수를 사용하기 위해서 라이브러리 가져옴
import random

#사용자의 입력이 범위 안인지 확인하는 플래그 변수
user_input_range = False

#사용자로부터 입력 받고 입력 받은 값의 범위를 확인해줌
user_input = int(input("Enter the number of dice rolls (between 100 and 1,000,000): "))
user_input_range = True if 100 <= user_input <= 1000000 else False #삼항연산자와 플래그 변수를 활용해 범위에 맞는 값인지 체크

#범위에 맞지 않는다면 맞을 때까지 반복 
while not user_input_range:
    print("Please enter a number within the specified range.")
    user_input = int(input("Enter the number of dice rolls (between 100 and 1,000,000): "))
    user_input_range = True if 100 <= user_input <= 1000000 else False

#몇 번 나왔는 지 카운트하기 위한 리스트 생성
count_num_list = [0, 0, 0, 0, 0, 0]

#주사위를 굴리고 어떤 면이 나왔는지 기록
for i in range(user_input):
    num = random.randint(1, 6)
    count_num_list[num - 1] += 1

# 가장 큰 값을 찾으며 저장하기 위한 변수
random_number_max = 0

#가장 큰 값을 "random_number_max"에 넣으면서 가장 큰 값을 찾음
for j in range(len(count_num_list)):
    random_number_max = count_num_list[j] if random_number_max < count_num_list[j] else random_number_max

#최종적으로 주사위의 히스토그램을 출력함
print("Dice Roll Frequency Histogram:")
for k in range(len(count_num_list)):
    star = int((count_num_list[k] / random_number_max) * 10)
    print(f"{k + 1}: {'*' * star} ({count_num_list[k]} times, {format((count_num_list[k] / user_input) * 100)}%)") #기록한 수치를 시각화 + 계산하여 사용자에게 보여줌