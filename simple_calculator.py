first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
addition_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number
floor_division_result = first_number // second_number
modulus_result = first_number % second_number
exponentiation_result = first_number ** second_number
print("\n" + "=" * 45)
print(f"  ARITHMETIC OPERATIONS RESULTS")
print("=" * 45)
print(f"  First Number  : {first_number}")
print(f"  Second Number : {second_number}")
print("-" * 45)
print(f"  {first_number} + {second_number}  = {addition_result}")
print(f"  {first_number} - {second_number}  = {subtraction_result}")
print(f"  {first_number} * {second_number}  = {multiplication_result}")
print(f"  {first_number} / {second_number}  = {division_result}")
print(f"  {first_number} // {second_number} = {floor_division_result}")
print(f"  {first_number} % {second_number}  = {modulus_result}")
print(f"  {first_number} ** {second_number} = {exponentiation_result}")
print("=" * 45)
