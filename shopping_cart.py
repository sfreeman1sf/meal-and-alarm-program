# CSC500 - Module 3 Portfolio Milestone
# Online Shopping Cart (2 items)
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${fmt_money(self.item_price)} = ${fmt_money(total)}")

def fmt_money(x: float) -> str:
    """Show dollars like the example: $1 not $1.00; keep cents if needed (e.g., 2.50)."""
    return str(int(x)) if float(x).is_integer() else f"{x:.2f}"

def get_valid_string(prompt):
    """Prompt for a string input, handle EOFError."""
    while True:
        try:
            value = input(prompt)
            if not value.strip():
                print("Input cannot be empty. Please try again.")
                continue
            return value
        except EOFError:
            print("Input interrupted (EOF). Please try again.")
            continue

def get_valid_float(prompt):
    """Prompt for a valid float, handle invalid inputs and EOFError."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            print("Input interrupted (EOF). Please try again.")

def get_valid_int(prompt):
    """Prompt for a valid integer, handle invalid inputs and EOFError."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except EOFError:
            print("Input interrupted (EOF). Please try again.")

if __name__ == "__main__":
    try:
        # Item 1
        print("Item 1")
        name1 = get_valid_string("Enter the item name:\n")
        price1 = get_valid_float("Enter the item price:\n")
        qty1 = get_valid_int("Enter the item quantity:\n")
        item1 = ItemToPurchase(name1, price1, qty1)

        # Item 2
        print("\nItem 2")
        name2 = get_valid_string("Enter the item name:\n")
        price2 = get_valid_float("Enter the item price:\n")
        qty2 = get_valid_int("Enter the item quantity:\n")
        item2 = ItemToPurchase(name2, price2, qty2)

        # Output
        print("\nTOTAL COST")
        item1.print_item_cost()
        item2.print_item_cost()
        total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
        print(f"\nTotal: ${fmt_money(total_cost)}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")