# Function to calculate discount
def calculate_discount(price, discount_percent):
 
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Prompting user input and applying discount
def apply_discount():
    price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after applying the discount is: ${final_price:.2f}")

# Applying discount based on user input
apply_discount()