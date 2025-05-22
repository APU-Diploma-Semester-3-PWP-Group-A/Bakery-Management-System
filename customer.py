import os, time, custom_modules.reusableFunctions as rFunctions, sharedFunctions as sFunctions
from datetime import datetime

# (C)(i) Customer Page
def customerHomePage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "="*40)
        print("Customer Home Page".center(40))
        print("="*40 + f"{rFunctions.color('reset', None)}")
        print(f"Welcome {username},") 
        print("1. 👤 Account Management")
        print("2. 🌐 Product Browsing")
        print("3. 🛒 Cart Management")
        print("4. 📋 Order Tracking") 
        print("5. ⭐ Product Review")
        print("6. 🔒 Log Out")
        print("-"*40)
        try:
            customerMain = input("Enter selection: ").lower()
            if customerMain.isdigit(): #if functionality consist of all digits
                customerMain = int(customerMain)
            if customerMain in [1, "account management", "1. account management"]:
                newUsername = accountManagementPage(username)
                username = newUsername
            elif customerMain in [2, "product browsing", "2. product browsing"]:
                productBrowsingPage(username)
            elif customerMain in [3, "cart management", "3. cart management"]:
                cartManagementPage(username)
            elif customerMain in [4, "order tracking", "4. order tracking"]:
                orderTrackingPage(username)
            elif customerMain in [5, "product review", "5. product review"]:
                productReviewPage(username)
            elif customerMain in [6, "log out", "6. log out"]:
                rFunctions.clearPreviousLine()
                while True: #to keep confirm log out until get 'yes' or 'no'
                    try:
                        confirm = input("Enter <YES> to confirm log out or <NO> to cancel:").lower()
                        if confirm == "yes":
                            logOut = True
                            break
                        elif confirm == "no":
                            logOut = False
                            break
                        else:
                            raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                        rFunctions.clearPreviousLine()
                if logOut:
                    break
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

# Functionality 01: Account Management
def accountManagementPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40)
        print("Account Management".center(40))
        print("-"*40 + f"{rFunctions.color('reset', None)}")
        print("1. 📝 Update Personal Information")
        print("2. 🔑 Change Password") 
        print("3. 🔙 Back")
        print("-"*40)
        try:
            accountManagement = input("Enter selection: ").lower()
            if accountManagement.isdigit(): #if functionality consist of all digits
                accountManagement = int(accountManagement)
            if accountManagement in [1, "update personal information", "1. update personal information"]:
                newUsername = accountUpdatePersonalInformationPage(username)
                username = newUsername
            elif accountManagement in [2, "change password", "2. change password"]:
                accountChangePasswordPage(username)
            elif accountManagement in [3, "back", "3. back"]:
                return username
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

# (i) Update Personal Information
def accountUpdatePersonalInformationPage(username):
    while True:
        customersDict = rFunctions.readFile("customer")
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Personal Information".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                print(f"User ID: {customer['id']}")
                print(f"1. Name: {customer['name']}")
                print(f"2. Username: {customer['username']}")
                print(f"3. Age: {customer['age']}")
                print(f"4. Gender: {customer['gender']}")
                print(f"5. Phone number: {customer['phone number']}")
                print(f"6. Email: {customer['email']}")
                print(f"7. Address: {customer['address']}")
                print("-" * 40)
                usernameChanges = False
                if not rFunctions.askContinue():
                    return username
                rFunctions.clearPreviousLine()
                try:
                    updatePersonalInformationSelection = input("Enter the number of the field you want to update: ")
                    if updatePersonalInformationSelection.isdigit(): #if functionality consist of all digits
                        updatePersonalInformationSelection = int(updatePersonalInformationSelection)
                    if updatePersonalInformationSelection == 1:
                        rFunctions.clearPreviousLine()
                        customer['name'] = input("Enter new name: ")
                    elif updatePersonalInformationSelection == 2:
                        rFunctions.clearPreviousLine()
                        newUsername = input("Enter new username: ")
                        errorMsg, validUsername = rFunctions.validData(username = newUsername)
                        if not validUsername:
                            raise ValueError(f"{errorMsg} ☹️") 
                        if newUsername != username:
                            if rFunctions.checkUniqueData("customer", "username", newUsername, customersDict):
                                raise ValueError(f"Username already exists ☹️! Please try another one.{rFunctions.color('reset', None)}")
                            else:
                                customer['username'] = newUsername
                                usernameChanges = True
                        elif newUsername == username:
                            raise ValueError("Your new username cannot be the same as the old username ☹️")
                    elif updatePersonalInformationSelection == 3:
                        rFunctions.clearPreviousLine()
                        age = int(input("Enter new age: "))
                        if age <= 0:
                            raise ValueError(f"Invalid age ☹️ : Age cannot be 0 years old or negative.")
                        else:
                            customer['age'] = age
                    elif updatePersonalInformationSelection == 4:
                        rFunctions.clearPreviousLine()
                        gender = input("Enter new gender: ").capitalize()
                        errorMsg, validGender = rFunctions.validData(gender = gender)
                        if not validGender:
                            raise ValueError(f"Invalid gender ☹️ : {errorMsg}")
                        else:
                            customer['gender'] = gender
                    elif updatePersonalInformationSelection == 5:
                        rFunctions.clearPreviousLine()
                        phoneNum = input("Enter new phone number: ")
                        errorMsg, validPhoneNum = rFunctions.validData(phoneNumber = phoneNum)
                        if not validPhoneNum:
                            raise ValueError(f"Invalid phone number ☹️ : {errorMsg}")
                        else:
                            customer['phone number'] = phoneNum
                    elif updatePersonalInformationSelection == 6:
                        rFunctions.clearPreviousLine()
                        email = input("Enter new email address: ")
                        errorMsg, validEmail = rFunctions.validData(email = email)
                        if not validEmail:
                            raise ValueError(f"Invalid phone number ☹️ : {errorMsg}")
                        else:
                            customer['email'] = email
                    elif updatePersonalInformationSelection == 7:
                        rFunctions.clearPreviousLine()
                        customer['address'] = input("Enter new address: ")
                    else:
                        raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                    if usernameChanges == True:
                        rFunctions.writeFile("customer", customersDict)
                        rFunctions.readFile("customer")
                        print(f"{rFunctions.color('green', 'foreground')}Personal information updated successfully! 😄{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        return newUsername
                    else:
                        rFunctions.writeFile("customer", customersDict)
                        rFunctions.readFile("customer")
                        print(f"{rFunctions.color('green', 'foreground')}Personal information updated successfully! 😄{rFunctions.color('reset', None)}")
                        time.sleep(2)
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()

# (ii) Change Password
def accountChangePasswordPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Update Password".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print(f"Username: {username}")  
        try:
            oldPassword = str(input("Old Password: "))
            newPassword = str(input("New Password: "))
            customersDict = rFunctions.readFile("customer")
            checkUsername, checkPassword = rFunctions.checkLogin("customer", username, oldPassword, customersDict)
            try:
                if checkUsername and checkPassword:
                    if str(oldPassword) == str(newPassword):
                        raise ValueError(f"{rFunctions.color('red', 'foreground')}Your new password cannot be the same as the old password ☹️ Please try again...{rFunctions.color('reset', None)}")
                    else:
                        errorMsg, validPassword = rFunctions.validData(password = newPassword)
                        if not validPassword:
                            raise ValueError(f"{errorMsg} ☹️")
                        else:
                            for customer in customersDict["customers"]:
                                if customer['username'] == username:
                                    customer['password'] = newPassword
                                    rFunctions.writeFile("customer", customersDict)
                                    print(f"{rFunctions.color('green', 'foreground')}Your password has been updated! 😄{rFunctions.color('reset', None)}")
                                    time.sleep(1)
                else:
                    raise ValueError(f"{rFunctions.color('red', 'foreground')}Your password is wrong ☹️ Please try again...{rFunctions.color('reset', None)}")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                if not rFunctions.askContinue():
                    break
                rFunctions.clearPreviousLine()
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# Functionality 02: Product Browsing
def productBrowsingPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Product Browsing".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print("1. 🔎 Search for Product")
        print("2. 🔽 Filter")
        print("3. 🔙 Back")
        print("-"*40)
        try:
            productBrowsing = input("Enter selection: ").lower()
            if productBrowsing.isdigit(): #if functionality consist of all digits
                productBrowsing = int(productBrowsing)
            if productBrowsing in [1, "search for product", "1. search for product"]:
                browsingSearchForProductPage(username)
            elif productBrowsing in [2, "filter", "2. filter"]:
                browsingFilterPage(username)
            elif productBrowsing in [3, "back", "3. back"] :
                break
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (i) Search for Product
def browsingSearchForProductPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Search for Product".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        results = []
        try:
            browsingSearch = input("Enter product flavour / name: ").strip().lower()
            if isinstance(browsingSearch, str):
                productsDict = rFunctions.readFile("product")
                if productsDict and 'products' in productsDict:
                    for product in productsDict['products']:
                        if browsingSearch in product['name'].lower() or browsingSearch in product['flavour'].lower():
                            results.append(product)
                if results:
                    print("\nSearch Results: ")
                    for i, product in enumerate(results, 1):
                        print(f"{i}. {product['name']}")
                    print()
                    if not rFunctions.askContinue():
                        break
                    rFunctions.clearPreviousLine()
                    try:
                        productSearchSelection = input("Enter the number of the product you want to view details for: ")
                        if productSearchSelection.isdigit(): #if functionality consist of all digits
                            productSearchSelection = int(productSearchSelection)
                        if isinstance(productSearchSelection, int):
                            if 1 <= productSearchSelection <= len(results):
                                displayProductDetails(username, results[productSearchSelection-1])
                                break
                            else:
                                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                        else:
                            raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                else:
                    print(f"{rFunctions.color('red', 'foreground')}No products found matching your search criteria.{rFunctions.color('reset', None)}")
                    time.sleep(1)
                    if not rFunctions.askContinue():
                        break
                    rFunctions.clearPreviousLine()
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (ii) Filter
def browsingFilterPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Filter".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        productsDict = rFunctions.readFile("product")
        products = productsDict['products']
        uniqueCategories = []
        for product in products:
            category = product['category']
            if category not in uniqueCategories:
                uniqueCategories.append(category)
        for i, category in enumerate(uniqueCategories, 1):
            print(f"{i}. {category}")
        print(f"{len(uniqueCategories) + 1}. 🔝 Top 3 Products")
        print(f"{len(uniqueCategories) + 2}. 🔙 Back")
        try:
            browsingFilter = input("\nEnter the number of category: ")
            if browsingFilter.isdigit(): #if functionality consist of all digits
                browsingFilter = int(browsingFilter)
            if isinstance(browsingFilter, int):
                if 1 <= browsingFilter <= len(uniqueCategories):
                    productCategory(uniqueCategories[browsingFilter - 1], username)
                    break
                elif browsingFilter == len(uniqueCategories) + 1:
                    top3Products(username)
                elif browsingFilter == len(uniqueCategories) + 2:
                    break
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (ii)(i) Product Category Function
def productCategory(category:str, username):
    while True:
        os.system('cls') #clear terminal
        productsDict = rFunctions.readFile("product")
        productsCategory = [product for product in productsDict['products'] if product['category'].lower() == category.lower()]
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Category: {category}".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        if productsCategory:
            for i, product in enumerate(productsCategory, 1):
                print(f"{i}. {product['name']}")
        print()
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        try:
            categorySelection = input("Enter the number of product to view details: ")
            if categorySelection.isdigit(): #if functionality consist of all digits
                categorySelection = int(categorySelection)
            if isinstance(categorySelection, int):
                if 1 <= categorySelection <= len(productsCategory):
                    displayProductDetails(username, productsCategory[categorySelection - 1])
                    break
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (ii)(ii) Top 3 Products
def top3Products(username):
    while True:
        os.system('cls') #clear terminal
        print("Top 3 Products in Year and Month".center(40, "-"))
        topProducts = sFunctions.productPopularityTop3()
        print()
        productsDict = rFunctions.readFile("product")
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        try:
            topProductSelection = input("Enter the number of product to view details: ")
            if topProductSelection.isdigit(): #if functionality consist of all digits
                topProductSelection = int(topProductSelection)
            if isinstance(topProductSelection, int):
                if 1 <= topProductSelection <= len(topProducts):
                    for product in productsDict['products']:
                        if product['name'] == topProducts[topProductSelection - 1][0]:
                            displayProductDetails(username, product)
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (iii) Display Product Details
def displayProductDetails(username, product: dict):
    while True:
        os.system('cls') #clear terminal
        print("\033c" + f"{product['name']}".center(40, "-"))
        sFunctions.productDetails(product)
        print("\nOptions:")
        print("1. 🛒 Add to cart?")
        print("2. 🔙 Back")
        try:
            displayProductSelection = input("\nEnter selection: ").lower()
            if displayProductSelection.isdigit(): #if functionality consist of all digits
                displayProductSelection = int(displayProductSelection)
            if displayProductSelection in [1, "add to cart", "1. add to cart"]:
                cartManagementPage(username, product = product, action = "add")
                break
            elif displayProductSelection in [2, "back", "2. back"]:
                break
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (iii)(i) Add Product To Cart
def addToCart(cart:dict, product:dict):
    while True:
        os.system('cls') #clear terminal
        productsDict = rFunctions.readFile("product")
        for productSelected in productsDict['products']:
            if productSelected['name'] == product['name']:
                productName = productSelected['name']
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Add {productName} to Cart".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        try:
            quantity = input(f"Enter the quantity for {productName}: ")
            if quantity.isdigit():
                quantity = int(quantity)
            if isinstance(quantity, int):
                cartsDict = rFunctions.readFile("cart")
                for userCart in cartsDict['carts']:
                    if userCart['cartID'] == cart['cartID']:
                        productsInCart = eval(userCart['products'])
                        selectedProduct = None
                        for item in productsInCart:  # Check if the product already exists in the cart
                            if item[0] == product['id']:
                                selectedProduct = item
                                break
                        if selectedProduct:
                            selectedProduct[2] = str(int(selectedProduct[2]) + int(quantity)) # Update the quantity if the product exists
                        else:
                            newProduct = [product['id'], product['name'], quantity]
                            productsInCart.append(newProduct)
                        userCart['products'] = str(productsInCart)
                rFunctions.writeFile("cart", cartsDict)
                print(f"{rFunctions.color('green', 'foreground')}{productName} added to '{cart['cartName']}' successfully! 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                print()
                if not rFunctions.askContinue():
                    return False
                else:
                    return True
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# Functionality 03: Cart Management
def cartManagementPage(username, product=None, action="manage"):
    while True:
        os.system('cls') #clear terminal
        productsDict = rFunctions.readFile("product")
        if action == "add":
            for productSelected in productsDict['products']:
                if productSelected['name'] == product['name']:
                    productName = productSelected['name']
            print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Select Cart to Add {productName}".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        else:
            print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Cart Management".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        userCarts = []
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        cartsDict = rFunctions.readFile("cart")
        for cart in cartsDict['carts']:
            if cart['userID'] == userID:
                userCarts.append(cart)
        if userCarts:
            for i, cart in enumerate(userCarts, 1):
                print(f"{i}. {cart['cartName']}")
            print(f"{len(userCarts) + 1}. Create a new cart?")
            print(f"{len(userCarts) + 2}. 🔙 Back")
        else:
            print(f"{1}. Create a new cart?")
            print(f"{2}. 🔙 Back")
        try:
            cartSelection = input("Enter the number of your selection: ")
            if cartSelection.isdigit(): #if functionality consist of all digits
                cartSelection = int(cartSelection)
            if isinstance(cartSelection, int):
                if 1 <= cartSelection <= len(userCarts):
                    selectedCart = userCarts[cartSelection - 1]
                    selectedCartName = selectedCart['cartName']
                    selectedCartID = selectedCart['cartID']
                    if action == "add":
                        repeat = addToCart(selectedCart, product)
                        if not repeat:
                            break
                    else:
                        displayCartDetails(selectedCartID, selectedCartName, username)
                elif cartSelection == len(userCarts) + 1:
                    newCart(username, product=product, action=action)
                elif cartSelection == len(userCarts) + 2:
                    break
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (i) Display Cart Details
def displayCartDetails(selectedCartID, selectedCartName, username):
    while True:
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        cartsDict = rFunctions.readFile("cart")
        for cart in cartsDict['carts']:
            if cart['userID'] == userID and cart['cartID'] == selectedCartID and cart['cartName'] == selectedCartName:
                selectedCart = cart
                break    
        os.system('cls') #clear terminal
        print("\033c" + f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Cart {selectedCartName}".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print(f"\nCart ID: {selectedCart['cartID']}")
        cartDate = datetime.strptime(selectedCart["creationDateTime"], "%Y-%m-%d %H:%M:%S").date()
        cartTime = datetime.strptime(selectedCart["creationDateTime"], "%Y-%m-%d %H:%M:%S").time()
        print(f"\nCreated Date: {cartDate}")
        print(f"\nCreated Time: {cartTime}")
        products = eval(selectedCart['products'])
        if not products:
            print()
            print(f"{rFunctions.color('red', 'foreground')}No items in the cart.{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
        else:
            print("\n" + rFunctions.tabulateGivenData(["Product ID", "Product Name", "Quantity"], products, tbfmt = "outline"))
            print("\nOptions:" + "\n" + "1. Select the product to modify (Change quantity or remove)")
            print("2. Proceed to checkout")
            print("3. 🔙 Back" + "\n")
            try:
                cartManagementOption = input("Enter the number of option you wish to proceed: ")
                if cartManagementOption.isdigit(): #if functionality consist of all digits
                    cartManagementOption = int(cartManagementOption)
                if cartManagementOption == 1:
                    rFunctions.clearPreviousLine()
                    modifyProductInCart(selectedCartID, selectedCartName, username)
                elif cartManagementOption == 2: #Checkout for cart
                    rFunctions.clearPreviousLine()
                    while True:
                        try:
                            confirmation = input("Proceed to checkout? (Enter 'Y' for Yes or 'N' for No): ").upper()
                            if confirmation == "Y":
                                rFunctions.clearPreviousLine()
                                print(f"{rFunctions.color('green', 'foreground')}Proceeding to checkout...{rFunctions.color('reset', None)}")
                                time.sleep(1)
                                generateOrder(selectedCartID, selectedCartName, username)
                            elif confirmation == "N":
                                print(f"{rFunctions.color('red', 'foreground')}Checkout failed ☹️{rFunctions.color('reset', None)}")
                                break
                            else:
                                raise ValueError("Invalid input ☹️ : Enter either 'Y' or 'N'")
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                        break
                elif cartManagementOption == 3:
                    break
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()

# (i)(i) Modify Product in Cart
def modifyProductInCart(selectedCartID, selectedCartName, username):
    while True:
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        cartsDict = rFunctions.readFile("cart")
        for cart in cartsDict['carts']:
            if cart['userID'] == userID and cart['cartID'] == selectedCartID and cart['cartName'] == selectedCartName:
                selectedCart = cart
                break
        selectedProduct = None
        products = eval(selectedCart['products'])
        try:
            productIDSelection = input("Enter the product ID you wish to modify/remove: ")
            if isinstance(productIDSelection, str):
                productIDSelection = str(productIDSelection).upper()
                for product in products:
                    if product[0] == productIDSelection:
                        selectedProduct = product
                        break
            if selectedProduct:
                rFunctions.clearPreviousLine()
                modifyProduct = input("Enter 'M' to modify quantity or 'R' to remove the product from cart: ").upper()
                if modifyProduct == "M":
                    for cart in cartsDict['carts']:
                        if cart["cartID"] == selectedCartID:
                            rFunctions.clearPreviousLine()
                            newQuantity = input("Enter the new quantity of the product: ")
                            if newQuantity.isdigit(): #if functionality consist of all digits
                                newQuantity = int(newQuantity)
                            else:
                                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                            rFunctions.clearPreviousLine()
                            selectedProduct[2] = newQuantity #Update quantity in the product list
                            selectedCart['products'] = str(products) #Convert list to string for storage
                            rFunctions.writeFile("cart", cartsDict)
                            print(f"{rFunctions.color('green', 'foreground')}Quantity updated successfully! 😄{rFunctions.color('reset', None)}")
                            time.sleep(1.5)
                            break
                    break
                elif modifyProduct == "R":
                    rFunctions.clearPreviousLine()
                    products.remove(selectedProduct)
                    selectedCart['products'] = str(products)
                    rFunctions.writeFile("cart", cartsDict)
                    print(f"{rFunctions.color('green', 'foreground')}Product removed successfully! 😄{rFunctions.color('reset', None)}")
                    time.sleep(1)
                    break
                else:
                    raise ValueError("Invalid input ☹️ : Enter either 'M' or 'R'")
            else:
                raise ValueError(f"Invalid Input ☹️ : {productIDSelection} does not exists")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()

# (ii) Create New Cart
def newCart(username, product=None, action="manage"):
    while True:
        cartsDict = rFunctions.readFile("cart")
        customersDict = rFunctions.readFile("customer")
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Create New Cart".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        cartName = input("Enter the name of your new cart: ")
        cartID = rFunctions.assignId("cart", cartsDict)
        createDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        newCart = {
            "cartID": cartID,
            "userID": userID,
            "cartName": cartName,
            "creationDateTime": createDateTime,
            "products": "[]"
        }
        cartsDict = rFunctions.readFile("cart")
        # Add the new cart to the carts list in cartsDict
        if 'carts' not in cartsDict:
            cartsDict['carts'] = []
        cartsDict['carts'].append(newCart)
        rFunctions.writeFile("cart", cartsDict)
        print(f"{rFunctions.color('green', 'foreground')}New cart '{cartName}' with ID '{cartID}' created successfully!{rFunctions.color('reset', None)}")
        time.sleep(2)
        break

# (iii) Generate Order According to the Cart
def generateOrder(selectedCartID, selectedCartName, username):
    while True:
        os.system('cls') #clear terminal
        ordersDict = rFunctions.readFile("order")
        productsDict = rFunctions.readFile("product")
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Order".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        orderID = rFunctions.assignId("order", ordersDict)
        orderCreatedDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Cart ID: {selectedCartID}" + "\n\n" + f"Order ID: {orderID}" + "\n\n" + f"Order created datetime: {orderCreatedDateTime}")
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        cartsDict = rFunctions.readFile("cart")
        for cart in cartsDict['carts']:
            if cart['userID'] == userID and cart['cartID'] == selectedCartID and cart['cartName'] == selectedCartName:
                selectedCart = cart
                break
        print("\nProducts: ")
        products = eval(selectedCart['products'])
        totalQuantity = 0
        totalPrice = 0.00
        newOrderForProducts = []
        for i, product in enumerate(products, 1):
            productID = product[0]
            productName = product[1]
            quantity = int(product[2])
            # Get product's unit price in productsDict
            for p in productsDict['products']:
                if p['id'] == productID:
                    unitPrice = float(p['price'].replace('RM', '').strip()) # Remove RM from bakerProducts.csv
                    totalProductPrice = quantity * unitPrice
                    totalPrice += totalProductPrice
                    totalQuantity += quantity
                    break
            newOrderForProducts.append(f'["{productID}"-"{productName}"-{quantity}-{unitPrice}-{totalProductPrice}]')
            print(f"{i}. {productName} * {quantity} * RM {unitPrice:.2f}")
        print(f"\nTotal number of products: {totalQuantity}")
        print(f"\nTotal price: RM {totalPrice:.2f}")
        print("\nPayment Method: " + "\n" + "1. COD" + "\n" + "2. TNG" + "\n" + "3. Online Banking")
        try:
            paymentMethodSelection = input("\nEnter your selection for payment method: ").lower()
            payment = False
            if paymentMethodSelection.isdigit(): #if functionality consist of all digits
                paymentMethodSelection = int(paymentMethodSelection)
            if paymentMethodSelection in [1, "cod", "1. cod"]:
                paymentMethod = "COD"
                payment = True
            elif paymentMethodSelection in [2, "tng", "2. tng"]:
                paymentMethod = "TNG"
                payment = True
            elif paymentMethodSelection in [3, "online banking", "3. online banking"]:
                paymentMethod = "Online Banking"
                payment = True
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
        if payment:
            print(f"{rFunctions.color('green', 'foreground')}Payment method selected successfully! 😄{rFunctions.color('reset', None)}")
            time.sleep(1.5)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            print(f"Payment Method: {paymentMethod}")
            print("\nLogistics Services: " + "\n" + "1. Pickup" + "\n" + "2. Delivery")
            try:
                logisticsServicesSelection = input("\nEnter your selection for logistics services: ").lower()
                logistics = False
                if logisticsServicesSelection.isdigit(): #if functionality consist of all digits
                    logisticsServicesSelection = int(logisticsServicesSelection)
                if logisticsServicesSelection in [1, "pickup", "1. pickup"]:
                    logisticsServices = "Pickup"
                    logistics = True
                elif logisticsServicesSelection in [2, "delivery", "2. delivery"]:
                    logisticsServices = "Delivery"
                    logistics = True
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
            if logistics:
                print(f"{rFunctions.color('green', 'foreground')}Logistics service selected successfully! 😄{rFunctions.color('reset', None)}")
                time.sleep(1.5)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                print(f"Logistics Services: {logisticsServices}")
                try:
                    confirmation = input("\nConfirm order (Y/N): ").upper()
                    if confirmation == "Y":
                        productsStr = "[" + ", ".join(newOrderForProducts) + "]"
                        newOrder = {
                        "orderID": orderID,
                        "cartID": selectedCartID,
                        "userID": selectedCart['userID'],
                        "orderCreatedDateTime": orderCreatedDateTime,
                        "products": productsStr,
                        "paymentMethod": paymentMethod,
                        "logisticsService": logisticsServices,
                        "completionStatus": "Pending"
                        }
                        ordersDict['orders'].append(newOrder)
                        rFunctions.writeFile("order", ordersDict)
                        cartsDict['carts'].remove(selectedCart)
                        rFunctions.writeFile("cart", cartsDict)
                        print()
                        print(f"{rFunctions.color('green', 'foreground')}Order placed successfully! 😄{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        orderTrackingPage(username)
                    elif confirmation == "N":
                        print()
                        print(f"{rFunctions.color('red', 'foreground')}Order not confirmed.{rFunctions.color('reset', None)}")
                        time.sleep(1)
                        break
                    else:
                        raise ValueError("Invalid input ☹️ : Enter either 'Y' or 'N'")
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()

# Functionality 04: Order Tracking
def orderTrackingPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "List of Orders".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        ordersDict = rFunctions.readFile("order")
        ordersTrack = [order for order in ordersDict['orders'] if order['userID'] == userID and order['completionStatus'] not in ['completed']]
        if ordersTrack:
            for i, order in enumerate(ordersTrack, 1):
                print(f"{i}. {order['orderID']}")
            print(f"{len(ordersTrack) + 1}. 🔙 Back")
            try:
                orderTrackSelection = input("Enter the number of the order to track: ")
                if orderTrackSelection.isdigit(): #if functionality consist of all digits
                    orderTrackSelection = int(orderTrackSelection)
                if isinstance(orderTrackSelection, int):
                    if 1 <= orderTrackSelection <= len(ordersTrack):
                        selectedOrder = ordersTrack[orderTrackSelection - 1]
                        orderTrackDetails(username, selectedOrder)
                    elif orderTrackSelection == len(ordersTrack) + 1:
                        break
                    else:
                        raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
        elif not ordersTrack:
            print(f"{rFunctions.color('red', 'foreground')}No order can be tracked.{rFunctions.color('reset', None)}")
            time.sleep(2)
            break

# (i) Order Tracking Details
def orderTrackDetails(username, orderTrack):
    while True:
        os.system('cls') #clear terminal
        productsDict = rFunctions.readFile("product")
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Order Tracking for {orderTrack['orderID']}".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print(f"\nUsername: {username}")
        orderDate = datetime.strptime(orderTrack["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date()
        orderTime = datetime.strptime(orderTrack["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").time()
        print(f"\nOrder Date: {orderDate}")
        print(f"\nOrder Time: {orderTime}")
        productList = []
        productList = eval(orderTrack["products"])
        print("\n" + rFunctions.tabulateGivenData(["Product ID", "Product Name", "Quantity", "Unit Price", "Total Price"], productList, tbfmt = "outline"))
        promotions = []
        for product in productList:
            for bakerProduct in productsDict["products"]:
                if bakerProduct["id"] == product[0]:
                    if bakerProduct["promotion"] != "":
                        promotions.append([product[0], bakerProduct["promotion"]])
        for promotion in promotions:
            print(rFunctions.color('cyan', 'foreground') + f"{promotion[1]} {promotion[0]}" + rFunctions.color('reset', None))
        print(f"\nPayment Method: {orderTrack['paymentMethod']}")
        print(f"\nLogistics Services: {orderTrack['logisticsServices']}")
        print("\nOrder Status:", f"{orderTrack['completionStatus']}")
        print()
        orderDetails = input("Enter 0 to <EXIT>: ")
        try:
            if orderDetails.isdigit(): #if functionality consist of all digits
                orderDetails = int(orderDetails)
            if orderDetails == 0:
                break
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# Functionality 05: Product Review
def productReviewPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Product Review".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print("1. Completed Reviews")
        print("2. Incomplete Reviews")
        print("3. 🔙 Back")
        try:
            reviewSelection = input("Enter selection: ").lower()
            if reviewSelection.isdigit(): #if functionality consist of all digits
                reviewSelection = int(reviewSelection)
            if reviewSelection in [1, "completed reviews", "1. completed reviews"]:
                productReviewCompletedPage(username)
            elif reviewSelection in [2, "incomplete reviews", "2. incomplete reviews"]:
                productReviewIncompletePage(username)
            elif reviewSelection in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (i) Completed Review of Order
def productReviewCompletedPage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Completed Product Review".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        reviewsDict = rFunctions.readFile("review")
        orderIDs = []
        for review in reviewsDict['reviews']:
            if review['userID'] == userID:
                orderID = review['orderID']
                orderIDs.append(orderID)
        if orderIDs:
            for i, orderID  in enumerate(orderIDs, 1):
                print(f"{i}. {orderID}")
            print(f"{len(orderIDs) + 1}. 🔙 Back")
            try:
                orderSelection = input("Enter the number of the order to review: ")
                if orderSelection.isdigit(): #if functionality consist of all digits
                    orderSelection = int(orderSelection)
                if isinstance(orderSelection, int):
                    if 1 <= orderSelection <= len(orderIDs):
                        selectedOrderID = orderIDs[orderSelection - 1]
                        completedProductsInOrder(username, selectedOrderID)
                    elif orderSelection == len(orderIDs) + 1:
                        break
                    else:
                        raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
        elif not orderIDs:
            print(f"{rFunctions.color('red', 'foreground')}No completed reviews are done.{rFunctions.color('reset', None)}")
            time.sleep(2)
            break

# (i)(i) Completed Review of Products in Particular Order
def completedProductsInOrder(username, selectedOrderID):
    while True:
        os.system('cls') #clear terminal
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        reviewsDict = rFunctions.readFile("review") 
        orderReviews = [review for review in reviewsDict['reviews'] if review['userID'] == userID and review['orderID'] == selectedOrderID]
        print(f"{rFunctions.color('bold', None)}" + "-"*40)
        print(f"Order ID: {selectedOrderID}".center(40))
        print("-"*40 + f"{rFunctions.color('reset', None)}")
        if orderReviews:
            order = orderReviews[0] # Since orderReviews is a list, get the first item
            products = eval(order['products'])
            for i, product in enumerate(products, 1):
                productID, productName, rating, feedback = product
                print(f"{i}. {productID}, {productName}")
            print(f"{len(products) + 1}. 🔙 Back")
        try:
            productSelection = input("Select a product to view the review: ")
            if productSelection.isdigit(): #if functionality consist of all digits
                productSelection = int(productSelection)
            if isinstance(productSelection, int):
                if 1 <= productSelection <= len(products):
                    selectedProduct = products[productSelection - 1]
                    productReview(selectedProduct)
                elif productSelection == len(products) + 1:
                    break
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

# (i)(ii) Details of Completed Review of Product
def productReview(selectedProduct:list):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Product Review: {selectedProduct[1]}".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print(f"Item: {selectedProduct[1]}")
        print(f"Rating: {'⭐'*selectedProduct[2]}")
        print(f"Feedback: {selectedProduct[3]}")
        print()
        try:
            reviewBack = input("Enter 0 to <EXIT>: ")
            if reviewBack.isdigit(): #if functionality consist of all digits
                reviewBack = int(reviewBack)
            if reviewBack == 0:
                break
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (ii) Incompleted Review of Order
def productReviewIncompletePage(username):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Incomplete Reviews".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        reviewsDict = rFunctions.readFile("review")
        ordersDict = rFunctions.readFile("order")
        incompleteOrders = []
        reviewedOrderIDs = [review['orderID'] for review in reviewsDict['reviews'] if review['userID'] == userID]
        for order in ordersDict['orders']:
            if order['userID'] == userID and order['orderID'] not in reviewedOrderIDs and order['completionStatus'] == 'completed':
                incompleteOrders.append(order['orderID'])
            elif order['userID'] == userID and order['orderID'] in reviewedOrderIDs and order['completionStatus'] == 'completed':
                numberOfProduct = len(eval(order['products']))
                for review in reviewsDict['reviews']:
                    if review['orderID'] == order['orderID']:
                        numberOfReview = len(eval(review['products']))
                        if numberOfReview < numberOfProduct:
                            incompleteOrders.append(order['orderID'])
        try:
            if incompleteOrders:
                for i, orderID in enumerate(incompleteOrders, 1):
                    print(f"{i}. {orderID}")
                print(f"{len(incompleteOrders) + 1}. 🔙 Back")
                try:
                    orderSelection = input("Enter the number of the order to review: ")
                    if orderSelection.isdigit(): #if functionality consist of all digits
                        orderSelection = int(orderSelection)
                    if isinstance(orderSelection, int):
                        if 1 <= orderSelection <= len(incompleteOrders):
                            selectedOrderID = incompleteOrders[orderSelection - 1]
                            incompleteProductsInOrder(username, selectedOrderID)
                        elif orderSelection == len(incompleteOrders) + 1:
                            break
                        else:
                            raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                    else:
                        raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
            else:
                print(f"{rFunctions.color('red', 'foreground')}No incomplete reviews available.{rFunctions.color('reset', None)}")
                time.sleep(2)
                break
        except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()

# (ii)(i) Incomplete Review of Products in Particular Order
def incompleteProductsInOrder(username, orderID):
    while True:
        os.system('cls') #clear terminal
        print(f"{rFunctions.color('bold', None)}" + "-"*50 + "\n" + f"Incomplete Reviews for Products in Order {orderID}".center(50) + "\n" + "-"*50 + f"{rFunctions.color('reset', None)}")
        reviewsDict = rFunctions.readFile("review") 
        ordersDict = rFunctions.readFile("order")
        selectedOrder = [order for order in ordersDict['orders'] if order['orderID'] == orderID]
        try:
            if selectedOrder:
                products = eval(selectedOrder[0]['products'])  # Extract the products from the selected orders
                for i, product in enumerate(products, 1):
                    foundReview = False
                    for review in reviewsDict["reviews"]:
                        if review["orderID"] == orderID:
                            foundReview = True
                            reviewedProducts = eval(review["products"])
                            notReviewed = True
                            for reviewed in reviewedProducts:
                                if reviewed[0] == product[0]:
                                    notReviewed = False
                            if notReviewed:
                                productID, productName, _, _, _ = product
                                print(f"{productID}, {productName}")
                    if not foundReview:
                        productID, productName, _, _, _ = product
                        print(f"{productID} {productName}")
                if not rFunctions.askContinue():
                    break
                rFunctions.clearPreviousLine()
                try:
                    selectedProduct = None
                    incompleteProductSelection = str(input("Select a product code to review: ")).upper()
                    for product in products:
                        if product[0] == incompleteProductSelection:
                            selectedProduct = product
                            break
                    if selectedProduct:
                        incompleteProductReview(username, selectedProduct, selectedOrder[0])
                    else:
                        raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()

# (ii)(ii) Enter Review for the Incomplete Product in Order
def incompleteProductReview(username, selectedProduct:list, selectedOrder:dict):
    while True:
        os.system('cls') #clear terminal
        reviewsDict = rFunctions.readFile("review") 
        ordersDict = rFunctions.readFile("order")
        customersDict = rFunctions.readFile("customer")
        for customer in customersDict['customers']:
            if customer['username'] == username:
                userID = customer['id']
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Review for Product {selectedProduct[1]}".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print(f"Product ID: {selectedProduct[0]}")
        print(f"Product Name: {selectedProduct[1]}")
        try:
            rating = input("Enter your rating for the product (1-5): ")
            if rating.isdigit(): #if functionality consist of all digits
                rating = int(rating)
            if isinstance(rating, int):
                if rating >= 1 and rating <= 5:
                    print(f"{rFunctions.color('green', 'foreground')}Your rating for the product is recorded! 😄{rFunctions.color('reset', None)}")
                    time.sleep(1.5)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
                    print(f"Rating: {"⭐"*rating}")
                else:
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            else:
                raise ValueError("Invalid input ☹️ : Please enter a number between 1 to 5")
            feedback = str(input("Enter your feedback for the product: "))
            if isinstance(feedback, str):
                if not feedback.strip():
                    raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
                else:
                    print(f"{rFunctions.color('green', 'foreground')}Your feedback for the product is recorded! 😄{rFunctions.color('reset', None)}")
                    time.sleep(1.5)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
                    print(f"Feedback: {feedback}")
            else:
                raise ValueError("Invalid Input ☹️") #invalid input, trigger exception handling
            newReview = [selectedProduct[0], selectedProduct[1], rating, feedback]
            reviewFound = False
            # Search for existing reviews
            for review in reviewsDict['reviews']:
                if review['orderID'] == selectedOrder['orderID']:
                    reviewFound = True
                    products = eval(review['products'])
                    #updatedProducts = [newReview if product[0] == selectedProduct[0] else product for product in products]
                    products.append(newReview)
                    review['products'] = str(products)
                    break
            # If no existing review found, add a new entry
            if not reviewFound:
                newReviewEntry = {
                    'orderID': selectedOrder['orderID'],
                    'userID': userID,
                    'products': str([newReview])
                }
                reviewsDict['reviews'].append(newReviewEntry)
            rFunctions.writeFile("review", reviewsDict)
            reviewsDict = rFunctions.readFile("review") 
            print(f"{rFunctions.color('green', 'foreground')}Review submitted successfully! 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()