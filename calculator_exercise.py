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
print(f"\nThe sum of {first_number} and {second_number} is {sum} \n")

sub = first_number + second_number
print("**************")
print(f"The difference of {first_number} and {second_number} is {sub}")
print(f"")
