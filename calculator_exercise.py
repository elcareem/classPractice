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

first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

sub = first_number - second_number
print("**************")
print(f"The difference of {first_number} and {second_number} is {sub:.2f}\n")

first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

mul = first_number * second_number
print("**************")
print(f"The multiplication value of {first_number} and {second_number} is {mul:.2f}\n")

first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

div = first_number / second_number
print("**************")
print(f"The division value of {first_number} and {second_number} is {div:.2f}\n")

first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

floor_div = first_number // second_number
print("**************")
print(f"The floor division value of {first_number} and {second_number} is {floor_div:.2f}\n")


first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))

exp = first_number ** second_number
print("**************")
print(f"The value of {first_number} raised to the power of {second_number} is {exp:.2f}\n")

