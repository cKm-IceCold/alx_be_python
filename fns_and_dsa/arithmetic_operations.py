def perform_operation(num1, num2, operation):
  if operation == 'add':
    result = num1 + num2
    print(f"result: {result}")
  
  elif operation == 'subtract':
    result = num1 - num2 
    print(f"result: {result}")

  elif operation == 'divide':
    if num2 != 0:
      return num1 / num2
    
    else:
       return "Error: Division by zero is not allowed."
       
  elif operation == 'multiply':
        result = num1 * num2
        print(f"result: {result}") 
        
  else: 
    print("Enter a Valid Operation")

  perform_operation(10, 5, 'add')
