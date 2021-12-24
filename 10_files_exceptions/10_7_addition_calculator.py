# 10.3 EXCEPTIONS
## EXERCISE 10-7

print("You'll give me two numbers. ")
print("I will add them and reeturn the result. ")
print("Type 'q' to quit anytime.")

while True:
    number1 = input("First number: ")
    if number1 == 'q':
        break
    try:
        number1 = int(number1)
    except ValueError:
        print("You can only imput numerical values or 'q' ")
        continue

    number2 = input("Second number: ")
    if number2 == 'q':
        break
    try:
        number2 = int(number2)
    except ValueError:
        print("You can only imput numerical values or 'q' ")
        continue

    sum = number1 + number2
    print(sum)
