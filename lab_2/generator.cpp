#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

vector<int> generateBinaryNumbers(int size) {
    vector<int> numbers(size);
    srand(time(0));
    for (int i = 0; i < size; ++i) {
        numbers[i] = rand() % 2;
    }
    return numbers;
}

int main() {
    int size = 128;
    vector<int> binaryNumbers = generateBinaryNumbers(size);
    for (int num : binaryNumbers) {
        cout << num;
    }
    cout << endl;
    return 0;
}
