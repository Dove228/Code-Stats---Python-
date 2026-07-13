# This is a Python sample file
# demonstrating the Code Stats tool

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

class Calculator:
    """A simple calculator class."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = 0
        for _ in range(b):
            result += a
        return result

if __name__ == "__main__":
    calc = Calculator()
    print(greet("World"))
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"2 * 3 = {calc.multiply(2, 3)}")