import os, time, custom_modules.reusableFunctions as rFunctions, sharedFunctions as sFunctions
#AttributeError if just import datetime.
#the strptime function is part of the datetime class within the datetime module,
#so you should import it like this:
from datetime import datetime

# #(B)(ii) Cashier Page
# #01 Home Page - Functionality
def cashierPage(username):
    while True:
        os.system('cls')
        print("="*40 + "\n" + " "*12 + "Cahier Main Page" + "\n" + "="*40)
        print(f"Welcome {username},")
        print("1. 📖 Product Display")
        print("2. 💰 Manage Discount")
        print("3. 🧾 Transaction Completion")
        print("4. 📋 Reporting")
        print("5. 🔚 Log Out")
        cashierMain = input("Enter selection: ").lower()
        try:
            if cashierMain.isdigit():
                cashierMain = int(cashierMain)
            if cashierMain in [1, "product display", "1. product display"]:
                productDisplayPage()
            elif cashierMain in [2, "manage discount", "2. manage discount"]:
                manageDiscountPage()
            elif cashierMain in [3, "transaction completion", "3. transaction completion"]:
                transactionCompletionPage()
            elif cashierMain in [4, "reporting", "4. reporting"]:
                reportingPage()
            elif cashierMain in [5, "log out", "5. log out"]:
                rFunctions.clearPreviousLine()
                while True:
                    try:
                        confirm = input("Enter <YES> to confirm log out or <NO> to cancel:").lower()
                        if confirm == "yes":
                            logOut = True
                            break
                        elif confirm == "no":
                            logOut = False
                            break
                        else:
                            raise ValueError("Invalid Input ☹️")
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                        rFunctions.clearPreviousLine()
                if logOut:
                    break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


##(B)(ii)(i) Product Display Page
def productDisplayPage():
    while True:
        productsDict = rFunctions.readFile("product")
        print("\033c" + "Product Display Page".center(66, "-") + "\n")
        print(rFunctions.tabulateCsvData("product", ["id", "name"], tbfmt = "outline"))
        try:
            prodid = input("\nEnter the ProductID to view: ").upper()
            #check the id format is correct or not
            if not rFunctions.checkUniqueData("product", "id", prodid, productsDict):
                raise ValueError(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {prodid} does not exists{rFunctions.color('reset', None)}")
            for product in productsDict["products"]:
                if product["id"] == prodid:
                    print("\033c" + "Product Details".center(40, "-"))
                    sFunctions.productDetails(product)
                    time.sleep(1)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()


#(B)(ii)(ii) Manage Discount Page
#01 Start of Manage Discount Page
def manageDiscountPage():
    while True:
        os.system('cls')
        print("-" * 40 + "\n" + " " * 12 + "Discount Management" + "\n" + "-" * 40)
        print("1. ➕ Add Discount")
        print("2. 🗑️  Delete Discount")
        print("3. ✏️  Modify Discount")
        print("4. 🔙 Back")
        discountMan = input("Enter selection: ").lower()
        try:
            if discountMan.isdigit():
                discountMan = int(discountMan)
            if discountMan in [1, "add discount", "1. add discount"]:
                addDiscountPage()
            elif discountMan in [2, "delete discount", "2. delete discount"]:
                deleteDiscountPage()
            elif discountMan in [3, "modify discount", "3. modify discount"]:
                modifyDiscountPage()
            elif discountMan in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


#02 Adding Discount Function
def addDiscountPage():
    while True:
        productsDict = rFunctions.readFile("product")
        os.system('cls')
        print("Add Promotion Page".center(66, "-"),"\n")
        print(rFunctions.tabulateCsvData("product", ["id", "name", "promotion"], tbfmt = "outline"))
        print()
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        try:
            prodcode = input("Enter the ProductID to add promotion: ").upper()
            if not rFunctions.checkUniqueData("product", "id", prodcode, productsDict): #check the id format is correct or not
                raise ValueError(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {prodcode} does not exists{rFunctions.color('reset', None)}")
            promo = False
            for product in productsDict["products"]:
                if product["id"] == prodcode and product["promotion"] == "":
                    promo = True
                    rFunctions.clearPreviousLine()
                    product["promotion"] = input("Enter new promotion: ")
            if promo:
                rFunctions.writeFile("product", productsDict)
                productsDict = rFunctions.readFile("product") #Update global(the dictionary)
                time.sleep(1)
                print(f"{rFunctions.color('green', 'foreground')}The promotion for {prodcode} is added successfully 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            else:
                raise ValueError(f"{prodcode} already had promotion ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()


#03 Deleting Discount Function
def deleteDiscountPage():
    while True:
        productsDict = rFunctions.readFile("product")
        os.system('cls')
        print("Delete Promotion Page".center(66, "-"), "\n")
        print(rFunctions.tabulateCsvData("product", ["id", "name", "promotion"], tbfmt = "outline"))
        print()
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        try:
            prodcode = input("Enter the ProductID to delete promotion: ").upper()
            if not rFunctions.checkUniqueData("product", "id", prodcode, productsDict):
                raise ValueError(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {prodcode} does not exists{rFunctions.color('reset', None)}")
            promo = False
            for product in productsDict["products"]:
                if product["id"] == prodcode and product["promotion"] != "":
                    promo = True
                    product["promotion"] = ""
                    break
            if promo:
                rFunctions.writeFile("product", productsDict)
                productsDict = rFunctions.readFile("product")
                time.sleep(1)
                print(f"{rFunctions.color('green', 'foreground')}The promotion for {prodcode} is deleted successfully 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            else:
                raise ValueError(f"{prodcode} does not has a promotion ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()


#04 Modifing Discount Function
def modifyDiscountPage():
    while True:
        productsDict = rFunctions.readFile("product")
        os.system('cls')
        print("Modify Promotion Page".center(66, "-"), "\n")
        print(rFunctions.tabulateCsvData("product", ["id", "name", "promotion"], tbfmt = "outline"))
        print()
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        try:
            prodcode = input("Enter the ProductID to modify promotion: ").upper()
            if not rFunctions.checkUniqueData("product", "id", prodcode, productsDict):
                raise ValueError(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {prodcode} does not exists{rFunctions.color('reset', None)}")
            promo = False
            for product in productsDict["products"]:
                if product["id"] == prodcode and product["promotion"] != "":
                    promo = True
                    rFunctions.clearPreviousLine()
                    product["promotion"] = input("Enter promotion that need to be modify: ") 
            if promo:
                rFunctions.writeFile("product", productsDict)
                productsDict = rFunctions.readFile("product")
                time.sleep(1)
                print(f"{rFunctions.color('green', 'foreground')}The promotion for {prodcode} is modified successfully 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            else:
                raise ValueError(f"{prodcode} does not has a promotion ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()


#(B)(ii)(iii) Transaction Completion Page
def transactionCompletionPage():
    while True:
        ordersDict = rFunctions.readFile("order")
        productsDict = rFunctions.readFile("product")
        os.system('cls')
        print("Generate Receipt Page".center(66, "-"), "\n")
        print("List of available to generate receipt for:")
        # Collect unique year-month combinations
        yearMonth = []
        for order in ordersDict["orders"]:
            orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date().month
            orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date().year
            orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
            yearMonth.append([orderYear, orderMonth]) if [orderYear, orderMonth] not in yearMonth else yearMonth
        print(rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
        while True:
            try:
                customersDict = rFunctions.readFile("customer")
                month, year = input("Enter month and year: ").split()
                month, year, valid = rFunctions.validMonthYear(month, year)
                if [year, month] in yearMonth and valid:
                    print("\033c" + "View Order Details".center(40, "-"))
                    print(f"{rFunctions.color('underline', None)}{month} {year}{rFunctions.color('reset', None)}")
                    orderList, orderIds = [], []
                    for order in ordersDict["orders"]:
                        orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date().month
                        orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date().year
                        orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
                        if orderMonth == month and orderYear == year:
                            date = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date()
                            for customer in customersDict["customers"]:
                                if customer["id"] == order["userID"]:
                                    customerUsername = customer["username"]
                            orderList.append([order["orderID"], order["userID"], customerUsername, date])
                            orderIds.append(order["orderID"])
                    print(rFunctions.tabulateGivenData(["Order ID", "Customer ID", "Customer Username", "Order Date"], orderList, tbfmt = "psql") + "\n")
                    break
                elif not valid:
                    rFunctions.clearPreviousLine()
                    continue
                elif [year, month] not in yearMonth:
                    raise ValueError(f"Invalid input ☹️ : No records for order in {month} {year}")
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        while True:
            try:
                rFunctions.readFile("order")
                rFunctions.readFile("product")
                orderid = input("Enter the OrderID to generate receipt: ").upper()
                if not rFunctions.checkUniqueData("order", "orderID", orderid, ordersDict):
                    raise ValueError(f"Invalid Input ☹️ : {orderid} does not exist")
                receipt = False
                for order in ordersDict["orders"]:
                    if order["orderID"] == orderid:
                        productList = []
                        receipt = True
                        os.system('cls')
                        print("\033c","Receipt".center(66, "-"))
                        print("OrderID:", order["orderID"])
                        print("UserID:", order["userID"])
                        print("Order Created Date & Time:", order["orderCreatedDateTime"])
                        print("Payment Method:", order["paymentMethod"])
                        productList = eval(order["products"])
                        for product in productList:
                            product[3] = f"RM {product[3]:.2f}"
                            product[4] = f"RM {product[4]:.2f}"
                        productTable = rFunctions.tabulateGivenData(["Food ID", "Name", "Quantity", "Price", "Total Price"], productList, tbfmt = "outline", align=("center", "left", "center", "center", "center"))
                        print(productTable)
                        promotions = []
                        for product in productList:
                            for bakerProduct in productsDict["products"]:
                                if bakerProduct["id"] == product[0]:
                                    if bakerProduct["promotion"] != "":
                                        promotions.append([product[0], bakerProduct["promotion"]])
                        for promotion in promotions:
                            print(rFunctions.color('cyan', 'foreground') + f"{promotion[1]} {promotion[0]}" + rFunctions.color('reset', None))


                tpayment = 0.00
                for product in productList:
                    tpayment += float(rFunctions.extractNumber(product[4]))
                print("\nTotal Payment: RM %.2f"%(tpayment))
                print()
                if not receipt:
                    print(f"{rFunctions.color('red', 'foreground')}OrderID not found.{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        if not rFunctions.askContinue():
            break


#(B)(ii)(iv) Reporting Page
#01 Start of Reporting Page
def reportingPage():
    while True:
        os.system('cls')
        print("-" * 40 + "\n" + "Report Page".center(40) + "\n" + "-" * 40)
        print("1. 📊 Sales Performance")
        print("2. 📈 Product Popularity")
        print("3. 🔙 Back")
        reportHome = input("Enter selection: ").lower()
        try:
            if reportHome.isdigit():
                reportHome = int(reportHome)
            if reportHome in [1, "sales performance", "1. sales performance"]:
                salesPerformancePage()
            elif reportHome in [2, "product popularity", "2. product popularity"]:
                productPopularityPage()
            elif reportHome in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


#02 Sales Performance Page
def salesPerformancePage():
    while True:
        # Read data from files
        ordersDict = rFunctions.readFile("order")
        productsDict = rFunctions.readFile("product")
        os.system('cls')
        print("Sales Performance".center(66, "-"))
        print("List of available sales performance for:")
        
        # Collect unique year-month combinations
        yearMonth = []
        for data in ordersDict["orders"]:
            if "orderCreatedDateTime" in data:
                dataMonthInt = datetime.strptime(data["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").month
                dataYearInt = datetime.strptime(data["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").year
                dataMonth, dataYear, valid = rFunctions.validMonthYear(dataMonthInt, dataYearInt)
                if [dataYear, dataMonth] not in yearMonth:
                    yearMonth.append([dataYear, dataMonth])
            else:
                print(f"Invalid date for: {data}")
        
        # Display available year and month data
        print(rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt="simple_grid"))
        
        # User input for selecting month and year
        while True:
            try:
                month, year = input("Enter month and year: ").split()
                rFunctions.clearPreviousLine()
                month, year, valid = rFunctions.validMonthYear(month, year)
                
                # Validate input and ensure the month-year is available
                if valid and [year, month] in yearMonth:
                    print("\033c")  # clear terminal
                    print(f"Sales Performance for {month} {year}".center(40, "-"))
                    
                    salesList = []

                    for product in productsDict["products"]:
                        numOfOrder = 0
                        for order in ordersDict["orders"]:
                            orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").month
                            orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").year
                            orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
                            
                            # Check if the order matches the selected month and year
                            if orderMonth == month and orderYear == year:
                                productList = eval(order["products"])
                                for orderProduct in productList:
                                    if orderProduct[0] == product["id"]:
                                        numOfOrder += orderProduct[2]
                        
                        # Print product performance
                        salesList.append([product["name"], numOfOrder])
                    salesTable = rFunctions.tabulateGivenData(["Food Name", "Number of Order"], salesList, tbfmt = "outline", align=("left", "center"))
                    print(salesTable)
                elif not valid:
                    continue
                elif [year, month] not in yearMonth:
                    raise ValueError(f"Invalid input ☹️ : No records for {month} {year}")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
        if not rFunctions.askContinue():
            break


#03 Product Popularity Page
def productPopularityPage():
    while True:
        os.system('cls')
        print("Product Popularity Page".center(66, "-"))
        print("List of available product popularity for:")
        sFunctions.productPopularityTop3()
        print()
        if not rFunctions.askContinue():
            break 