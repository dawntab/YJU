#랜덤함수를 사용하기 위해 라이브러리를 불러옴
import random

#빙고의 칸에 따라서 빙고가 된 횟수를 카운트하는 함수들 line 5 ~ line 39
def bingo_3(list):
    bingo_3_count = 0
    checklist = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(len(checklist)):
        a, b, c = checklist[i]
        if list[a] == list[b] == list[c]:
            bingo_3_count += 1
    return bingo_3_count

def bingo_4(list):
    bingo_4_count = 0
    checklist = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [0, 5, 10, 15], [3, 6, 9, 12]]
    for i in range(len(checklist)):
        a, b, c, d = checklist[i]
        if list[a] == list[b] == list[c] == list[d]:
            bingo_4_count += 1
    return bingo_4_count
        
def bingo_5(list):
    bingo_5_count = 0
    checklist = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], [0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]
    for i in range(len(checklist)):
        a, b, c, d, e = checklist[i]
        if list[a] == list[b] == list[c] == list[d] == list[e]:
            bingo_5_count += 1
    return bingo_5_count

def bingo_6(list):
    bingo_6_count = 0
    checklist = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35], [0, 6, 12, 18, 24, 30], [1, 7, 13, 19, 25, 31], [2, 8, 14, 20, 26, 32], [3, 9, 15, 21, 27, 33], [4, 10, 16, 22, 28, 34], [5, 11, 17, 23, 29, 25], [0, 7, 14, 21, 28, 35], [5, 10, 15, 20, 25, 30]]
    for i in range(len(checklist)):
        a, b, c, d, e, f = checklist[i]
        if list[a] == list[b] == list[c] == list[d] == list[e] == list[f]:
            bingo_6_count += 1
    return bingo_6_count
            
#유저가 입력한 값의 범위를 체크하기 위한 플래그 변수
user_input_range = False

#삼항연산자와 플래그 변수를 사용한 범위 계산
user_input = int(input("Enter the size of the bingo board (3 to 6): "))
user_input_range = True if 3 <= user_input <= 6 else False

#반복문, 삼항연산자, 플래그 변수를 사용해 사용자가 잘못 입력한 변수의 범위를 다시 입력 받음
while not user_input_range:
    print("Size must be between 4 and 6 Please try again.")
    user_input = int(input("Enter the size of the bingo board (3 to 6): "))
    user_input_range = True if 3 <= user_input <= 6 else False

#입력받은 칸 수를 통해 전체 칸의 수를 구함
bingo_board = user_input * user_input

#1부터 36까지 든 리스트와 랜덤 값이 들어갈 리스트 생성
number_list = [_ for _ in range(1, 37)]
random_list = []

#1에서 36이 랜덤한 순서로 들어간 리스트를 만드는 과정
for i in range(36):
    num = random.randint(0, len(number_list) - 1)
    random_list.append(number_list[num])
    number_list.remove(number_list[num])

#빙고에 들어갈 값을 넣을 리스트
bingo_list = []

#리스트에 랜덤한 값 추가
for j in range(bingo_board):
    bingo_list.append(random_list[j])

#어떤 수가 들어갔는지 체크하기 위해서 빙고판의 모양으로 만들어 출력함
line_count = 0

for k in range(len(bingo_list)):
    print(bingo_list[k], end=" ")
    line_count += 1
    if line_count == user_input:
        print()
        line_count = 0

#빙고를 맞추면서 몇 번 시도 했는지 기록할 변수와 몇 빙고가 되었는지 기록하는 변수 두 개 생성
bingo_try = 0
bingo_count = 0        

#빙고가 2줄보다 작지 않을 때까지 돌아가는 반복문
while bingo_count < 2:
    bingo_try += 1  #반복문의 반복 횟수 기록
    input("Press Enter to generate a random number: ") #생성 신호
    random_number = random.randint(1, 36) #1 부터 36까지 중에서 랜덤함 정수 하나 뽑기
    print(f"Random Number {bingo_try}: {random_number}") #현재 진행중인 정보 출력
    for h in range(len(bingo_list)): #랜덤으로 뽑은 정수가 리스트안에 있는지 체크
        if random_number == bingo_list[h]:
            bingo_list[h] = " *"     #있으면 "*"로 치환

    #위에 코드들 실행 후 빙고판이 어떻게 바뀌었는지 확인하기 위한 빙고판 출력
    for k in range(len(bingo_list)): 
        print(bingo_list[k], end=" ")
        line_count += 1
        if line_count == user_input:
            print()
            line_count = 0
            
    #위에 코드들을 실행 후 만들어진 빙고가 있는 지 체크하기 위해 함수를 호출해 확인
    if user_input == 3:
        bingo_count = bingo_3(bingo_list)
    elif user_input == 4:
        bingo_count = bingo_4(bingo_list)
    elif user_input == 5:
        bingo_count = bingo_5(bingo_list)
    else:
        bingo_count = bingo_6(bingo_list)

#두 줄이상의 빙고를 성공 했음을 출력
print("Congratulations! You've won the game with 2 or more bingos!")