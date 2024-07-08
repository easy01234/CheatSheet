try:
    num1=int(input("Enter a number: "))
    
    num2=int(input("Enter another number: "))
    result=num1/num2
    print("Result: ",result)
except ValueError:
    print("Invalid input,Please Enter a Valid Input.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero ")
except Exception as e:
    print("An error Occurred:",str(e))