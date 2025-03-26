num1 = float(input("insert a number: "))
num2 = float(input("insert the second number: "))
operation =input(" Enter an operation (+,-,*,/)")

if operation == '+' :
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result =  num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*" :
    result = num1 * num2 
    print(f"{num1} * {num2} = {result}")
elif operation == '/' :
 if num2 !=0 :
     result = num1 / num2
     print(f"{num1} / {num2} = {result}")

 else: print("Invalid: Divivion by 0 is not allowed.")

else:
    result =str("please enter a valid operation")

    print(result)


