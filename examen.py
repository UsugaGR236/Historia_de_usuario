# Inventory and Sales Management System for an Electronics Store
# All interactions are in English
# Simple modular version with reports and validations

import datetime

# -----------------------------------------
# Initial Data
# -----------------------------------------
inventory = {
    1: {"name": "Laptop Pro 14", "brand": "TechMaster", "category": "Computers",
        "price": 1200, "stock": 10, "warranty": 24},
    2: {"name": "Smartphone X10", "brand": "MobileOne", "category": "Phones",
        "price": 850, "stock": 15, "warranty": 12},
    3: {"name": "4K TV VisionMax", "brand": "VisionMax", "category": "TV",
        "price": 950, "stock": 7, "warranty": 36},
    4: {"name": "Gaming Headset G5", "brand": "SoundWave", "category": "Audio",
        "price": 120, "stock": 25, "warranty": 18},
    5: {"name": "Bluetooth Speaker Mini", "brand": "SoundWave", "category": "Audio",
        "price": 60, "stock": 30, "warranty": 12}
}

sales = []

# Lambda example: calculate net income after discount
calculate_net = lambda price, qty, discount: (price * qty) * (1 - discount)


# -----------------------------------------
# Inventory Functions
# -----------------------------------------

def add_product():
    try:
        name = input("Product name: ")
        brand = input("Brand: ")
        category = input("Category: ")
        price = float(input("Unit price: "))
        stock = int(input("Stock quantity: "))
        warranty = int(input("Warranty (months): "))

        if price <= 0 or stock < 0 or warranty < 0:
            print("Invalid values. Product not saved.")
            return

        new_id = max(inventory.keys()) + 1
        inventory[new_id] = {
            "name": name, "brand": brand, "category": category,
            "price": price, "stock": stock, "warranty": warranty
        }
        print("Product added successfully.")
    except:
        print("Invalid input. Product not registered.")


def view_inventory():
    for pid, data in inventory.items():
        print(pid, "-", data)


def update_product():
    try:
        pid = int(input("Enter product ID to update: "))
        if pid not in inventory:
            print("Product not found.")
            return

        print("Leave empty to keep current value.")
        for key in inventory[pid]:
            new_val = input(f"{key} ({inventory[pid][key]}): ")
            if new_val != "":
                if key in ["price", "stock", "warranty"]:
                    try:
                        new_val = float(new_val) if key == "price" else int(new_val)
                    except:
                        print("Invalid value. Skipping update for this field.")
                        continue
                inventory[pid][key] = new_val

        print("Product updated successfully.")
    except:
        print("Error updating product.")


def delete_product():
    try:
        pid = int(input("Enter product ID to delete: "))
        if pid in inventory:
            del inventory[pid]
            print("Product deleted.")
        else:
            print("Product not found.")
    except:
        print("Invalid ID.")


# -----------------------------------------
# Sales Functions
# -----------------------------------------

def register_sale():
    try:
        customer = input("Customer name: ")
        customer_type = input("Customer type (Regular / VIP): ").lower()

        pid = int(input("Product ID: "))
        if pid not in inventory:
            print("Product not found.")
            return

        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("Invalid quantity.")
            return

        if inventory[pid]["stock"] < quantity:
            print("Insufficient stock.")
            return

        # Discount depending on customer type
        discount = 0.1 if customer_type == "vip" else 0

        price = inventory[pid]["price"]
        net_total = calculate_net(price, quantity, discount)

        sale = {
            "customer": customer,
            "type": customer_type,
            "product": inventory[pid]["name"],
            "brand": inventory[pid]["brand"],
            "quantity": quantity,
            "date": datetime.date.today().isoformat(),
            "discount": discount,
            "gross": price * quantity,
            "net": net_total
        }

        sales.append(sale)

        inventory[pid]["stock"] -= quantity

        print("Sale registered successfully.")
    except:
        print("Error registering sale.")


def view_sales():
    for s in sales:
        print(s)


# -----------------------------------------
# Reports
# -----------------------------------------

def report_top_products():
    if not sales:
        print("No sales recorded.")
        return

    count_map = {}
    for s in sales:
        count_map[s["product"]] = count_map.get(s["product"], 0) + s["quantity"]

    top = sorted(count_map.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 best selling products:")
    for p, qty in top:
        print(f"{p}: {qty} units")


def report_sales_by_brand():
    brand_map = {}
    for s in sales:
        brand_map[s["brand"]] = brand_map.get(s["brand"], 0) + s["net"]

    print("Sales grouped by brand (net income):")
    for brand, total in brand_map.items():
        print(f"{brand}: {total}")


def report_income():
    gross = sum(s["gross"] for s in sales)
    net = sum(s["net"] for s in sales)
    print(f"Gross income: {gross}")
    print(f"Net income: {net}")


def report_inventory_performance():
    print("Inventory performance based on sold quantities:")
    sold_map = {}
    for s in sales:
        sold_map[s["product"]] = sold_map.get(s["product"], 0) + s["quantity"]

    for pid, data in inventory.items():
        sold = sold_map.get(data["name"], 0)
        print(f"{data['name']} - Sold: {sold}, Remaining stock: {data['stock']}")


# -----------------------------------------
# Main Menu
# -----------------------------------------

def main_menu():
    while True:
        print("\n--- Inventory and Sales Management System ---")
        print("1. Add product")
        print("2. View inventory")
        print("3. Update product")
        print("4. Delete product")
        print("5. Register sale")
        print("6. View sales")
        print("7. Report: Top 3 sold products")
        print("8. Report: Sales by brand")
        print("9. Report: Gross and net income")
        print("10. Report: Inventory performance")
        print("11. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            register_sale()
        elif choice == "6":
            view_sales()
        elif choice == "7":
            report_top_products()
        elif choice == "8":
            report_sales_by_brand()
        elif choice == "9":
            report_income()
        elif choice == "10":
            report_inventory_performance()
        elif choice == "11":
            print("Exiting system.")
            break
        else:
            print("Invalid option.")


# Program start
main_menu()