import java.util.Random;

public class Main {

    public static int[] generateBinaryNumbers(int size) {
        int[] numbers = new int[size];
        Random random = new Random();
        for (int i = 0; i < size; ++i) {
            numbers[i] = random.nextInt(2);
        }
        return numbers;
    }

    public static void main(String[] args) {
        int size = 128;
        int[] binaryNumbers = generateBinaryNumbers(size);
        for (int num : binaryNumbers) {
            System.out.print(num);
        }
    }
}
