// TypeScript sample file
// demonstrating the Code Stats tool

/**
 * Greets a person by name
 * @param name - The person's name
 * @returns Greeting message
 */
function greet(name: string): string {
    return `Hello, ${name}!`;
}

/**
 * Calculator class with type safety
 */
class Calculator {
    /**
     * Add two numbers
     */
    add(a: number, b: number): number {
        return a + b;
    }

    /**
     * Multiply two numbers
     */
    multiply(a: number, b: number): number {
        let result: number = 0;
        for (let i: number = 0; i < b; i++) {
            result += a;
        }
        return result;
    }
}

// Main execution
const calc: Calculator = new Calculator();
console.log(greet("World"));
console.log(`2 + 3 = ${calc.add(2, 3)}`);
console.log(`2 * 3 = ${calc.multiply(2, 3)}`);