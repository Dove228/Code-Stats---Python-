/* Java sample file */
/* demonstrating the Code Stats tool */

package com.example;

/**
 * A simple Java class
 */
public class Calculator {
    
    /**
     * Add two integers
     * @param a first integer
     * @param b second integer
     * @return sum of a and b
     */
    public int add(int a, int b) {
        return a + b;
    }
    
    /**
     * Multiply two integers
     * @param a first integer
     * @param b second integer
     * @return product of a and b
     */
    public int multiply(int a, int b) {
        int result = 0;
        for (int i = 0; i < b; i++) {
            result += a;
        }
        return result;
    }
    
    /**
     * Main method
     */
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println("Hello, World!");
        System.out.println("2 + 3 = " + calc.add(2, 3));
        System.out.println("2 * 3 = " + calc.multiply(2, 3));
    }
}