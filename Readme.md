# Advanced Calculator Documentation
 
## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation & Setup](#installation--setup)
4. [Usage Guide](#usage-guide)
5. [Method Reference](#method-reference)
6. [Examples](#examples)
7. [Error Handling](#error-handling)
8. [Technical Details](#technical-details)
---
 
## Overview
 
The **Advanced Calculator** is a comprehensive Python application that performs various mathematical operations. It provides a user-friendly interactive menu for students, professionals, and anyone who needs to perform complex calculations beyond basic arithmetic.
 
### Key Highlights
- different mathematical operations
- Interactive command-line interface
- Error handling for invalid inputs
- Advanced algorithms (Newton's method, Taylor series, Binary search)
- Support for both basic and complex mathematical calculations
---
 
## Features
 
### 1. **Basic Arithmetic Operations**
   - Addition
   - Subtraction
   - Multiplication
   - Division (with zero-division error handling)
### 2. **Power & Root Operations**
   - Find Power (exponential calculations)
   - Find Square Root
   - Find Nth Root (using Newton's method)
### 3. **Factorial Calculation**
   - Recursive factorial computation
   - Useful for combinatorics and probability
### 4. **Financial Calculations**
   - Simple Interest: `SI = (P × R × T) / 100`
   - Compound Interest: `CI = P(1 + R/100)^T - P`
### 5. **Logarithmic Functions**
   - Base 10 Logarithm (using Binary search)
   - Custom Base Logarithm (using change of base formula)
### 6. **Trigonometric Functions**
   - Sine function (using Taylor series expansion)
---
 
## Installation & Setup
 
### Requirements
- Python 3.6 or higher
- No external libraries required (uses only built-in Python)
### Steps
1. Save the code as `calculate.py`
2. Open terminal/command prompt in the directory
3. Run: `python calculate.py`
```bash
python calculate.py
```
 
---
 
## Usage Guide
 
### Running the Program
 
When you run the program, you'll see an interactive menu:
 
```
========================================
ADVANCED CALCULATOR MENU
========================================
1.  Addition
2.  Subtraction
3.  Multiplication        
4.  Division
5.  Find square root
6.  Find factorial
7.  Find power
8.  Calculate simple interest
9.  Calculate compound interest
10. Nth root
11. Compute logarithm with custom base
12. Sine of an angle
13. Exit
========================================
 
Enter your choice (1-13):
```
 
### Menu Navigation
 
1. Enter the number corresponding to your desired operation
2. Follow the prompts to enter required values
3. View the result
4. The menu will repeat, allowing multiple calculations
5. Press `13` to exit the program
---
 
## Method Reference
 
### Basic Arithmetic
 
#### `add(a, b)`
Performs addition of two numbers.
```python
result = calculator.add(10, 5)  # Returns: 15
```
 
#### `subtraction(a, b)`
Performs subtraction of two numbers.
```python
result = calculator.subtraction(10, 5)  # Returns: 5
```
 
#### `multiplication(a, b)`
Performs multiplication of two numbers.
```python
result = calculator.multiplication(10, 5)  # Returns: 50
```
 
#### `division(a, b)`
Performs division with zero-division error handling.
```python
result = calculator.division(10, 5)   # Returns: 2.0
result = calculator.division(10, 0)   # Returns: "Division by zero is not possible"
```
 
---
 
### Power & Root Operations
 
#### `find_power(base, exponent)`
Calculates base raised to the power of exponent.
```python
result = calculator.find_power(2, 3)      # Returns: 8
result = calculator.find_power(2, -1)     # Returns: 0.5
result = calculator.find_power(4, 0.5)    # Returns: 2.0 (square root)
```
 
#### `find_square_root(n)`
Calculates the square root of a number.
```python
result = calculator.find_square_root(16)   # Returns: 4.0
result = calculator.find_square_root(-4)   # Returns: "Square root of negative number is not possible"
```
 
#### `find_nth_root(A, n, e=1e-6)`
Calculates the nth root using Newton's method.
 
**Algorithm**: Uses iterative formula: `x = ((n-1)*x + A/x^(n-1)) / n`
 
```python
result = calculator.find_nth_root(27, 3)   # Returns: 3.0 (cube root)
result = calculator.find_nth_root(16, 4)   # Returns: 2.0 (fourth root)
result = calculator.find_nth_root(-8, 3)   # Returns: -2.0 (odd root of negative)
result = calculator.find_nth_root(-4, 2)   # Returns: "Even root of negative number is not possible"
```
 
**Parameters**:
- `A`: The number to find root of
- `n`: Degree of root
- `e`: Precision threshold (default: 1e-6)
---
 
### Factorial
 
#### `find_factorial(n)`
Calculates factorial using recursion.
Formula: `n! = n × (n-1) × (n-2) × ... × 1` where `0! = 1`
 
```python
result = calculator.find_factorial(5)   # Returns: 120 (5×4×3×2×1)
result = calculator.find_factorial(0)   # Returns: 1
```
 
**Warning**: For very large numbers (n > 1000), may cause recursion depth error.
 
---
 
### Financial Calculations
 
#### `calculate_simple_interest(principal, rate, time)`
Calculates simple interest.
Formula: `SI = (P × R × T) / 100`
 
```python
# $1000 at 5% per year for 2 years
result = calculator.calculate_simple_interest(1000, 5, 2)  # Returns: 100
```
 
**Parameters**:
- `principal` (P): Initial amount
- `rate` (R): Annual interest rate in percentage
- `time` (T): Time period in years
#### `calculate_compound_interest(principal, rate, time)`
Calculates compound interest.
Formula: `CI = P(1 + R/100)^T - P`
 
```python
# $1000 at 5% per year for 2 years (compounded annually)
result = calculator.calculate_compound_interest(1000, 5, 2)  # Returns: 102.5
```
 
**Parameters**:
- `principal` (P): Initial amount
- `rate` (R): Annual interest rate in percentage
- `time` (T): Time period in years
---
 
### Logarithmic Functions
 
#### `compute_log_base_10(a)`
Calculates logarithm base 10 using binary search.
 
**Algorithm**: Finds `x` such that `10^x = a` using iterative binary search over 50 iterations.
 
```python
result = calculator.compute_log_base_10(100)    # Returns: 2.0
result = calculator.compute_log_base_10(1)      # Returns: 0.0
result = calculator.compute_log_base_10(-5)     # Prints error message
```
 
#### `compute_log_base_a_of_b(a, num)`
Calculates logarithm with custom base.
Formula: `log_a(num) = log_10(num) / log_10(a)` (Change of Base formula)
 
```python
result = calculator.compute_log_base_a_of_b(2, 8)   # Returns: 3.0 (since 2^3 = 8)
result = calculator.compute_log_base_a_of_b(10, 100) # Returns: 2.0
```
 
**Parameters**:
- `a`: Base of logarithm (must be > 1)
- `num`: Number to find logarithm of (must be > 0)
**Constraints**:
- Base `a` must be > 1
- Number must be > 0
---
 
### Trigonometric Functions
 
#### `sine(angle)`
Calculates sine of an angle using Taylor series expansion.
 
**Algorithm**: `sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...` (approximated with 10 terms)
 
```python
result = calculator.sine(0)     # Returns: 0.0
result = calculator.sine(90)    # Returns: ~1.0
result = calculator.sine(180)   # Returns: ~0.0
result = calculator.sine(270)   # Returns: ~-1.0
```
 
**Parameters**:
- `angle`: Angle in degrees (automatically converted to radians)
**Accuracy**: Accurate to ~10 decimal places for angles within ±360°
 
---
 
## Examples
 
### Example 1: Simple Interest Calculation
```python
c = AdvancedCalculator()
 
# Calculate interest on $5000 at 8% per year for 3 years
principal = 5000
rate = 8
time = 3
 
interest = c.calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: ${interest}")  # Output: Simple Interest: $1200.0
```
 
### Example 2: Factorial Calculation
```python
c = AdvancedCalculator()
 
# Calculate permutations: P(10,3) = 10!/(10-3)! = 10*9*8
result = c.find_factorial(10) // c.find_factorial(7)
print(result)  # Output: 720
```
 
### Example 3: Compound Interest
```python
c = AdvancedCalculator()
 
# Calculate compound interest on $10000 at 5% for 2 years
principal = 10000
rate = 5
time = 2
 
ci = c.calculate_compound_interest(principal, rate, time)
print(f"Compound Interest: ${ci}")  # Output: Compound Interest: $1025.0
```
 
### Example 4: Cube Root
```python
c = AdvancedCalculator()
 
# Find cube root of 125
cube_root = c.find_nth_root(125, 3)
print(f"Cube root of 125: {cube_root}")  # Output: Cube root of 125: 5.0
```
 
### Example 5: Logarithm
```python
c = AdvancedCalculator()
 
# Calculate log base 2 of 64
result = c.compute_log_base_a_of_b(2, 64)
print(f"log₂(64) = {result}")  # Output: log₂(64) = 6.0
```
 
---
 
## Error Handling
 
The calculator handles various error conditions gracefully:
 
| Error Condition | Method | Response |
|---|---|---|
| Division by zero | `division()` | Returns error message |
| Square root of negative | `find_square_root()` | Returns error message |
| Even root of negative | `find_nth_root()` | Returns error message |
| Log of non-positive | `compute_log_base_10()` | Prints error message |
| Invalid log base | `compute_log_base_a_of_b()` | Prints error message |
| Invalid menu choice | Main loop | Prompts to re-enter |
 
---
 
## Technical Details
 
### Algorithms Used
 
#### 1. **Newton's Method (Nth Root)**
- Iterative approach for finding roots
- Converges quickly for well-behaved functions
- Formula: `x_{n+1} = ((k-1)*x_n + A/x_n^(k-1)) / k`
- Precision controlled by epsilon (default: 1e-6)
#### 2. **Binary Search (Logarithm)**
- Finds logarithm by binary search between 0 and 2
- 50 iterations provide sufficient precision
- Time complexity: O(log n) where n is the number of iterations
#### 3. **Taylor Series (Sine)**
- Uses polynomial approximation
- Converges faster near 0
- 10 terms provide accuracy up to ~10 decimal places
- Series: `sin(x) = Σ (-1)^n * x^(2n+1) / (2n+1)!`
#### 4. **Recursion (Factorial)**
- Direct recursive implementation
- Base case: 0! = 1
- May hit recursion limit for n > 1000
### Complexity Analysis
 
| Operation | Time Complexity | Space Complexity |
|---|---|---|
| Addition/Subtraction/Multiplication/Division | O(1) | O(1) |
| Power | O(log n) | O(1) |
| Square Root | O(1) | O(1) |
| Factorial | O(n) | O(n) for recursion stack |
| Nth Root | O(50) = O(1) | O(1) |
| Log Base 10 | O(50) = O(1) | O(1) |
| Sine | O(10) = O(1) | O(1) |
 
---
 
## Improvements Made
 
The original code has been enhanced with:
 
1. ✅ Comprehensive docstrings for all methods
2. ✅ Fixed typo: `subraction` → `subtraction`
3. ✅ Fixed typo: `intrest` → `interest`
4. ✅ Fixed menu numbering (duplicate option 12)
5. ✅ Improved error messages capitalization and clarity
6. ✅ Better formatted menu with visual separators
7. ✅ Detailed inline comments explaining algorithms
8. ✅ Proper input prompts with context
9. ✅ Module-level docstring
10. ✅ Better code organization and readability
---
 
## Future Enhancements
 
Possible improvements for future versions:
 
- [ ] Add support for negative factorials (Gamma function)
- [ ] Implement additional trigonometric functions (cos, tan, etc.)
- [ ] Add matrix operations
- [ ] Support for complex numbers
- [ ] Graphical user interface (GUI) version
- [ ] Input validation for user inputs
- [ ] Memory feature to store previous results
- [ ] Support for more mathematical constants
- [ ] Unit conversion capabilities
- [ ] Export calculations to file
---
 
## Troubleshooting
 
### Issue: "RecursionError: maximum recursion depth exceeded"
**Cause**: Factorial calculation with very large number
**Solution**: Use iterative factorial or choose smaller numbers
 
### Issue: Inaccurate logarithm results
**Cause**: Limited precision due to 50 iterations
**Solution**: Results are accurate to ~6 decimal places for typical use cases
 
### Issue: Sine approximation is inaccurate for large angles
**Cause**: Taylor series has limited convergence radius
**Solution**: Use angles within ±360°, or implement range reduction
 
---
 
## License
This calculator is provided as educational material. Feel free to modify and use as needed.
 