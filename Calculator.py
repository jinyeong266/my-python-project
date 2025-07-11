# Guidance
print("This calculator performs basic arithmetic operations.\n")

# Input num1
while True:
  try:
    num1 = float(input("Please, enter the first number to be calculated: ").strip())
    break
  except ValueError:
    print("Invalid input! Please enter a valid number.")

# Input num2    
while True:
  try:
    num2 = float(input("Please, enter the second number to be calculated: ").strip())
    break
  except ValueError:
    print("Invalid input! Please enter a valid number.")
        
# Calculator
addition_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2

# Division with zero division check
if num2 != 0:
  division_result = num1 / num2
else:
  division_result = None

# Output the result
print(f"The result of addition is {addition_result}.")
print(f"The result of subtraction is {subtraction_result}.")
print(f"The result of multiplication is {multiplication_result}.")

if division_result is not None:
  print(f"The result of division is {division_result:.3f}.")
else:
  print(f"Division by {num2}(zero) is undefined.")
