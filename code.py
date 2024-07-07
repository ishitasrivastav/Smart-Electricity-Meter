# ElectricMeter class represents a utility meter to track usage and limit of different categories.

class ElectricMeter:
    def __init__(self, total_units):
        # Constructor to initialize the ElectricMeter object.
        self.total_units = total_units
        self.categories = {}  # Dictionary to store category-wise total units.
        self.usage = {}      # Dictionary to store category-wise usage.

    def add_category(self, category, units):
        # Method to add a new category with specified units.
        self.categories[category] = units
        self.usage[category] = 0

    def usage_mode(self):
        # Method to input and update category-wise usage.
        print("Enter the units used for each category:")
        for category in self.categories:
            units = float(input(f"{category}: "))
            self.usage[category] += units
            self.categories[category] -= units
        print("Usage updated successfully.")

    def check_limit(self):
        # Method to check if any category has exceeded its limit and adjust accordingly.
        for category, units in self.categories.items():
            if units < 0:
                print(f"WARNING: {category} category has exceeded its limit.")
                # Find the category with the highest available units
                max_units_category = max(self.categories, key=self.categories.get)
                borrowed_units = min(abs(units), self.categories[max_units_category])
                self.categories[max_units_category] -= borrowed_units
                self.categories[category] += borrowed_units
                print(f"Borrowed {borrowed_units} units from {max_units_category} category.")

    def show_balance(self):
        # Method to display the balance units for each category.
        print("Balance units for each category:")
        for category, units in self.categories.items():
            print(f"{category}: {units} units")

    def run(self):
        # Method to run the menu-driven utility meter application.
        while True:
            print("\n1. Usage Mode\n2. Check Limit\n3. Show Balance\n4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.usage_mode()
                self.check_limit()
            elif choice == "2":
                self.check_limit()
            elif choice == "3":
                self.show_balance()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")


def main():
    # Main function to drive the utility meter application.
    while True:
        total_units = int(input("Enter the total number of units: "))

        # Asking user for categories and units until the sum matches total_units
        while True:
            meter = ElectricMeter(total_units)

            # Adding categories
            num_categories = int(input("Enter the number of categories: "))
            category_units = {}
            sum_units = 0
            for _ in range(num_categories):
                category = input("Enter category name: ")
                units = float(input("Enter units for this category: "))
                category_units[category] = units
                sum_units += units

            if sum_units != total_units:
                print(f"Sum of units ({sum_units}) does not match total units ({total_units}). Please re-enter.")
            else:
                for category, units in category_units.items():
                    meter.add_category(category, units)
                break

        meter.run()


if __name__ == "__main__":
    main()
