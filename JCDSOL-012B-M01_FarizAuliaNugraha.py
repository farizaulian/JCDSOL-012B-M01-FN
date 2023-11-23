# Capstone Project Module 1: JCDSOL-012B Fariz Aulia Nugraha
# Program Name: Laptop Warehouse Management System


# Warehouse stock data
warehouse_stock = [
    # Low-spec laptops
    {
        'InventoryNumber': 'P001', # Inv No.
        'SerialNumber': 'JC23B501', # Serial No. 
        'Model': 'JCDSOL012A',
        'Specifications': '4GB RAM, 256GB SSD, Core-i3',
        'Status': 'Available',
        'AssignedTo': None
    },
    {
        'InventoryNumber': 'P002',
        'SerialNumber': 'JC23B502',
        'Model': 'JCDSOL012A',
        'Specifications': '4GB RAM, 256GB SSD, Core-i3',
        'Status': 'Assigned',
        'AssignedTo': 'Jane Smith'
    },
    {
        'InventoryNumber': 'P003',
        'SerialNumber': 'JC23B503',
        'Model': 'JCDSOL012A',
        'Specifications': '4GB RAM, 256GB SSD, Core-i3',
        'Status': 'Assigned',
        'AssignedTo': 'Akira Oda'
    },

    # Mid-spec laptops
    {
        'InventoryNumber': 'P004',
        'SerialNumber': 'JC23B511',
        'Model': 'JCDSOL012B',
        'Specifications': '8GB RAM, 512GB SSD, Core-i5',
        'Status': 'Available',
        'AssignedTo': None
    },
    {
        'InventoryNumber': 'P005',
        'SerialNumber': 'JC23B512',
        'Model': 'JCDSOL012B',
        'Specifications': '8GB RAM, 512GB SSD, Core-i5',
        'Status': 'Available',
        'AssignedTo': None
    },
    {
        'InventoryNumber': 'P006',
        'SerialNumber': 'JC23B513',
        'Model': 'JCDSOL012B',
        'Specifications': '8GB RAM, 512GB SSD, Core-i5',
        'Status': 'Assigned',
        'AssignedTo': 'Akira Oda'
    },
    {
        'InventoryNumber': 'P007',
        'SerialNumber': 'JC23B514',
        'Model': 'JCDSOL012B',
        'Specifications': '8GB RAM, 512GB SSD, Core-i5',
        'Status': 'Available',
        'AssignedTo': None
    },

    # High-spec laptops
    {
        'InventoryNumber': 'P008',
        'SerialNumber': 'JC23B521',
        'Model': 'JCDSOL012C',
        'Specifications': '16GB RAM, 1TB SSD, Core-i7',
        'Status': 'Available',
        'AssignedTo': None
    },
    {
        'InventoryNumber': 'P009',
        'SerialNumber': 'JC23B522',
        'Model': 'JCDSOL012C',
        'Specifications': '16GB RAM, 1TB SSD, Core-i7',
        'Status': 'Available',
        'AssignedTo': None
    },
    {
        'InventoryNumber': 'P010',
        'SerialNumber': 'JC23B523',
        'Model': 'JCDSOL012C',
        'Specifications': '16GB RAM, 1TB SSD, Core-i7',
        'Status': 'Assigned',
        'AssignedTo': 'Liu Wei'
    }
]

def print_stock_list(stock_list):
    if not stock_list: # Check if the list is empty
        print("No stock data available.")
        return # Exit function
    print('Laptop Stock List\n')
    print('Inv No.\t| Serial No.\t| Model\t\t| Specifications\t\t| Status\t| Assigned To')
    for item in stock_list: 
        assigned_to = item['AssignedTo'] if item['AssignedTo'] else "None"
        print(f'{item["InventoryNumber"]}\t| {item["SerialNumber"]}\t| {item["Model"]}\t| {item["Specifications"]}\t| {item["Status"]}\t| {assigned_to}')

# Function to display the stock list
def display_stock_list():
    print('''
Choose the list to display:
1. All Stock List
2. Available Stock List
3. Assigned Stock List
''')
    choice = input("Select an option: ")
    
    if choice == '1':
        print_stock_list(warehouse_stock)
    elif choice == '2':
        available_stock = [item for item in warehouse_stock if item['Status'] == 'Available']
        print_stock_list(available_stock)
    elif choice == '3':
        assigned_stock = [item for item in warehouse_stock if item['Status'] == 'Assigned']
        print_stock_list(assigned_stock)
    else:
        print("Invalid option selected.")


# Function to generate the next inventory number
def generate_inventory_number():
    if not warehouse_stock:
        return 'P001'
    last_inv_number = warehouse_stock[-1]['InventoryNumber']
    last_seq = int(last_inv_number[1:])  # Extract the numerical part
    new_seq = f'{last_seq + 1:03}'  # Increment and keep leading zeros in 3 digit format
    return f'P{new_seq}'

# Function to print a single laptop's details in a tabular format
def print_laptop_details(laptop):
    assigned_to = laptop['AssignedTo'] if laptop['AssignedTo'] else "None"
    print('Inv No.\t| Serial No.\t| Model\t\t| Specifications\t\t| Status\t| Assigned To')
    print(f'{laptop["InventoryNumber"]}\t| {laptop["SerialNumber"]}\t| {laptop["Model"]}\t| {laptop["Specifications"]}\t| {laptop["Status"]}\t| {assigned_to}')

# Function to add a new stock item
def add_stock_item():
    print("\n--- Add New Laptop ---")
    inventory_number = generate_inventory_number()
    serial_number = input('Enter the serial number: ')
    
    # Check for duplicate serial number
    if any(item['SerialNumber'] == serial_number for item in warehouse_stock):
        print("A laptop with this serial number already exists in the warehouse.")
        return

    # Input for model
    model = input('Enter the laptop model: ')

    # Input for specifications
    ram_size = input('Enter RAM size (e.g., 16GB): ')
    ssd_size = input('Enter SSD storage size (e.g., 512GB): ')
    cpu_size = input('Enter CPU size (e.g., Core-i5): ')

    # Assemble the specifications string
    specifications = f'{ram_size} RAM, {ssd_size} SSD, {cpu_size}'

    # Since this is a new addition, the status will be 'Available' and 'AssignedTo' will be None
    status = 'Available'
    assigned_to = None

    # Data saving confirmation
    print("\nSave this data?")
    print("1. Yes")
    print("2. No")
    save_option = input("Choose an option: ")

    # Conditional logic based on user's choice to save data
    if save_option == '1':
        new_laptop = {
            'InventoryNumber': inventory_number,
            'SerialNumber': serial_number,
            'Model': model,
            'Specifications': specifications,
            'Status': status,
            'AssignedTo': assigned_to
        }
        warehouse_stock.append(new_laptop)
        print("Data successfully saved. Here are the details of the new laptop:")
        print_laptop_details(new_laptop)
    else:
        print("Data entry cancelled.")


# Function to update a stock item
def update_stock_item():
    print_stock_list(warehouse_stock) # Optional: Display the current stock list
    print("\n--- Update Laptop Stock ---")
    inventory_number = input('Enter the inventory number of the laptop to update: ')
    laptop_to_update = next((item for item in warehouse_stock if item['InventoryNumber'] == inventory_number), None) # Searching for matching data
    
    if not laptop_to_update:
        print("The data you are looking for does not exist.")
        return
    
    # Display the laptop data that corresponds to the serial number
    print_laptop_details(laptop_to_update)
    
    # Ask if user wants to continue update
    print("\nDo you want to continue updating this laptop's data?")
    print("1. Yes")
    print("2. No")
    continue_update = input("Choose an option: ")

    if continue_update == '1':
        # User chooses which detail to update
        print("Which detail would you like to update?")
        print("1. Model")
        print("2. Specifications")
        column_choice = input("Select the detail to update (enter the number): ")
        
        # User inputs new value
        new_value = input("Enter the new value: ")
        
        # Mapping user choice to dictionary key (useful for bigger data set with many columns)
        column_map = {
            '1': 'Model',
            '2': 'Specifications',
        }
        
        if column_choice in column_map:
            column_key = column_map[column_choice]
            # Confirm update
            print(f"Update {column_key} from '{laptop_to_update[column_key]}' to '{new_value}'?") #Corfirmation
            print("1. Yes")
            print("2. No")
            confirm_update = input("Confirm update (enter the number): ")
            
            if confirm_update == '1':
                # Updating data
                laptop_to_update[column_key] = new_value
                print("Data successfully updated.")
                print_laptop_details(laptop_to_update)
            else:
                print("Update cancelled.")
        else:
            print("Invalid option selected. Update cancelled.")
    else:
        print("Update cancelled.")


# Function to delete a stock item
def delete_stock_item():
    print_stock_list(warehouse_stock)  # Optional: Display the current stock list
    print("\n--- Delete Laptop ---")
    inventory_number = input('Enter the inventory number of the laptop to delete: ')

    # Find the laptop to delete by Inventory Number
    laptop_to_delete = next((item for item in warehouse_stock if item['InventoryNumber'] == inventory_number), None)

    # Check if laptop exists
    if laptop_to_delete is None:
        print("The data you are looking for does not exist.")
        return

    # Display the laptop details
    print("\nLaptop details:")
    print_laptop_details(laptop_to_delete)

    # Show data deletion option menu
    print("\nAre you sure you want to delete this laptop from the stock?")
    print("1. Yes")
    print("2. No")
    delete_option = input("Choose an option: ")

    # Confirm delete
    if delete_option == '1':
        # Find the index of the laptop to delete
        index_to_delete = warehouse_stock.index(laptop_to_delete)
        del warehouse_stock[index_to_delete]
        print("Data successfully deleted.")
    else:
        print("Data deletion cancelled.")


# --- New Additional Features ---


# Function to assign or unassign a laptop
def assign_or_unassign_laptop():
    print_stock_list(warehouse_stock)  # Optional: Display the current stock list
    inventory_number = input('Enter the inventory number of the laptop to assign/unassign: ')
    laptop = next((item for item in warehouse_stock if item['InventoryNumber'] == inventory_number), None)

    if not laptop:
        print("No laptop found with the given inventory number.")
        return
    
    # Initialize confirmation variables
    confirm_assignment = '0'  # Default value indicating no confirmation yet
    confirm_unassignment = '0'  # Default value indicating no confirmation yet
    
    # Display laptop details before making changes
    print("\nLaptop details:")
    print_laptop_details(laptop)
    
    # There are two possibilities
    # 1. Available
    if laptop['Status'] == 'Available':
        assigned_to = input('Enter the name of the person to assign this laptop to: ')
        if not assigned_to.strip():
            print("Invalid name. It cannot be empty.")
            return
        
        # Confirm assignment
        print(f"Assign laptop {inventory_number} to '{assigned_to}'?")
        print("1. Yes")
        print("2. No")
        confirm_assignment = input("Confirm assignment (enter the number): ")
        
        if confirm_assignment == '1':
            laptop['AssignedTo'] = assigned_to
            laptop['Status'] = 'Assigned'
            print("Laptop assigned successfully.")
        else:
            print("Assignment cancelled.")

    # 2. Assigned
    elif laptop['Status'] == 'Assigned':
        print(f"This laptop is currently assigned to {laptop['AssignedTo']}.")
        print("Do you want to unassign it?")
        print("1. Yes")
        print("2. No")
        unassign_option = input("Choose an option: ")

        if unassign_option == '1':
            # Confirm unassignment
            print(f"Unassign laptop {inventory_number} from '{laptop['AssignedTo']}'?")
            print("1. Yes")
            print("2. No")
            confirm_unassignment = input("Confirm unassignment (enter the number): ")
            
            if confirm_unassignment == '1':
                laptop['AssignedTo'] = None
                laptop['Status'] = 'Available'
                print("Laptop unassigned successfully.")
            else:
                print("Unassignment cancelled.")
        elif unassign_option == '2':
            print("No changes made.")


    # Display laptop details after making changes
    if confirm_assignment == '1' or confirm_unassignment == '1':
        print("\nUpdated laptop details:")
        print_laptop_details(laptop)


# Function to search for a stock item
def search_stock_item():
    print("\n--- Search Laptop Stock ---")
    print("Choose the category to search by:")
    print("1. All Categories")
    print("2. Serial Number")
    print("3. Model")
    print("4. Specifications")
    print("5. Status")
    print("6. Assigned To")
    search_choice = input("Select an option: ")

    search_term = input("Enter search term: ").lower()

    # Define the search function
    def is_match(item, term, category): # Search term in item's category 
        if category == 'all':
            return (term in item['SerialNumber'].lower() or
                    term in item['Model'].lower() or
                    term in item['Specifications'].lower() or
                    term in item['Status'].lower() or
                    (item['AssignedTo'] and term in item['AssignedTo'].lower())) # Search term in all item's categories
        else:
            return term in item[category].lower() # Search term in selected item's category only

    # Map the choice to category
    categories = {
        '1': 'all',
        '2': 'SerialNumber',
        '3': 'Model',
        '4': 'Specifications',
        '5': 'Status',
        '6': 'AssignedTo'
    }

    category = categories.get(search_choice, 'all') # Based on user's selection. Category/key

    found_items = [item for item in warehouse_stock if is_match(item, search_term, category)] # Need to fulfill is_match() condition
    
    if found_items:
        print("\nSearch Results:")
        print('Inv No.\t| Serial No.\t| Model\t\t| Specifications\t\t| Status\t| Assigned To')
        for item in found_items:
            assigned_to = item['AssignedTo'] if item['AssignedTo'] else "None"
            print(f'{item["InventoryNumber"]}\t| {item["SerialNumber"]}\t| {item["Model"]}\t| {item["Specifications"]}\t| {item["Status"]}\t| {assigned_to}')
    else:
        print("No laptops found matching the search criteria.")


# User authorization (demo)
authorized_users = {
    'admin': 'passw0rd',
    'fariz': 'passw0rd_FN'
}

# Function to handle user login
def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in authorized_users and authorized_users[username] == password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password. Please try again.")
            attempts -= 1
    return False


# Main menu function
def main_menu():
    while True:
        print('''
Welcome to the Laptop Warehouse Management System of Data Science Team

1. Display Laptop Stock List
2. Add New Laptop Stock
3. Update Laptop Information
4. Assign/unassign Laptop
5. Delete Laptop Stock
6. Search Laptop Stock
7. Exit Program
''')
        choice = input("Select an option: ")
        if choice == '1':
            display_stock_list()
        elif choice == '2':
            add_stock_item()
        elif choice == '3':
            update_stock_item()
        elif choice == '4':
            assign_or_unassign_laptop()
        elif choice == '5':
            delete_stock_item()
        elif choice == '6':
            search_stock_item()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("The option you entered is not valid. Please try again.")


# Starting point of the program (username: admin, password: passw0rd)
if login():
    main_menu()
else:
    print("Access denied. Exiting program.")
    


# # Starting point of the program (without login)
# main_menu()
