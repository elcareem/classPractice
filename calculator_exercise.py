#A simple calculator app
print('''***********************
1. Addtion
2. Subtraction
3. Multiplication
4. Division
**********************
''')
print("Enter two numbers to add")
first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))
sum = float(first_number + second_number)
print(f"\nThe sum of {first_number} and {second_number} is {sum:.2f} \n")

sub = first_number - second_number
print("**************")
print(f"The difference of {first_number} and {second_number} is {sub:.2f}\n")

mul = first_number * second_number
print("**************")
print(f"The multiplication value of {first_number} and {second_number} is {mul:.2f}\n")

div = first_number / second_number
print("**************")
print(f"The division value of {first_number} and {second_number} is {div:.2f}\n")

exp = first_number ** second_number
print("**************")
print(f"The value of {first_number} raised to the power of {second_number} is {exp:.2f}\n")

