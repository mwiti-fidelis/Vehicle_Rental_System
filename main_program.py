from datetime import datetime

class Vehicle:
    def __init__(self, make, model, year, rental_price):
        self.make = make
        self.model = model
        self.year = year
        self.rental_price = rental_price

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}"

    def calculate_rental_cost(self, days):
        total = self.rental_price * days
        return total


class Car(Vehicle):
    def __init__(self, make, model, year, rental_price, num_doors):
        super().__init__(make, model, year, rental_price)
        self.num_doors = num_doors

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Number of Doors: {self.num_doors}"

    def calculate_rental_cost(self, days):
        total = self.rental_price * days
        if days > 7:
            total *= 0.9
            return total
        else:
            return self.rental_price


class Truck(Vehicle):
    def __init__(self, make, model, year, rental_price, payload_capacity):
        super().__init__(make, model, year, rental_price)
        self.payload_capacity = payload_capacity

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Payload Capacity: {self.payload_capacity}"

    def calculate_rental_cost(self, days):
        total = self.rental_price * days
        if days < 3:
            total += 20.00
            return total
        else:
            return self.rental_price


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, rental_price, engine_size):
        super().__init__(make, model, year, rental_price)
        self.engine_size = engine_size

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Rental Price: {self.rental_price}, Engine Size: {self.engine_size}"

    def calculate_rental_cost(self, days):
        total = self.rental_price
        total = 15.0 * days
        return total


class RentalSystem:
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.customer_dict = {'fidel': 9854, 'mwiti': 32122, 'Moreen': 546542}
        # Map customer name -> list of rental records.
        # Each rental record is a dict: {'make','model','days','price_per_day','rented_on'}
        self.rented_vehicles = {'fidel': [], 'mwiti': [], 'Moreen': []}
    
    def available_vehicles(self):
        print("\nAvailable Vehicles in Inventory:")
        print("--------------------------------")
        if not self.vehicles:
            print("No vehicles currently in inventory.")
            return self.vehicles
        
        print(f"Total vehicles: {len(self.vehicles)}")
        for i, vehicle in enumerate(self.vehicles, 1):
            print(f"\n{i}. {vehicle.get_info()}")
        return self.vehicles

    def add_customer(self):
        customer_count = len(self.customer_dict)
        no_of_customers = int(input("Enter the number of customers you would like to add: "))
        for customer in range(no_of_customers):
            name = input("Enter the name of the customer: ").strip()
            license_number = int(input("Enter the customer's license number: "))
            self.customer_dict[name] = license_number
            # initialize an empty list for future rentals
            self.rented_vehicles[name] = []
            print(f"The new customer's name is: {name} and their license number is: {license_number} ")
            customer_count += 1
        print(self.customer_dict)
        print("")
        return self.customer_dict

    def rent_vehicle(self):
        name = input("Enter the name of the customer: ").strip()
        # Validate customer exists
        if not name or name not in self.customer_dict:
            print("Customer does not exist. Kindly add the new customer.")
            return
        print("Customer exists.")

        number_of_vehicles = input("Enter the number of vehicles you wish to rent: ").strip()
        try:
            number_of_vehicles = int(number_of_vehicles)
        except ValueError:
            print("Invalid input. Please enter a valid number")
            exit()
        # Ensure there is a list to append to
        self.rented_vehicles.setdefault(name, [])

        for i in range(number_of_vehicles):
            model_input = input("Enter the model or make of the vehicle you want to rent: ").strip()
            if not model_input:
                print("Invalid model input. Please try again.")
                return

            # Find vehicle in inventory by model or make (case-insensitive)
            found = None
            for v in self.vehicles:
                if model_input.lower() == v.model.lower() or model_input.lower() == v.make.lower():
                    found = v
                    break

            if not found:
                print("Vehicle does not exist in our inventory. Enter a correct vehicle model or make.")
                return
            else:
                print("Vehicle exists in our inventory and is ready for hire.")

            try:
                days = int(input("Enter the number of days you wish to rent the vehicle: "))
            except ValueError:
                print("Invalid number of days. Please enter an integer.")
                return

            rental_record = {
                'make': found.make,
                'model': found.model,
                'days': days,
                'price_per_day': found.rental_price,
                'rented_on': datetime.now().strftime('%Y-%m-%d %H:%M')
            }

            # append the rental record to that customer's list
            self.rented_vehicles[name].append(rental_record)
            print(f"You have successfully rented: {rental_record}")
        print("")
        print(f"All rentals for {name}: {self.rented_vehicles[name]}")
        return self.rented_vehicles

    def return_vehicle(self):
        customer_returning = input("Enter the name of the customer returning the vehicle: ").strip()
        if not customer_returning or customer_returning not in self.customer_dict:
            print(f"The customer {customer_returning} does not exist in the customers list. Kindly confirm the name entered.")
            return

        # Ask for model or make to return
        vehicle_input = input("Enter the model or make of the vehicle you wish to return: ").strip().lower()
        if not vehicle_input:
            print("Invalid vehicle input.")
            return

        rentals = self.rented_vehicles.get(customer_returning, [])
        for idx, rec in enumerate(rentals):
            if vehicle_input == rec.get('model', '').lower() or vehicle_input == rec.get('make', '').lower():
                removed = rentals.pop(idx)
                print(f"{removed['make']} {removed['model']} has been returned by {customer_returning} on {datetime.now()}")
                return self.rented_vehicles

        print("The specified vehicle was not found in that customer's rentals.")
        return self.rented_vehicles

    def get_rental_summary(self, name=None):  # A method to write the summary of all rented vehicles with their costs
        # Allow passing a name in for non-interactive calls (helpful for tests)
        if name is None:
            name = input("Enter the name of the customer to see their rental summary: ").strip()

        if not name or name not in self.customer_dict:
            print("Invalid customer name entered or customer does not exist!")
            return

        rentals = self.rented_vehicles.get(name, [])
        if not rentals:
            print(f"{name} has no current rentals.")
            return []

        total_cost = 0.0
        print(f"Rental summary for {name}:")
        for rec in rentals:
            days = rec.get('days', 0)

            # Find the corresponding Vehicle instance (if available) so we can use
            # its calculate_rental_cost method which may include discounts/fees.
            matched_vehicle = None
            for v in self.vehicles:
                if v.make.lower() == rec.get('make', '').lower() and v.model.lower() == rec.get('model', '').lower():
                    matched_vehicle = v
                    break

            if matched_vehicle:
                try:
                    cost = matched_vehicle.calculate_rental_cost(days)
                except Exception:
                    # If a subclass implementation fails, fall back to stored price
                    cost = rec.get('price_per_day', 0) * days
            else:
                cost = rec.get('price_per_day', 0) * days

            total_cost += cost
            print(f" - {rec.get('make')} {rec.get('model')}: {days} days @ ${rec.get('price_per_day')} -> ${cost:.2f}")

        print(f"Total due: ${total_cost:.2f}")
        return rentals


vehicles = [
    Truck("ford", "f-150", 2021, 50.0, "2000lbs"),
    Motorcycle("Kawasaki", 'ninja', 2024, 32, '1000cc'),
    Truck("Scania", 'S-series', 2016, 62, '80000lbs' ),
    Car("Audi", "R8", 2022, 64, 4),
    Motorcycle("harley_Davidson", "sportster", 2022, 20.0, "600cc"),
    Car("toyota", "camry", 2020, 40.0, 4)

]

if __name__ == "__main__":
    System = RentalSystem(vehicles)
    while True:
        print("\n===============Vehicle Rental Menu====================")
        print("1. Add a new Customer")
        print("2. Show vehicle inventory")
        print("3. Rent a vehicle")
        print("4. Return a vehicle")
        print("5. Rental summary")
        print("6. Exit")
        choice = input("Enter a choice (1-6): ").strip()
        try:
            choice = int(choice)
        except ValueError:
            print("Choice must be a number between 1 and 6")
            # invalid input; prompt again
            continue

        # handle valid numeric choice
        if choice == 1:
            System.add_customer()
        elif choice == 2:
            System.available_vehicles()
        elif choice == 3:
            System.rent_vehicle()
        elif choice == 4:
            System.return_vehicle()
        elif choice == 5:
            System.get_rental_summary()
        elif choice == 6:
            print("Thank you! See you soon")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")
            continue

