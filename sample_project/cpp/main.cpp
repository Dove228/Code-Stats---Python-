// C++ sample file
// demonstrating the Code Stats tool

#include <iostream>
#include <string>

/**
 * Calculator class
 */
class Calculator {
public:
    /**
     * Add two integers
     */
    int add(int a, int b) {
        return a + b;
    }
    
    /**
     * Multiply two integers
     */
    int multiply(int a, int b) {
        int result = 0;
        for (int i = 0; i < b; i++) {
            result += a;
        }
        return result;
    }
};

/**
 * Main function
 */
int main() {
    Calculator calc;
    std::cout << "Hello, World!" << std::endl;
    std::cout << "2 + 3 = " << calc.add(2, 3) << std::endl;
    std::cout << "2 * 3 = " << calc.multiply(2, 3) << std::endl;
    return 0;
}