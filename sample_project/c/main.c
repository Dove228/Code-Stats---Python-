/* C sample file */
/* demonstrating the Code Stats tool */

#include <stdio.h>

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

/**
 * Main function
 */
int main() {
    printf("Hello, World!\n");
    printf("2 + 3 = %d\n", add(2, 3));
    printf("2 * 3 = %d\n", multiply(2, 3));
    return 0;
}