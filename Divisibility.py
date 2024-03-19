#Function to check if a number is divisible by ten
def divisible_by_ten(num):
    num = int(input("Enter a number to check if its divisible by ten: "))
    if num % 10 == 0:
        return True
    else:
        return False
print("\nTest cases for divisible_by_ten function:")
print(divisible_by_ten(25))  # False
print(divisible_by_ten(100)) # True

