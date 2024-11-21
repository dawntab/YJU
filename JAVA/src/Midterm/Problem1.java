package Midterm;

import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //게임을 실행하기 전에 필요한 변수 선언
        boolean game = true;
        int round = 1;
        int score = 0;

        //게임 시작
        while (game) {
            System.out.println(round + "번째 게임");
            round ++;
            System.out.print("게임을 시작하려면 아무 값이나 입력하세요: ");
            sc.nextLine();

            //+, -, * 를 포함하는 배열
            char arr[] =  {'+', '-', '*'};
            char save[] = {' ', ' ', ' '};

            //랜덤으로 +, -, * 중 하나를 save에 저장 (3번 반복)
            for (int i = 0; i < 3; i++) {
                int r = (int)(Math.random() * 3);
                save[i] = arr[r];
            }

            //랜덤하게 저장된 결과 출력
            System.out.println("--------------------------------");
            for (int i = 0; i < 3; i++) {
                System.out.print("     " + save[i] + " :    ");
            }
            System.out.println();
            System.out.println("--------------------------------");

            //+, -, * 의 갯수를 저장할 변수 선언
            int p = 0;
            int m = 0;
            int g = 0;

            char OneArr = save[0];
            char TwoArr = save[1];
            char ThreeArr = save[2];

            //각 부호의 객수 측정
            for (int i = 0; i < 3; i++) {
                if (save[i] == '+') {
                    p++;
                }
                else if (save[i] == '-') {
                    m++;
                }
                else {
                    g++;
                }
            }
            //같은 기호 2개가 있는 지 확인 후 있으면 그거에 따른 점수 조정
            if (p == 2 || m == 2 || g == 2) {
                if (p == 2) {
                    if (OneArr == TwoArr || TwoArr == ThreeArr) {
                        System.out.println("+ 2 Combo - 보너스 점수 1점 획득");
                        score += 1;
                    }
                }
                else if (m == 2) {
                    if (OneArr == TwoArr || TwoArr == ThreeArr) {
                        System.out.println("- 2 Combo - 보너스 점수 1점 감소");
                        score -= 1;
                    }

                }
                else {
                    if (OneArr == TwoArr || TwoArr == ThreeArr) {
                        System.out.println("* 2 Combo - 보너스 점수 2점 획득");
                        score += 2;
                    }
                }
            }

            //같은 기호 3개가 있는 지 확인 후 있으면 그거에 따른 점수 조정
            if (p == 3 || m == 3 || g == 3) {
                if (p == 3) {
                    System.out.println("+ 3 Combo - 보너스 점수 3점 획득");
                    score += 3;
                }
                else if (m == 3) {
                    System.out.println("- 3 Combo - 보너스 점수 3점 감점");
                    score -= 3;
                }
                else {
                    System.out.println("* 3 Combo - 보너스 점수 5점 획득");
                    score += 5;
                }
            }

            System.out.println("현재 점수 : " + score);

            if (score >= 5) {
                System.out.println("승리! 최종점수 : " + score);
                break;
            }
            else if (score <= -5) {
                System.out.println("패배! 최종점수 : " + score);
            }

        }
        sc.close();

    }
}

