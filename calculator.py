# 1. ADD
# 2. SUBTRACT

while True:
  print("Select an operation to perform.")
  print("1. ADD")
  print("2. SUBTRACT")
  print("3. Exit")


  operation = input()

  if operation == "1":
      num1 = input("Enter first number:")
      num2 = input("Enter second number:")
      print("The sum is " + str(int(num1) + int(num2)))
  elif operation == "2":
      num1 = input("Enter first number:")
      num2 = input("Enter second number:")
      print("The sum is " + str(int(num1) - int(num2)))
  elif operation == "3":
    break

