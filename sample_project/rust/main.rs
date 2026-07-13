// Rust sample file
// demonstrating the Code Stats tool

/// Calculator struct
struct Calculator;

impl Calculator {
    /// Add two integers
    fn add(a: i32, b: i32) -> i32 {
        a + b
    }

    /// Multiply two integers
    fn multiply(a: i32, b: i32) -> i32 {
        let mut result = 0;
        for _ in 0..b {
            result += a;
        }
        result
    }
}

/// Main function
fn main() {
    println!("Hello, World!");
    println!("2 + 3 = {}", Calculator::add(2, 3));
    println!("2 * 3 = {}", Calculator::multiply(2, 3));
}