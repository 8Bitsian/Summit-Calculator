# Basic Arithmetic Calculator
def print_menu():
  """Print calculator menu"""
  print("Available Operations")
  print("+ | Add")
  print("- | Subtract")
  print("* | Multiply")
  print("/ | Divide")

# Input value
def get_input():
  """Get calculator input"""
  a = float(input("Enter value: "))
  b = float(input("Enter value: "))
  return (a, b)

# Process values
def add(a, b):
  """Addition"""
  return a + b

def subtract(a, b):
  """Subtraction"""
  return a - b

def multiply(a, b):
  """Multiplication"""
  return a * b
  
def divide(a, b):
  """Division"""
  if b == 0:
    return "ERROR: Cannot divide by zero!"
  else:
    return a / b

# Output value
def set_output(result):
  print(f"Total: {result}")

def main():
  """Get user input"""
  print_menu()
  operation = input("Enter operation: ").strip()
  
  if operation not in ("+", "-", "*", "/"):
    print("ERROR: Invalid Operation")
    return

  a, b = get_input()

  if operation == '+':
    c = add(a, b)
  elif operation == '-':
    c = subtract(a, b)
  elif operation == '*':
    c = multiply(a, b)
  elif operation == '/':
    c = divide(a, b)

  set_output(c)

main()
