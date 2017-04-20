"""
try:
    print(10/0)
except ZeroDivisionError:
    print("You can't divide by zero.")
"""
print("Please give me two numbers, and I'll divide them.")
print("Enter 'q' to quit this program.")

while True:
    first_number = input("\nInput first number: ")
    if first_number == 'q':
        break
    second_number = input("\nInput second number: ")
    if second_number == 'q':
        break
    # 异常处理
    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        print("Division result is " + str(result))



