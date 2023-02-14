first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

temp=first

print("----press key for operator (+,-,*,**,/,//,%)----")
operator = input ("Enter operator: ")

if operator == "+":
    print(str(first+second))

elif operator == "*":
    print(str(first*second))

elif operator == "**":
    for i in range(second-1):
        temp=temp*first
    print(str(temp))

    print(str(first**second))

elif operator == "/":
    print(str(first/second))

elif operator == "//":
    print(str(first//second))

elif operator == "%":
    print(str(first%second))

else:
    print("Invalid Operation")

