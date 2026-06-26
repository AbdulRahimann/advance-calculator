#################################
##     ADVANCE CALCULATOR      ##
#################################


"""
Advanced Calculator - A comprehensive mathematical calculation tool
This module provides a class with various mathematical operations including:
- Basic arithmetic (addition, subtraction, multiplication, division)
- Advanced operations (factorial, power, roots, logarithms)
- Trigonometric functions (sine)
- Financial calculations (simple and compound interest)
"""


class AdvancedCalculator:

    """
    A calculator class that performs various mathematical operations.
    
    Methods include arithmetic, power operations, roots, logarithms,
    trigonometric functions, and financial calculations. """

    def add(self,a,b):
        """
        Addition operation.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    def subraction(self,a,b): 
        """
        Subtraction operation.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            Difference of a and b (a - b)
        """
        return a - b

    def multiplication(self,a,b):
        """
        Multiplication operation.
        
        Args:
            a: First number (multiplicand)
            b: Second number (multiplier)
            
        Returns:
            Product of a and b
        """
        return a * b
    
    def division(self,a,b):
        """
        Division operation with zero-division error handling.
        
        Args:
            a: Dividend (numerator)
            b: Divisor (denominator)
            
        Returns:
            Result of a divided by b
            Error message if b is zero
        """

        try:
            return a / b
        except ZeroDivisionError:
            return "division by zero is not possible"
        
    def find_square_root(self,n):
        """
        Calculate the square root of a number.
        
        Args:
            n: Non-negative number
            
        Returns:
            Square root of n
            Error message if n is negative
        """
 
        if n < 0:
            return "square root of negetive number is not possible"
        else:
            return n ** 0.5
        
    def find_factorial(self,n):
        """
        Calculate the factorial of a number using recursion.
        
        Factorial(n) = n * (n-1) * (n-2) * ... * 1
        Factorial(0) = 1
        
        Args:
            n: Non-negative integer
            
        Returns:
            Factorial of n
            
        Note:
            Uses recursive approach. May cause stack overflow for very large n.
        """
        if n == 0:
            return 1
        else:
            return n * self.find_factorial(n - 1)
        
    def find_power(self,base, exponent):
        """
        Calculate the power of a number.
        
        Result = base ^ exponent
        
        Args:
            base: Base number
            exponent: Power (can be positive, negative, or fractional)
            
        Returns:
            base raised to the power of exponent
        """
        return base ** exponent
    
    def calculate_simple_intrest(self,principal, rate, time):
        """
        Calculate simple interest using the formula: SI = (P * R * T) / 100
        
        Args:
            principal: Initial amount (P)
            rate: Annual interest rate in percentage (R)
            time: Time period in years (T)
            
        Returns:
            Simple interest amount
        """

        return (principal * rate * time) / 100
    
    def calculate_compound_intrest(self,principal, rate, time):
        """
        Calculate compound interest using the formula: 
        CI = P(1 + R/100)^T - P
        
        Args:
            principal: Initial amount (P)
            rate: Annual interest rate in percentage (R)
            time: Time period in years (T)
            
        Returns:
            Compound interest amount
        """
 
        a = principal * (1 + rate / 100) ** time
        return a - principal

    def find_n_th_root(self,A, n,e=1e-6):
        """
        Calculate the nth root of a number using Newton's method.
        
        Uses iterative approach: x = ((n-1)*x + A/x^(n-1)) / n
        
        Args:
            A: The number to find root of
            n: The degree of root (e.g., 2 for square root, 3 for cube root)
            e: Precision threshold (default: 1e-6)
            
        Returns:
            nth root of A (approximated)
            Error message if even root of negative number is requested
        """


        if A < 0 and n % 2 == 0:
            return "even root of negetive number is not possible"
        x = A / n

        while True:
            prev = x

            x = ((n - 1) * x + A / (x ** (n - 1))) / n

            if abs(prev - x) < e:
                break
        return x

    def compute_log_a(self,a):
        
        if a <= 0:
            print("logarithms are not possible for non positive numers")
        else:
            x = 0
            high = 2
            low = 0
            for _ in range(50):
                x = (high + low) / 2

                if (10 ** x < a):
                    low=x
                else:
                    high=x
            print(x)
            return x
        
    def compute_log_base_a_of_b(self,a, num):

       
        if a <= 1:
            print(f"logarithm with base {a} is not exist")
            return 
        
        else:
            log_base=self.compute_log_a(a)
            log_num=self.compute_log_a(num)

            return log_num/log_base
       
        
    def sine(self, angle):
        pi=3.141592653589793
        rad = angle* pi /180

        term = rad
        sin_x = rad

        for n in range(1, 10):
            term = -term * rad * rad / ((2*n) * (2*n + 1))
            sin_x += term

        return sin_x 

    def start(self):
        while True:
            print("================================")
            print("ADVANCED CALCULATOR MENU")
            print("================================")
            print("\n1.addition")
            print("2.subtraction")
            print("3.multiplication")        
            print("4.division")
            print("5.find square root")
            print("6.find factorial")
            print("7.find power")
            print("8.calculate simple intrest")
            print("9.calculate compound intrest")
            print("10.n th root")
            print("11.compute log base a of b")
            print("12.sine of an angle")
            print("13.exit")

            print("================================")

            choice=int(input("\nenter your choice:"))

            print("================================")
        
            if choice==1:
                a=int(input("enter first number:"))
                b=int(input("enter second number:"))
                print("\nresult:",self.add(a,b))

            elif choice==2:
                a=int(input("enter first number:"))
                b=int(input("enter second number:"))
                print(f"\nresult:{self.subraction(a,b)}")

            elif choice==3:
                a=int(input("enter first number:"))
                b=int(input("enter second number:"))
                print(f"\nresult:{self.multiplication(a,b)}")

            elif choice==4:
                a=int(input("enter first number:"))
                b=int(input("enter second number:"))
                print(f"\nresult: {self.division(a,b)}")

            elif choice==5:
                a=int(input("enter a number:"))
                print(f"result :{self.find_square_root(a)}")

            elif choice ==6:
                a=int(input("enter a number:"))
                print(f"result: {self.find_factorial(a)}")

            elif choice ==7 :
                a=int(input("enter base:"))
                b=int(input("enter exponent:"))
                print(f"result : {self.find_power(a,b)}")

            elif choice ==8:
                principal=int(input("enter principal amount:"))
                rate=float(input("enter intrest rate:"))
                time=int(input("enter time in years:"))
                print(f"the simple intrest is:{self.calculate_simple_intrest(principal,rate,time)}")

            elif choice ==9:
                principal=int(input("enter principal amount:"))
                rate=float(input("enter intrest rate:"))
                time=int(input("enter time in years:"))
                print(f"the compound intrest is :{self.calculate_compound_intrest(principal,rate,time)}")

            elif choice ==10:
                A=int(input("enter a number:"))
                n=int(input("enter the root:"))
                print(f"result: {self.find_n_th_root(A,n)}")

            elif choice ==11:
                a=int(input("enter base:"))
                b=int(input("enter number:"))
                print(f"result: {self.compute_log_base_a_of_b(a,b)}")

            elif choice ==12:
                angle=float(input("enter an angle in degree:"))
                print(f"result: {self.sine(angle)}")
            elif choice==13:
                break

            else:
                print("wrong command")

            print("================================")








if __name__=='__main__':
    c=AdvancedCalculator()
    c.start()