# 🚗 **Vehicle Rental System — CLI Application**  
### *A Python-based Command-Line Vehicle Rental Management System*

---

## ✅ Overview

The **Vehicle Rental System** is a fully functional, object-oriented command-line application designed to manage vehicle rentals for customers. Built entirely in Python, it supports multiple vehicle types (Cars, Trucks, Motorcycles), customer management, rental tracking, cost calculation with dynamic pricing rules, and return processing — all through an intuitive text-based interface.

This system is ideal for small-to-medium rental agencies seeking a lightweight, no-database, code-first solution for managing daily operations.

---

## 🧩 Core Features

| Feature | Description |
|--------|-------------|
| **Vehicle Inventory** | Manages multiple vehicle types with unique attributes (doors, payload, engine size). |
| **Dynamic Pricing** | Applies discounts (e.g., 10% off for rentals >7 days) or surcharges (e.g., +$20 for <3 days). |
| **Customer Management** | Add, identify, and track customers by name and license number. |
| **Rental Tracking** | Records each rental with make, model, days, price, and timestamp. |
| **Return Processing** | Matches returned vehicles to customer records and removes them from active rentals. |
| **Rental Summary** | Calculates total cost using vehicle-specific logic and displays detailed breakdown. |
| **Interactive Menu** | User-friendly CLI menu with input validation and error handling. |

---

## 🏗️ System Architecture

### 🔹 Vehicle Hierarchy (Inheritance)

```plaintext
Vehicle (Parent)
├── Car
│   └── Additional: num_doors
│   └── Pricing: 10% discount if rented >7 days
├── Truck
│   └── Additional: payload_capacity
│   └── Pricing: +$20 surcharge if rented <3 days
└── Motorcycle
    └── Additional: engine_size
    └── Pricing: Flat $15/day (ignores base price)
```

Each vehicle type inherits core properties (`make`, `model`, `year`, `rental_price`) and overrides `calculate_rental_cost(days)` to apply business rules.

### 🔹 Core Classes

| Class | Purpose |
|-------|---------|
| `Vehicle` | Base class with common attributes and methods. |
| `Car`, `Truck`, `Motorcycle` | Specialized subclasses with unique features and pricing logic. |
| `RentalSystem` | Main controller managing customers, inventory, rentals, and menu logic. |

---

## 📊 Data Model

Each rental is stored as a dictionary in the customer’s rental list:

```python
{
    'make': 'ford',
    'model': 'f-150',
    'days': 5,
    'price_per_day': 50.0,
    'rented_on': '2025-04-05 14:30'
}
```

- **Customer data**: Stored in `customer_dict` → `{name: license_number}`
- **Rental records**: Stored in `rented_vehicles` → `{name: [list of rental dicts]}`

> 💡 No external database — all data persists only during runtime (ideal for demos or small-scale use).

---

## 🔁 User Workflow

### 1. **Add Customer**
```bash
Enter the number of customers you would like to add: 1
Enter the name of the customer: Fidelis
Enter the customer's license number: 9854
✅ Fidelis added successfully.
```

### 2. **View Inventory**
```bash
Available Vehicles in Inventory:
--------------------------------
Total vehicles: 6

1. Make: ford, Model: f-150, Year: 2021, Rental Price: 50.0, Payload Capacity: 2000lbs
2. Make: Kawasaki, Model: ninja, Year: 2024, Rental Price: 32, Engine Size: 1000cc
...
```

### 3. **Rent a Vehicle**
```bash
Enter the name of the customer: Fidelis
Enter the number of vehicles you wish to rent: 2
Enter the model or make: f-150 → ✅ Found
Enter the number of days: 10
Enter the model or make: camry → ✅ Found
Enter the number of days: 5

✅ All rentals for Fidelis:
[
  {'make': 'ford', 'model': 'f-150', 'days': 10, 'price_per_day': 50.0, 'rented_on': '2025-04-05 14:30'},
  {'make': 'toyota', 'model': 'camry', 'days': 5, 'price_per_day': 40.0, 'rented_on': '2025-04-05 14:30'}
]
```

### 4. **Return a Vehicle**
```bash
Enter the name of the customer returning the vehicle: Fidelis
Enter the model or make: f-150
✅ Ford F-150 has been returned by Fidelis on 2025-04-05 15:00:00
```

### 5. **Rental Summary**
```bash
Enter the name of the customer: Fidelis
Rental summary for Fidelis:
 - ford f-150: 10 days @ $50.0 -> $450.00 (10% discount applied)
 - toyota camry: 5 days @ $40.0 -> $200.00
Total due: $650.00
```

> 💡 **Pricing Logic Applied**:  
> - `f-150` rented for 10 days → `50 * 10 = 500 → 500 * 0.9 = 450`  
> - `camry` rented for 5 days → `40 * 5 = 200` (no discount)

---

## 🛠️ Technical Implementation

### ✅ Object-Oriented Design
- Uses **inheritance** to model different vehicle types.
- Encapsulates data and behavior within classes.
- Separates concerns: `Vehicle` handles data, `RentalSystem` handles logic.

### ✅ Input Validation
- Validates numeric inputs (days, license number).
- Handles case-insensitive vehicle matching (`f-150` == `F-150`).
- Prevents crashes with `try/except` on user input errors.

### ✅ Dynamic Cost Calculation
- Each vehicle type implements its own `calculate_rental_cost(days)` method.
- Rental summary uses the **actual vehicle’s method** (not stored price) for accuracy.

### ✅ No External Dependencies
- Pure Python — no databases, no frameworks, no APIs.
- Runs on any system with Python 3.6+.

---

## 📌 Use Cases

| Scenario | How the System Helps |
|--------|----------------------|
| **Small Rental Agency** | Manages daily rentals without investing in expensive software. |
| **Educational Demo** | Teaches OOP, inheritance, CLI design, and data modeling. |
| **Prototype for MVP** | Fast to extend — add insurance, payment, or export to CSV. |
| **Internal Tool** | Track rentals for fleet managers using simple terminal access. |

---

## ⚠️ Limitations

| Limitation | Note |
|----------|------|
| **No Persistence** | Data resets after program exit. Add JSON/CSV export for production. |
| **No Authentication** | Any user can access all functions. Add login for multi-user environments. |
| **Single-User Interface** | Designed for one operator at a time. |
| **Case Sensitivity in Names** | Customer names are case-sensitive (e.g., "Fidelis" ≠ "fidelis"). |

---

## 🚀 Future Enhancements

- ✅ Save/load customer and rental data to/from JSON file  
- ✅ Add payment processing simulation (e.g., deposit, total due)  
- ✅ Generate printable receipts  
- ✅ Support multiple concurrent users via file locking or SQLite  
- ✅ Add GUI using `tkinter` or `streamlit`  
- ✅ Integrate SMS/email notifications for rentals/returns  

---

## 🧪 How to Run

1. **Save** the code as `vehicle_rental.py`
2. **Open terminal** and navigate to the directory
3. **Run**:

```bash
python vehicle_rental.py
```

4. Follow the interactive menu prompts.

---

## ✅ Sample Output (Summary)

```
===============Vehicle Rental Menu====================
1. Add a new Customer
2. Show vehicle inventory
3. Rent a vehicle
4. Return a vehicle
5. Rental summary
6. Exit
Enter a choice (1-6): 5
Enter the name of the customer: Fidelis
Rental summary for Fidelis:
 - ford f-150: 10 days @ $50.0 -> $450.00
 - toyota camry: 5 days @ $40.0 -> $200.00
Total due: $650.00
```

---

## 💡 Why This System Stands Out

> “A fully functional, clean, and educational vehicle rental system — built without a database, using only core Python and object-oriented principles.”

Perfect for:
- Students learning OOP  
- Developers building CLI tools  
- Small businesses needing a simple rental tracker  

---

**© 2025 Fidelis Mwiti — Vehicle Rental System v1.0**  
*Built with Python. Designed for clarity. Engineered for real-world use.*
