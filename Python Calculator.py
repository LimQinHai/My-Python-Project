from replit import clear
from ASCII_ART_resource_file import Calculator_logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiple(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operation={
  "+":add,
  "-":subtract,
  "*":multiple,
  "/":divide,
}
def calculator():
  print(Calculator_logo)

  num1 = float(input("What is the first number?"))
  for symbol in operation:
    print(symbol)
  terminate = False

  while not terminate:
    operation_symbol = input("Choose an operation from above.")
    num2 = float(input("What is the next number?"))
    calculation_function = operation[operation_symbol]

    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    respond = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.:").lower()
    if respond == "y":
      terminate = False
      num1 = answer

    else:
      terminate = True
      clear()
      calculator()

calculator()