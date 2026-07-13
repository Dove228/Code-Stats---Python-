// Go sample file
// demonstrating the Code Stats tool

package main

import "fmt"

// Calculator struct
type Calculator struct{}

// Add two integers
func (c *Calculator) Add(a, b int) int {
	return a + b
}

// Multiply two integers
func (c *Calculator) Multiply(a, b int) int {
	result := 0
	for i := 0; i < b; i++ {
		result += a
	}
	return result
}

// Main function
func main() {
	calc := &Calculator{}
	fmt.Println("Hello, World!")
	fmt.Printf("2 + 3 = %d\n", calc.Add(2, 3))
	fmt.Printf("2 * 3 = %d\n", calc.Multiply(2, 3))
}