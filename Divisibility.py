#Function to check if a number is divisible by ten
def check_divisibility_by_ten():
    num = int(input("Enter a number to check if its divisible by ten: "))
    if divisible_by_ten():
        print(f"{num} is divisible by ten.")
    else:
        print(f"{num} is not divisible by ten")

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
print("\nTest cases for divisible_by_ten function:")
print(divisible_by_ten(25))  # False
print(divisible_by_ten(100)) # True

# Function to prompt user input and check divisibility by 10
