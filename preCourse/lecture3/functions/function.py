# Global variable to track the total number of discounts applied
total_discounts_applied = 0

# 1. Decorator: Logging function calls
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# 2. Higher-Order Function: Apply a discount
def apply_discount(discount_function):
    def calculate(price):
        return discount_function(price)
    return calculate

# 3. Function Definitions with Scope Example
@log_decorator
def fixed_discount(price):
    """Applies a fixed discount of $20."""
    global total_discounts_applied  # Modify global variable
    total_discounts_applied += 1
    discount = 20
    return max(0, price - discount)  # Ensure price doesn't go below 0

@log_decorator
def percentage_discount(price, percentage=10):
    """Applies a percentage discount (default: 10%)."""
    global total_discounts_applied
    total_discounts_applied += 1
    return price - (price * (percentage / 100))

# 4. Using Higher-Order Function with Lambdas
@log_decorator
def calculate_total(prices, discount_function):
    """Applies a discount to a list of prices and returns the total."""
    return sum([discount_function(price) for price in prices])

# 5. Nested Function and Enclosing Scope Example
def dynamic_discount(multiplier):
    """Returns a discount function with a dynamic multiplier."""
    def discount(price):
        # Enclosing scope variable: multiplier
        return price - (price * multiplier)
    return discount

# 6. Main Program
if __name__ == "__main__":
    # List of prices
    prices = [100, 150, 200, 300]

    # Applying a fixed discount
    print("\n--- Fixed Discount ---")
    fixed = apply_discount(fixed_discount)
    print("Discounted Prices:", [fixed(price) for price in prices])

    # Applying a percentage discount
    print("\n--- Percentage Discount (15%) ---")
    percentage = apply_discount(lambda price: percentage_discount(price, percentage=15))
    print("Discounted Prices:", [percentage(price) for price in prices])

    # Using a dynamic discount (20% off)
    print("\n--- Dynamic Discount (20%) ---")
    dynamic = dynamic_discount(0.20)
    print("Discounted Prices:", [dynamic(price) for price in prices])

    # Calculate total price after discount
    print("\n--- Total Price Calculation ---")
    total = calculate_total(prices, dynamic)
    print("Total Price after Discount:", total)

    # Global variable: Total discounts applied
    print(f"\nTotal Discounts Applied Globally: {total_discounts_applied}")
