class FibonacciCalculator:
    def __init__(self, n):
        self.n = n

    def compute(self):
        # Base cases
        if self.n <= 0:
            return 0
        elif self.n == 1:
            return 1
        
        # Iterative calculation (O(n) time, O(1) space)
        prev2 = 0  # F(0)
        prev1 = 1  # F(1)
        current = 0
        
        for _ in range(2, self.n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return current


if __name__ == "__main__":
    try:
        user_input = int(input("Enter the value of n: "))
        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            fib_obj = FibonacciCalculator(user_input)
            result = fib_obj.compute()
            print(f"The {user_input}th Fibonacci number is: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")