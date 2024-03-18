# Function to test if the result of base to the exponent is greater than 5000
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    # Test Cases
print("Test cases for large_power function:")
print(large_power(99, 3)) 
print(large_power(1, 10))  

# Function to prompt user input and perform large power calculation
def perform_large_power_calculation():
    base = float(input("Enter the base number: "))
    exponent  = float(input("Enter the exponent: "))
    result = large_power(base, exponent)
    if result:
        print("The result of the base to the exponent is greater than 5000.")
    else:
        print("The result of the base to the exponent is not greater than 5000.")