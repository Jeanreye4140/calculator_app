

def calc_app():
    
    def addition(num1, num2):
        result = num1 + num2
        print(f"This is the sum of {num1} and {num2}: {result} ")
    
    def subtraction(num1, num2):
        result = num2 - num1
        print(f"This is the subtraction of {num2} and {num1}: {result} ")
    
    def multiplication(num1, num2):
        result = num1 * num2
        print(f"This is the multiplication of {num1} and {num2}: {result} ")
        
    def division(num1, num2):
        result = num2 / num1
        print(f"This is the division of {num2} and {num1}: {result} ")
        
    operation = print("What operation do you need: addition, subtraction, multiplication, division")    
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    
calc_app()