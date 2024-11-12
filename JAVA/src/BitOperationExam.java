public class BitOperationExam {
    public static void main(String[] args) {
        int a = 6;
        int b = 3;

        int resultAnd = a&b;
        System.out.println(resultAnd);

        int resultOr = a|b;
        System.out.println(resultOr);

        int resultXor = a^b;
        System.out.println(resultXor);

        int resultNot = ~a;
        System.out.println(resultNot);

        int resultLeftShift = a << 1;
        System.out.println(resultLeftShift);

        int resultRightShift = a >> 1;
        System.out.println(resultRightShift);
    }
}
