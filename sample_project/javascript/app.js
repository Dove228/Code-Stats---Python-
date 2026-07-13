// JavaScript sample file
// demonstrating the Code Stats tool

/**
 * Greets a person by name
 * @param {string} name - The person's name
 * @returns {string} Greeting message
 */
function greet(name) {
    return `Hello, ${name}!`;
}

/**
 * Calculator class
 */
class Calculator {
    /**
     * Add two numbers
     * @param {number} a - First number
     * @param {number} b - Second number
     * @returns {number} Sum
     */
    add(a, b) {
        return a + b;
    }

    /**
     * Multiply two numbers
     * @param {number} a - First number
     * @param {number} b - Second number
     * @returns {number} Product
     */
    multiply(a, b) {
        let result = 0;
        for (let i = 0; i < b; i++) {
            result += a;
        }
        return result;
    }
}

// Main execution
const calc = new Calculator();
console.log(greet("World"));
console.log(`2 + 3 = ${calc.add(2, 3)}`);
console.log(`2 * 3 = ${calc.multiply(2, 3)}`);