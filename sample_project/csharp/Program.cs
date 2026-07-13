// C# sample file
// demonstrating the Code Stats tool

using System;

namespace CodeStatsDemo
{
    /// <summary>
    /// A simple calculator class
    /// </summary>
    public class Calculator
    {
        /// <summary>
        /// Add two integers
        /// </summary>
        public int Add(int a, int b)
        {
            return a + b;
        }

        /// <summary>
        /// Multiply two integers
        /// </summary>
        public int Multiply(int a, int b)
        {
            int result = 0;
            for (int i = 0; i < b; i++)
            {
                result += a;
            }
            return result;
        }
    }

    /// <summary>
    /// Main program class
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            Calculator calc = new Calculator();
            Console.WriteLine("Hello, World!");
            Console.WriteLine($"2 + 3 = {calc.Add(2, 3)}");
            Console.WriteLine($"2 * 3 = {calc.Multiply(2, 3)}");
        }
    }
}