#Farn Xin Yang
#TP074541


#format for item and user
format_length = "{6:<9}\t{7:<{0}}\t{8:<{1}}\t{9:<{2}}\t{10:<{3}}\t{11:<{4}}\t{12:<{5}}"
format_length2 = "{13:<{14}}\t{6:<9}\t{7:<{0}}\t{8:<{1}}\t{9:<{2}}\t{10:<{3}}\t{11:<{4}}\t{12:<{5}}"
format_user = "{0:<{4}}\t{1:<{5}}\t{2:<{6}}\t{3}"


#check value is integer or not
def check_integer(i):
    try:
        int(i)
        return True
    except ValueError:
        return False


#check value is float or not
def check_float(i):
    try:
        float(i)
        return True
    except ValueError:
        return False


#read inventory from text file
def read_inventory():
    inventory_list = []
    inventory_file = open("inventory.txt", "r")
    for lines in inventory_file:
        line = lines.strip().split("\t")
        inventory_list.append(line)
    inventory_file.close()
    return inventory_list


#write inventory to text file
def write_inventory(inventory_list):
    inventory_file = open("inventory.txt", "w")
    for item in inventory_list:
        for details in item:
            inventory_file.write(details)
            inventory_file.write("\t")
        inventory_file.write("\n")
    inventory_file.close()


#add new item to text file
def add_inventory(inventory_info):
    inventory_file = open("inventory.txt", "a")
    for info in inventory_info:
        inventory_file.write(info)
        inventory_file.write("\t")
    inventory_file.write("\n")
    inventory_file.close()


#get category
def get_category():

    print("   Category:")

    category_list = []

    #read category from text file
    category_file = open("category.txt", "r")
    for lines in category_file:
        line = lines.strip()
        category_list.append(line)
    category_file.close()

    #print category
    for log, category in enumerate(category_list):
        print("      {}. {}".format(log+1, category))

    #get category
    while True:
        choice = input("   Enter Category   : ")
        if check_integer(choice):
            choice = int(choice)
            if 1 <= choice <= len(category_list):
                break
            else:
                print("      *Please enter value that available*")
        else:
            print("      *Please enter Integer*")

    category = category_list[choice-1]
    
    return category


#add new category
def add_category():

    print("Start add Category")

    category_list = []

    #read category from text file
    category_file = open("category.txt", "r")
    for lines in category_file:
        line = lines.strip()
        category_list.append(line)
    category_file.close()

    #get new category
    while True:
        target = True
        new_category = input("   Enter new Category: ")
        if new_category.isalpha():
            for category in category_list:
                if new_category == category:
                    target = False
            if target:
                break
            else:
                print("      *This Category already added*")
        else:
            print("      *Please enter Alphabet*")

    #add new category to text file
    category_file = open("category.txt", "a")
    category_file.write(new_category)
    category_file.write("\n")
    category_file.close()

    print("Add category successfully")


#show all category
def show_category():

    print("Start show category")

    category_list = []

    #read category from text file
    category_file = open("category.txt", "r")
    for lines in category_file:
        line = lines.strip()
        category_list.append(line)
    category_file.close()

    #print category
    for log, category in enumerate(category_list):
        print("   {}. {}".format(log+1, category))

    print("Show category successfully")


#delete category
def delete_category():

    print("Start delete category")

    category_list = []

    #read category from text file
    category_file = open("category.txt", "r")
    for lines in category_file:
        line = lines.strip()
        category_list.append(line)
    category_file.close()

    #print category
    for log, category in enumerate(category_list):
        print("   {}. {}".format(log+1, category))

    #get which category want delete
    while True:
        choice = input("   Which you want delete: ")
        if check_integer(choice):
            choice = int(choice)
            if 1 <= choice <= len(category_list):
                break
            else:
                print("      *Please enter value that available*")
        else:
            print("      *Please enter Integer*")
    
    choice -= 1

    target = category_list[choice]

    #delete category
    category_list.remove(target)

    #write category to text file
    category_file = open("category.txt", "w")
    for category in category_list:
        category_file.write(category)
        category_file.write("\n")
    category_file.close()

    print("Delete category successfully")


#length for format item
def item_length():
    inventory_list = read_inventory()
    description_length = 11
    category_length = 8
    unit_length = 4
    price_length = 5
    quantity_length = 8
    minimum_length = 7
    item_quantity = 3
    for item in inventory_list:
        if len(item[1]) > description_length:
            description_length = len(item[1])
        if len(item[2]) > category_length:
            category_length = len(item[2])
        if len(item[3]) > unit_length:
            unit_length = len(item[3])
        if len(item[4]) > price_length:
            price_length = len(item[4])
        if len(item[5]) > quantity_length:
            quantity_length = len(item[5])
        if len(item[6]) > minimum_length:
            minimum_length = len(item[6])
    if len(str(len(inventory_list))) > item_quantity:
        item_quantity = len(str(len(inventory_list)))
    return description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item_quantity


#length for foramt user
def user_length():
    username_length = 8
    password_length = 8
    user_quantity = 3
    user_list = []
    user_file = open("userdata.txt", "r")
    for lines in user_file:
        line = lines.strip().split("\t")
        user_list.append(line)
    user_file.close()
    for user in user_list:
        if len(user[0]) > username_length:
            username_length = len(user[0])
        if len(user[1]) > password_length:
            password_length = len(user[1])
    if len(str(len(user_list))) > user_quantity:
        user_quantity = len(str(len(user_list)))
    return username_length, password_length, user_quantity


#function insert new item
def insert_new_item():

    print("Start Insert New Item")

    while True:

        #get inventory list
        inventory_list = read_inventory()

        #get new item details
        while True:
            target = True
            item_code = input("   Enter Item Code  : ")
            if check_integer(item_code) and len(item_code) == 5:
                for item in inventory_list:
                    if item_code == item[0]:
                        target = False
                        print("      *This item code is already taken*")
                if target:
                    break
            else:
                print("      *Please enter 5 Digits Integer*")

        while True:
            target = True
            description = input("   Enter Description: ")
            for item in inventory_list:
                if description == item[1]:
                    target = False
            if target:
                break
            else:
                print("      *Description already given*")

        category = get_category()

        unit = input("   Enter Unit       : ")

        while True:
            price = input("   Enter Price      : ")
            if check_float(price):
                break
            else:
                print("      *Please enter Integer or Float*")

        while True:
            quantity = input("   Enter Quantity   : ")
            if check_integer(quantity):
                break
            else:
                print("      *Please enter Integer")

        while True:
            minimum = input("   Enter Minimum    : ")
            if check_integer(minimum):
                break
            else:
                print("      *Please enter Integer")

        #set item details as list
        inventory_info = [item_code, description, category, unit, price, quantity, minimum]

        #insert new item details to txt file
        add_inventory(inventory_info)

        #continue or terminate
        while True:
            print("Enter 1 to continue, 0 to terminate")
            choice = input("Choice: ")
            if check_integer(choice):
                choice = int(choice)
                if 0 <= choice <= 1:
                    break
                else:
                    print("   *Please enter 0 or 1*")
            else:
                print("   *Please enter Integer*")
        if choice == 0:
            break

    print("Item Inserted Successfully")


#function update item
def update_item():

    print("Start Update Item")

    #get inventory list
    inventory_list = read_inventory()

    #get item details length for format
    description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item_quantity = item_length()

    #get item code
    while True:
        target = None
        count = 0
        item_code = input("   Enter Item Code: ")
        if check_integer(item_code) and len(item_code) == 5:
            for item in inventory_list:
                if item_code == item[0]:
                    target = count
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum"), "*")
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6]), "*")
                count += 1
            if target is None:
                print("      *Item Code Not Found*")
            else:
                break
        else:
            print("      *Please enter 5 digits Integer*")
    
    print("   1. Item Code")
    print("   2. Description")
    print("   3. category")
    print("   4. Unit")
    print("   5. Price")
    print("   6. Quantity")
    print("   7. Minimum")

    #get which details to update
    while True:
        choice = input("   Enter your Choice: ")
        if check_integer(choice):
            choice = int(choice)
            if 1 <= choice <= 7:
                break
            else:
                print("      *Please enter 1 to 7")
        else:
            print("      *Please enter Integer*")

    #update new value to list
    def change_item_list(which_change):
        item = inventory_list[target]
        item[which_change] = new_value
     
    if choice == 1:
        while True:
            temp = True
            new_value = input("   Please enter New Value: ")
            if check_integer(new_value) and len(new_value) == 5:
                for item in inventory_list: 
                    if new_value == item[0]:
                        temp = False
                        print("      *This item code is already taken*")
                if temp:
                    break
            else:
                print("      *Please enter 5 digits Integer")
        change_item_list(0)
    elif choice == 2:
        while True:
            temp = True
            new_value = input("   Please enter New Value: ")
            for item in inventory_list:
                if new_value == item[1]:
                    temp = False
                    print("      *This description is already taken")
            if temp:
                break
        change_item_list(1)
    elif choice == 3:
        category = get_category()
        new_value = category
        change_item_list(2)
    elif choice == 4:
        new_value = input("   Please enter New Value: ")
        change_item_list(3)
    elif choice == 5:
        while True:
            new_value = input("   Please enter New Value: ")
            if check_float(new_value):
                break
            else:
                print("      *Please enter float")
        change_item_list(4)
    elif choice == 6:
        while True:
            new_value = input("   Please enter New Value: ")
            if check_integer(new_value):
                break
            else:
                print("      *Please enter Integer*")
        change_item_list(5)
    elif choice == 7:
        while True:
            new_value = input("   Please enter New Value: ")
            if check_integer(new_value):
                break
            else:
                print("      *Please enter Integer")
        change_item_list(6)
    
    #update item to txt file
    write_inventory(inventory_list)

    print("Update Successfully")


#function delete item
def delete_item():

    print("Start Delete Item")

    #get inventory list
    inventory_list = read_inventory()

    #get item details length for format
    description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item_quantity = item_length()

    #get item code and print out item
    while True:
        target = None
        item_code = input("   Enter Item Code: ")
        if check_integer(item_code) and len(item_code) == 5:
            for item in inventory_list:
                if item_code == item[0]:
                    target = item
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum"), "*")
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6]), "*")
            if target is None:
                print("      *Item Code Not Found*")
            else:
                break
        else:
            print("      *Please enter 5 digits Integer*")

    print("   Do you want Delete?")
    print("   1. Yes")
    print("   2. No")

    #check is that want to delete
    while True:
        choice = input("   Enter your choice: ")
        if check_integer(choice):
            choice = int(choice)
            if choice == 1 or choice == 2:
                break
            else:
                print("      *Please enter 1 or 2*")
        else:
            print("      *Please enter Integer*")

    #delete item
    if choice == 1:
        inventory_list.remove(target)
        write_inventory(inventory_list)

    print("Item Delete Successfully")


#function stock staking
def stock_taking():
    
    print("Start Stock Taking")

    #get inventory list
    inventory_list = read_inventory()

    #get item details length for format
    description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item_quantity = item_length()

    #get item code and print out item
    while True:
        target = None
        count = 0
        item_code = input("   Enter Item Code: ")
        if check_integer(item_code) and len(item_code) == 5:
            for item in inventory_list:
                if item_code == item[0]:
                    target = count
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum"), "*")
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6]), "*")
                count += 1
            if target is None:
                print("      *Item Code Not Found*")
            else:
                break
        else:
            print("      *Please enter 5 digits Integer*")

    print("   Do you want change Quantity?")
    print("   1. Yes")
    print("   2. No")

    #make sure want change quantity or not
    while True:
        choice = input("   Enter your Choice: ")
        if check_integer(choice):
            choice = int(choice)
            if 1 <= choice <= 2:
                break
            else:
                print("      *Please enter 1 or 2*")
        else:
            print("      *Please enter Integer*")

    #change quantity
    if choice == 1:
        while True:
            new_quantity = input("   New Quantity : ")
            if check_integer(new_quantity):
                break
            else:
                print("      *Please enter Integer*")
        item = inventory_list[target]
        item[5] = new_quantity
        write_inventory(inventory_list)

    print("Stock Taking Successfully")


#function view replenish list
def view_replenish_list():

    replenish_list = []

    print("Start view replenish list")

    #get inventory list
    inventory_list = read_inventory()

    #get item details length for format
    description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item_quantity = item_length()

    #append item that need replenish to list
    for item in inventory_list:
        if int(item[5]) < int(item[6]):
            replenish_list.append(item)

    #sorting list by item code
    replenish_list.sort(key=lambda item: int(item[0]))

    #print out list
    if len(replenish_list) == 0:
        print("No item need replenish")
    else:
        print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum", "No.", item_quantity), "*")
        for log, item in enumerate(replenish_list):
            print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6], log+1, item_quantity), "*")
        print("View replenish list successfully")


#function stock replenishment
def stock_replenishment():

    print("Start stock replenishment")

    #get inventory list
    inventory_list = read_inventory()

    #get item details length for format
    description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item_quantity = item_length()

    #get item code and print out
    while True:
        target = None
        count = 0
        item_code = input("   Enter item code: ")
        if check_integer(item_code) and len(item_code) == 5:
            for item in inventory_list:
                if item_code == item[0]:
                    target = count
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum"), "*")
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6]), "*")
                count += 1
            if target is None:
                print("      *Item Code Not Found*")
            else:
                break
        else:
            print("      *Please enter 5 digits Integer*")

    #get add value
    while True:
        add_value = input("   How many stock you want add: ")
        if check_integer(add_value):
            break
        else:
            print("      *Please enter Integer*")

    #update list
    item = inventory_list[target]
    total = int(item[5]) + int(add_value)
    item[5] = str(total)

    #update text file
    write_inventory(inventory_list)

    print("Stock Replenishment Successfully")


#function search items
def search_items():

    print("Start search item")

    #get inventory list
    inventory_list = read_inventory()

    #get item details length for format
    description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item_quantity = item_length()

    print("   Search methods: ")
    print("   1. Description")
    print("   2. Code Range")
    print("   3. Category")
    print("   4. Price Range")

    #get search methods
    while True:
        choice = input("   Enter your choice: ")
        if check_integer(choice):
            choice = int(choice)
            if 1 <= choice <= 4:
                break
            else:
                print("      *Please enter 1 to 4*")
        else:
            print("      *Please enter integer*")

    #search by description
    if choice == 1:

        #get description and print out
        while True:
            description = input("   Enter description: ")
            target = True
            for item in inventory_list:
                if description == item[1]:
                    target = False
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum"), "*")
                    print("      *", format_length.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6]), "*")
            if target:
                print("      *Item not found*")
            else:
                break

    #search by code range
    elif choice == 2:

        target = None

        #get start item code
        while True:
            from_item_code = input("   From? : ")
            if check_integer(from_item_code) and len(from_item_code) == 5:
                from_item_code = int(from_item_code)
                break
            else:
                print("      *Please enter 5 digits Integer*")

        #get end item code
        while True:
            to_item_code = input("   To? : ")
            if check_integer(to_item_code) and len(to_item_code) == 5:
                to_item_code = int(to_item_code)
                break
            else:
                print("      *Please enter 5 digits Integer*")

        #change position if from item code bigger than to item code
        if from_item_code > to_item_code:
            from_item_code, to_item_code = to_item_code, from_item_code

        i = from_item_code

        while from_item_code <= to_item_code:
            for item in inventory_list:
                if from_item_code == int(item[0]):
                    target = 1
            from_item_code += 1

        #print out item
        if target is None:
            print("      *Item Not Found*")
        else:
            from_item_code = i
            log = 1
            print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum", "No.", item_quantity), "*")
            while from_item_code <= to_item_code:
                for item in inventory_list:
                    if from_item_code == int(item[0]):
                        print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6], log, item_quantity), "*")
                        log += 1
                from_item_code += 1

    #search by category
    elif choice == 3:

        item_found = []

        #get category
        category = get_category()

        #append item that in this category
        for item in inventory_list:
            if category == item[2]:
                item_found.append(item)

        #sorting item with item code
        item_found.sort(key=lambda item: int(item[0]))

        #print out item
        if len(item_found) == 0:
            print("      *Item Not Found")
        else:
            print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum", "No.", item_quantity), "*")
            for log, item in enumerate(item_found):
                print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6], log+1, item_quantity), "*")

    #search by price range
    elif choice == 4:

        item_found = []

        #get start price
        while True:
            from_price = input("   From? : ")
            if check_float(from_price):
                from_price = float(from_price)
                break
            else:
                print("      *Please enter Integer or Float")

        #get end price
        while True:
            to_price = input("   To? : ")
            if check_float(to_price):
                to_price = float(to_price)
                break
            else:
                print("      *Please enter Integer or Float")

        #if start price bigger than end price change position
        if from_price > to_price:
            from_price, to_price = to_price, from_price

        #append item that in this price range to list
        for item in inventory_list:
            if from_price <= float(item[4]) <= to_price:
                item_found.append(item)

        #sorting item by price
        item_found.sort(key=lambda item: float(item[4]))

        #print out item
        if len(item_found) == 0:
            print("      *item not found")
        else:
            print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, "Item Code", "Description", "Category", "Unit", "Price", "Quantity", "Minimum", "No.", item_quantity), "*")
            for log, item in enumerate(item_found):
                print("      *", format_length2.format(description_length, category_length, unit_length, price_length, quantity_length, minimum_length, item[0], item[1], item[2], item[3], item[4], item[5], item[6], log + 1, item_quantity), "*")

    print("Search Items Successfully")


#function add new user
def add_new_user():

    print("Start add new user")

    user_list = []

    #append user from file to list
    user_file = open("userdata.txt", "r")
    for lines in user_file:
        line = lines.strip().split("\t")
        user_list.append(line)
        user_list.append("\n")
    user_file.close()

    #get new user username
    while True:
        target = None
        username = input("   Enter new username: ")
        for user in user_list:
            if username == user[0]:
                print("      *Username already taken*")
                target = 1
        if target is None:
            break

    #get new user password
    while True:
        password = input("   Enter password: ")
        confirm_password = input("   Confirm Password: ")
        if password == confirm_password:
            break
        else:
            print("      *Password did not match*")

    print("   User Type")
    print("   1. Admin")
    print("   2. Inventory Checker")
    print("   3. Purchaser")

    #get new user access
    while True:
        choice = input("   Enter your choice: ")
        if check_integer:
            choice = int(choice)
            if 1 <= choice <= 3:
                break
            else:
                print("      *Please enter 1 to 3*")
        else:
            print("      *Please enter Integer")

    #set user data as list
    userdata_info = [username, password, str(choice)]

    #add new user data to text file
    userdata_file = open("userdata.txt", "a")
    for details in userdata_info:
        userdata_file.write(details)
        userdata_file.write("\t")
    userdata_file.write("\n")
    userdata_file.close()

    print("User added successfully")


#function show all user
def show_user():

    print("Start show user")

    user_list = []

    #get user details length for format
    username_length, password_length, user_quantity = user_length()

    #read userdata from file to list
    user_file = open("userdata.txt", "r")
    for lines in user_file:
        line = lines.strip().split("\t")
        user_list.append(line)
    user_file.close()

    #print out user
    log = 1
    print("   ", format_user.format("No.", "Username", "Password", "Access", user_quantity, username_length, password_length))
    for user in user_list:
        if user[2] == "1":
            profile = "admin"
        elif user[2] == "2":
            profile = "inventory checker"
        elif user[2] == "3":
            profile = "purchaser"
        print("   ", format_user.format(log, user[0], user[1], profile, user_quantity, username_length, password_length))
        log += 1
        
    print("Show user successfully")


#function delete user
def delete_user():

    print("Start delete user")

    user_list = []

    #get user details length for format
    username_length, password_length, user_quantity = user_length()

    #read userdata from file to list
    user_file = open("userdata.txt", "r")
    for lines in user_file:
        line = lines.strip().split("\t")
        user_list.append(line)
    user_file.close()

    #print user
    log = 1
    print("   ", format_user.format("No.", "Username", "Password", "Access", user_quantity, username_length, password_length))
    for user in user_list:
        if user[2] == "1":
            profile = "admin"
        elif user[2] == "2":
            profile = "inventory checker"
        elif user[2] == "3":
            profile = "purchaser"
        print("   ", format_user.format(log, user[0], user[1], profile, user_quantity, username_length, password_length))
        log += 1

    #get which to delete
    while True:
        choice = input("   Which you want delete: ")
        if check_integer(choice):
            choice = int(choice)
            if 2 <= choice <= len(user_list):
                break
            elif choice == 1:
                print("      *This user cannot be delete*")
                if len(user_list) == 1:
                    break
            else:
                print("      *Please enter available value*")
        else:
            print("      *Please enter Integer*")

    choice -= 1

    #delete user
    if len(user_list) != 1:
        target = user_list[choice]
        user_list.remove(target)

        #update new data to text file
        user_file = open("userdata.txt", "w")
        for user in user_list:
            for details in user:
                user_file.write(details)
                user_file.write("\t")
            user_file.write("\n")
        user_file.close()

    print("User delete successfully")


#function edit user
def edit_user():

    print("Start edit user")
    
    user_list = []

    #get user data length for format
    username_length, password_length, user_quantity = user_length()

    #read user from file to list
    user_file = open("userdata.txt", "r")
    for lines in user_file:
        line = lines.strip().split("\t")
        user_list.append(line)
    user_file.close()

    #print user
    log = 1
    print("   ", format_user.format("No.", "Username", "Password", "Access", user_quantity, username_length, password_length))
    for user in user_list:
        if user[2] == "1":
            profile = "admin"
        elif user[2] == "2":
            profile = "inventory checker"
        elif user[2] == "3":
            profile = "purchaser"
        print("   ", format_user.format(log, user[0], user[1], profile, user_quantity, username_length, password_length))
        log += 1

    #get which user want to edit
    while True:
        choice = input("Which you want edit: ")
        if check_integer(choice):
            choice = int(choice)
            if 1 <= choice <= len(user_list):
                break
            else:
                print("   *Please enter available value*")
        else:
            print("   *Please enter Integer*")

    target = choice - 1

    print("   1. Username")
    print("   2. Password")
    print("   3. Access")

    #get want edit which data
    while True:
        choice = input("Enter your choice: ")
        if check_integer(choice):
            choice = int(choice)
            if 1 <= choice <= 3:
                if target == 0 and choice == 3:
                    print("      *This User Access cannot edit*")
                else:
                    break
            else:
                print("      *Please enter 1 to 3*")
        else:
            print("      *Please enter Integer")

    #edit username
    if choice == 1:
        while True:
            check = 0
            username = input("   Enter new username: ")
            for user in user_list:
                if username == user[0]:
                    print("      *This Username already taken")
                    check = 1
            if check == 0:
                user_list[target][0] = username
                break

    #edit password
    elif choice == 2:
        while True:
            password = input("   Enter new password: ")
            confirm_password = input("   Confirm password: ")
            if password == confirm_password:
                user_list[target][1] = password
                break
            else:
                print("      *Password Not Match*")

    #edit access
    elif choice == 3:
        print("      1. Admin")
        print("      2. inventory_checker")
        print("      3. purchaser")
        while True:
            choice = input("   Enter your choice: ")
            if check_integer(choice):
                choice = int(choice)
                if 1 <= choice <= 3:
                    break
                else:
                    print("      *Please enter 1 to 3*")
            else:
                print("      *Please enter Integer*")
        user_list[target][2] = str(choice)

    #update text file
    user_file = open("userdata.txt", "w")
    for user in user_list:
        for details in user:
            user_file.write(details)
            user_file.write("\t")
        user_file.write("\n")
    user_file.close()


#admin profile
def admin():
    while True:

        #home page
        print()
        print("-----------------------------------------")
        print("Welcome to Grocery Store Inventory System")
        print("   1. Insert New Item")
        print("   2. Update Item")
        print("   3. Delete Item")
        print("   4. Stock Taking")
        print("   5. View Replenish List")
        print("   6. Stock Replenishment")
        print("   7. Search Items")
        print("   8. Show Category")
        print("   9. Add Category")
        print("   10. Delete Category")
        print("   11. Show all user")
        print("   12. Add new user")
        print("   13. Delete user")
        print("   14. Edit User")
        print("   15. Logout")
        choice = (input("Enter Your Choice: "))
        print("-----------------------------------------")
        print()

        #check is which choice 
        if choice == "1":
            insert_new_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            stock_taking()
        elif choice == "5":
            view_replenish_list()
        elif choice == "6":
            stock_replenishment()
        elif choice == "7":
            search_items()
        elif choice == "8":
            show_category()
        elif choice == "9":
            add_category()
        elif choice == "10":
            delete_category()
        elif choice == "11":
            show_user()
        elif choice == "12":
            add_new_user()
        elif choice == "13":
            delete_user()
        elif choice == "14":
            edit_user()
        elif choice == "15":
            print("   Thank You for using Grocery Store Inventory System")
            print()
            print("-----------------------------------------")
            return main_program()
        else:
            print("   Invalid Value")


#inventory checker profile
def inventory_checker():
    while True:

        #home page
        print()
        print("-----------------------------------------")
        print("Welcome to Grocery Store Inventory System")
        print("   1. Stock Taking")
        print("   2. Search Items")
        print("   3. Logout")
        choice = (input("Enter Your Choice: "))
        print("-----------------------------------------")
        print()

        #check is which choice 
        if choice == "1":
            stock_taking()
        elif choice == "2":
            search_items()
        elif choice == "3":
            print("   Thank You for using Grocery Store Inventory System")
            print()
            print("-----------------------------------------")
            return main_program()
        else:
            print("   Invalid Value")


#purchase profile
def purchaser():
    while True:

        #home page
        print()
        print("-----------------------------------------")
        print("Welcome to Grocery Store Inventory System")
        print("   1. View Replenish List")
        print("   2. Stock Replenishment")
        print("   3. Search Items")
        print("   4. Logout")
        choice = (input("Enter Your Choice: "))
        print("-----------------------------------------")
        print()

        #check is which choice 
        if choice == "1":
            view_replenish_list()
        elif choice == "2":
            stock_replenishment()
        elif choice == "3":
            search_items()
        elif choice == "4":
            print("   Thank You for using Grocery Store Inventory System")
            print()
            print("-----------------------------------------")
            return main_program()
        else:
            print("   Invalid Value")


def main_program():

    user_list = []

    #read user from file to list
    user_file = open("userdata.txt", "r")
    for lines in user_file:
        line = lines.strip().split("\t")
        user_list.append(line)
    user_file.close()

    print()
    print("      *USER LOGIN*")

    #get username and password to login
    while True:
        username = input("   Username: ")
        password = input("   Password: ")
        count = 0
        target = None
        for user in user_list:
            if username == user[0] and password == user[1]:
                target = count
            count += 1
        if target is None:
            print("      *Invalid Username or Password")
        else:
            break

    #follow user access to enter profile
    if user_list[target][2] == "1":
        admin()
    elif user_list[target][2] == "2":
        inventory_checker()
    elif user_list[target][2] == "3":
        purchaser()


main_program()
