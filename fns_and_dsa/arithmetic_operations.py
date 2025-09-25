def perform_operation(num1: float, num2: float, operation: str):
  if operation == 'add':
    result = num1 + num2
    print(f"result: {result}")
  
  elif operation == 'subtract':
    result = num1 - num2 
    print(f"result: {result}")

  elif operation == 'divide':
    if num2 != 0:
      result = num1 / num2
      print(f"result: {result}")
    else:
       print("Error: Division by zero is not allowed.")
       
  elif operation == 'multiply':
        result = num1 * num2
        print(f"result: {result}") 
        
  else: 
    print("Enter a Valid Operation")

  