def get_number(number):
    while True:
        operand1 = input(f"Number {number}: ")
        try:
            return float(operand1)
        except:
            print('Invalid Number, Try again!')

operand1 = get_number(1)
operand2 = get_number(2)
sign = input("Sign: ")

result = 0
if sign == "+":
    result = float(operand1) +  float(operand2)
elif sign == "-":    
    result = float(operand1) -  float(operand2)
elif sign == "*":    
    result = float(operand1) *  float(operand2)        
elif sign == "/":   
    if float(operand2) !=0: 
        result = float(operand1) /  float(operand2)
    else:
        print("Division by Zero")
else:
    print("Invalid Sign")        

print(result)