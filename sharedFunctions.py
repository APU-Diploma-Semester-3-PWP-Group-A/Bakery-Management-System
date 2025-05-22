#Shared function
import os, time, custom_modules.reusableFunctions as rFunctions
from tabulate import tabulate
from datetime import datetime

#Display certain product details
def productDetails(product: dict):
    productData = {
        "ID": product.get("id", ""),
        "Name": product.get("name", ""),
        "Flavour": product.get("flavour", ""),
        "Category": product.get("category", ""),
        "Price": product.get("price", ""),
        "Promotion": product.get("promotion", "") or "No promotion",
        "Description": product.get("description", "")
    }
    productTable = [(key, value) for key, value in productData.items()]
    print(tabulate(productTable, tablefmt="psql", colalign=("left", "left"), maxheadercolwidths = 40))


def displayRecipeInstructions(product: dict):
    instructions = product.get("instructions", "").split('|')
    stepsList = []
    for i, steps in enumerate(instructions):
        stepsList.append([(i + 1), steps.replace(f"{i + 1}. ", "")])
    print(tabulate(stepsList, headers = ["No", "instructions"], tablefmt = "simple_grid", colalign = ("center", "left"), maxcolwidths = [None, 60]))


def Displayrecipe(product: dict):
    productData = {
        "ID": product.get("id", ""),
        "Category": product.get("category", ""),
        "Name": product.get("name", ""),
        "Ingredients": product.get("ingredients", ""),
    }
    productTable = [(key, value) for key, value in productData.items()]
    print(tabulate(productTable, headers = ["Field", "Details"], tablefmt = "presto", colalign = ("left", "left"), maxcolwidths = [None, 40]))
    print()
    displayRecipeInstructions(product)


def productPopularityTop3():
    # Read data from files
    ordersDict = rFunctions.readFile("order")
    productsDict = rFunctions.readFile("product")

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
            month, year, valid = rFunctions.validMonthYear(month, year)
            
            # Validate input and ensure the month-year is available
            if valid and [year, month] in yearMonth:
                print("\033c")  # clear terminal
                print(f"Product Popularity for {month} {year}".center(40, "-"))
                break
            elif not valid:
                rFunctions.clearPreviousLine()
                continue
            elif [year, month] not in yearMonth:
                raise Exception(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ ： No records for {month} {year}{rFunctions.color('reset', None)}")
        except Exception as E:
            print(f"{rFunctions.color('red', 'foreground')}{E}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
    print()
    productOrderCount = []

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
            productOrderCount.append((product['name'],numOfOrder))

    productOrderCount.sort(key = lambda x: x[1], reverse = True)
    for i in range(3):
        if i == 0:
            rank = "🥇"
        elif i == 1:
            rank = "🥈"
        elif i == 2:
            rank = "🥉"
        print(f"{rank} {productOrderCount[i][0]}: {productOrderCount[i][1]}")
    return productOrderCount[:3]


def recipeManagement():
    while True:
        try:
            print("\033c" + rFunctions.color('bold', None) + "Recipe Management".center(40, "-") + rFunctions.color('reset', None) + "\n1. ➕ Add Product\n2. 🔧 Modify Product\n3. 🗑️  Remove Product\n4. 🔙 Back\n" + "-"*40)
            functionality = input("Enter your selection: ").lower()
            if functionality.isdigit():
                functionality = int(functionality)
            if functionality in [1, "add product", "1. add product"]:
                addProduct()
            elif functionality in [2, "modify product", "2. modify product"]:
                modifyProduct()
            elif functionality in [3, "remove product", "3. remove product"]:
                removeProduct()
            elif functionality in [4, "back", "4. back"]:
                break
            else:
                raise ValueError(f"Invalid Input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def addProduct():
    while True:
        productsDict = rFunctions.readFile("product")
        print("\033c" + "Add New Product".center(40, "-"))
        showProduct = input("Enter <YES> to show all available products: ").lower()
        rFunctions.clearPreviousLine()
        if showProduct == "yes":
            categories = []
            print("\nList of Available Products:")
            for product in productsDict["products"]:
                categories.append(product["category"]) if product["category"] not in categories else categories
            for category in categories:
                products = []
                for product in productsDict["products"]:
                    products.append([product["id"], product["name"]]) if product["category"] == category else products
                print(f"{rFunctions.color('underline', None)}{category}{rFunctions.color('reset', None)}\n" + rFunctions.tabulateGivenData(["Product ID", "Name"], products, tbfmt = "simple_grid") + "\n")
        if not rFunctions.askContinue():
            break
        while True:
            try:
                productsDict = rFunctions.readFile("product")
                print("\033c" + "Add New Product".center(40, "-"))
                productCategory = input("Enter product category: ").title()
                rFunctions.clearPreviousLine()
                print(f"Category: {productCategory}\n")
                productName = input("Enter product name: ").title()
                rFunctions.clearPreviousLine()
                if productName.lower() in [product["name"].lower() for product in productsDict["products"]]:
                    raise ValueError(f"Invalid Input ☹️ :Product already existed")
                print(f"Name: {productName}\n")
                productFlavour = input("Enter product flavour: ").title()
                rFunctions.clearPreviousLine()
                print(f"Flavour: {productFlavour}\n")
                productPrice = input("Enter product price (RM): ")
                foundDigit = False
                for i, char in enumerate(productPrice):
                    if i == 0 and char.isdigit():
                        foundDigit = True
                        productPrice = rFunctions.extractNumber(productPrice)
                        break
                    if char.isdigit():
                        foundDigit = True
                        if productPrice[i - 1] == "-":
                            raise ValueError(f"Invalid Input ☹️ :Product price cannot be negative")
                        productPrice = rFunctions.extractNumber(productPrice)
                        break
                if foundDigit:
                    if int(productPrice) == 0:
                        raise ValueError(f"Invalid Input ☹️ :Product price cannot be zero")
                else:
                    raise ValueError(f"Invalid Input ☹️ :Product price not given")
                rFunctions.clearPreviousLine()
                print(f"Price: RM{productPrice:.2f}\n")
                productDescription = input("Enter product description: ").lower().replace(",", ", ").replace(",  ", ", ")
                rFunctions.clearPreviousLine()
                print(f"Description: {productDescription}\n")
                ingredientList = []
                index = 1
                print("Ingredients:")
                while True:
                    try:
                        ingredients = input("Enter product ingredients (no quantity) or '-1' to exit: ")
                        rFunctions.clearPreviousLine()
                        if ingredients == "-1":
                            break
                        else:
                            ingredients = ingredients.rsplit(" ", 2)[0]
                            quantity = input("Enter quantity of ingredients (specify unit): ").replace(" ", "")
                            rFunctions.clearPreviousLine()
                            foundDigit = False
                            for i, char in enumerate(quantity):
                                if i == 0 and char.isdigit():
                                    foundDigit = True
                                    break
                                if char.isdigit():
                                    foundDigit = True
                                    if quantity[i - 1] == "-":
                                        raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be negative")
                                    break
                            if foundDigit:
                                if int(rFunctions.extractNumber(quantity)) == 0:
                                    raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be zero")
                            else:
                                raise ValueError(f"Invalid Input ☹️ :No ingredient quantity given")
                            print(f"{index}. {ingredients} {quantity}")
                            ingredientList.append(f"{ingredients} {quantity}")
                            index += 1
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                productIngredients = ", ".join(ingredient for ingredient in ingredientList)
                index = 1
                instructionsList = []
                print("\nInstructions:")
                while True:
                    instructions = input(f"Enter instructions Step {index} or '-1' to exit: ").capitalize().replace(",", ", ").replace(",  ", ", ")
                    rFunctions.clearPreviousLine()
                    if instructions == "-1":
                        break
                    else:
                        print(f"{index}. {instructions}")
                        instructionsList.append(f"{index}. {instructions}")
                        index += 1
                productInstructions = "|".join(instruction for instruction in instructionsList)
                print()
                productNutritionInfo = input("Enter product nutrition info (x calories per unit): ")
                rFunctions.clearPreviousLine()
                print(f"Nutrition info: {productNutritionInfo}\n")
                productAllergenInfo = input("Enter product allergen info: ").replace(",", ", ").replace(",  ", ", ")
                rFunctions.clearPreviousLine()
                print(f"Allergen info: {productAllergenInfo}")
                time.sleep(2)
                print("\033c" + "Add New Product".center(40, "-"))
                newProduct = {"id": rFunctions.assignId("product", productsDict), "category": productCategory, "name": productName, "flavour": productFlavour, "price": "RM%.2f"%(productPrice), "promotion": "", "description": productDescription, "ingredients": productIngredients, "instructions": productInstructions, "nutrition info": productNutritionInfo, "allergen info": productAllergenInfo, "threshold quantity": 20, "quantity": 0}
                productDetails = [[key.capitalize(), value] for key, value in newProduct.items() if key in ["id", "category", "name", "flavour", "price", "description", "ingredients", "nutrition info", "allergen info"]]
                print("Product Details:\n" + rFunctions.tabulateGivenData(["Field", "Details"], productDetails, tbfmt = "simple_grid") + "\n\nProduct Recipe Instructions:")
                displayRecipeInstructions(newProduct)
                confirm = input("Enter <CONFIRM> to Save Product: ").lower()
                rFunctions.clearPreviousLine()
                if confirm != "confirm":
                    print(f"{rFunctions.color('red', 'foreground')}Product '{productName}' is not saved ☹️{rFunctions.color('reset', None)}")
                else:
                    rFunctions.appendFile("product", productsDict, newProduct)
                    print(f"{rFunctions.color('green', 'foreground')}Product '{productName}' is successfully saved 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                if not rFunctions.askContinue():
                    break
            except ValueError as vE:
                print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                print()
                if not rFunctions.askContinue():
                    break
        break

def modifyProduct():
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            print("\033c" + "Modify Existing Product".center(40, "-"))
            showProduct = input("Enter <YES> to show all available products: ").lower()
            rFunctions.clearPreviousLine()
            if showProduct == "yes":
                categories = []
                print("\nList of Available Products:")
                for product in productsDict["products"]:
                    categories.append(product["category"]) if product["category"] not in categories else categories
                for category in categories:
                    products = []
                    for product in productsDict["products"]:
                        products.append([product["id"], product["name"]]) if product["category"] == category else products
                    print(f"{rFunctions.color('underline', None)}{category}{rFunctions.color('reset', None)}\n" + tabulate(products, headers = ["Product ID", "Name"], tablefmt = "simple_grid",maxcolwidths = [None, 60]) + "\n")
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            while True:
                try:
                    productId = input("Enter product ID: ").upper()
                    if not rFunctions.checkUniqueData("product", "id", productId, productsDict):
                        raise ValueError(f"Invalid Input ☹️ : Product ID '{productId}' does not exists")
                    rFunctions.clearPreviousLine()
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            while True:
                try:
                    productsDict = rFunctions.readFile("product")
                    for product in productsDict["products"]:
                        if product["id"] == productId:
                            productDict = product
                            productDetails = [[key.capitalize(), value] for key, value in product.items() if key in ["id", "category", "name", "flavour", "price", "description", "ingredients", "nutrition info", "allergen info"]]
                    print("\033c" + "Modify Existing Product Details".center(40, "-"))
                    print("Product Details:\n" + rFunctions.tabulateGivenData(["Field", "Details"], productDetails, tbfmt = "simple_grid") + "\n\nProduct Recipe Instructions:")
                    displayRecipeInstructions(productDict)
                    print(f"{rFunctions.color('blue', 'foreground')}Can only modify{rFunctions.color('bold', None)} Category, Name, Flavour, Price, Description, Ingredients, Instructions, Nutrition Info, and Allergen Info{rFunctions.color('reset', None)}\n")
                    modify = input("Enter what to modify: ").lower()
                    rFunctions.clearPreviousLine()
                    if modify not in ["category", "name", "flavour", "price", "description", "ingredients", "instructions", "nutrition info", "allergen info"]:
                        raise ValueError(f"Invalid Input ☹️ : {modify} cannot be modified")
                    for product in productsDict["products"]:
                        if product["id"] == productId:
                            if modify in ["name", "category", "flavour"]:
                                newData = input(f"Enter new product {modify}: ").title()
                                if modify == "name":
                                    if newData.lower() in [product["name"].lower() for product in productsDict["products"]]:
                                        raise ValueError(f"Invalid Input ☹️ : {newData} already existed")
                                product[f"{modify}"] = newData
                            elif modify == "price":
                                newPrice = input("Enter new product price: ")
                                foundDigit = False
                                for i, char in enumerate(newPrice):
                                    if i == 0 and char.isdigit():
                                        foundDigit = True
                                        newPrice = rFunctions.extractNumber(newPrice)
                                        break
                                    elif char.isdigit():
                                        foundDigit = True
                                        if newPrice[i - 1] == "-":
                                            raise ValueError(f"Invalid Input ☹️ :Product price cannot be negative")
                                        newPrice = rFunctions.extractNumber(newPrice)
                                        break
                                if foundDigit:
                                    if int(newPrice) == 0:
                                        raise ValueError(f"Invalid Input ☹️ :Product price cannot be zero")
                                else:
                                    raise ValueError("Product price not given")
                                product["price"] = f"RM{newPrice:.2f}"
                            elif modify == "ingredients":
                                ingredientList = []
                                index = 1
                                print("Ingredients:")
                                while True:
                                    newIngredients = input("Enter product ingredients (no quantity) or '-1' to exit: ")
                                    rFunctions.clearPreviousLine()
                                    if newIngredients == "-1":
                                        break
                                    else:
                                        newIngredients = newIngredients.rsplit(" ", 2)[0]
                                        quantity = input("Enter quantity of ingredients (specify unit): ")
                                        rFunctions.clearPreviousLine()
                                        foundDigit = False
                                        for i, char in enumerate(quantity):
                                            if i == 0 and char.isdigit():
                                                foundDigit = True
                                                break
                                            elif char.isdigit():
                                                foundDigit = True
                                                if quantity[i - 1] == "-":
                                                    raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be negative")
                                        if foundDigit:
                                            if int(rFunctions.extractNumber(quantity)) == 0:
                                                raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be zero")
                                        else:
                                            raise ValueError(f"Invalid Input ☹️ :No ingredient quantity given")
                                        if rFunctions.extractChar(quantity) in ["kg", "liter", "liter", "g", "ml"]:
                                            quantity = quantity.replace(" ", "")
                                        print(f"{index}. {newIngredients} {quantity}")
                                        ingredientList.append(f"{newIngredients} {quantity}")
                                        index += 1
                                product["ingredients"] = ", ".join(ingredient for ingredient in ingredientList)
                                print("\n")
                            elif modify == "instructions":
                                index = 1
                                instructionsList = []
                                print("Instructions:")
                                while True:
                                    newInstructions = input(f"Enter instructions Step {index} or '-1' to exit: ").capitalize().replace(",", ", ").replace(",  ", ", ")
                                    rFunctions.clearPreviousLine()
                                    if newInstructions == "-1":
                                        break
                                    else:
                                        print(f"{index}. {newInstructions}")
                                        instructionsList.append(f"{index}. {newInstructions}")
                                        index += 1
                                product["instructions"] = "|".join(instruction for instruction in instructionsList)
                                print("\n")
                            elif modify in ["description", "nutrition info", "allergen info"]:
                                newData = input(f"Enter new product {modify}: ").lower().replace(",", ", ").replace(",  ", ", ")
                                if modify == "name":
                                    if newData.lower() in [product["name"].lower() for product in productsDict["products"]]:
                                        raise ValueError(f"Invalid Input ☹️ : {newData} already existed")
                                product[f"{modify}"] = newData
                    rFunctions.writeFile("product", productsDict)
                    rFunctions.clearPreviousLine()
                    print(f"{rFunctions.color('green', 'foreground')}Product {modify} has been successfully updated😄{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    if not rFunctions.askContinue():
                        break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def removeProduct():
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            print("\033c" + "Remove Existing Product".center(40, "-"))
            showProduct = input("Enter <YES> to show all available products: ").lower()
            rFunctions.clearPreviousLine()
            if showProduct == "yes":
                categories = []
                print("\nList of Available Products:")
                for product in productsDict["products"]:
                    categories.append(product["category"]) if product["category"] not in categories else categories
                for category in categories:
                    products = []
                    for product in productsDict["products"]:
                        products.append([product["id"], product["name"]]) if product["category"] == category else products
                    print(f"{rFunctions.color('underline', None)}{category}{rFunctions.color('reset', None)}\n" + rFunctions.tabulateGivenData(["Product ID", "Name"], products, tbfmt = "simple_grid") + "\n")
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            while True:
                try:
                    productId = input("Enter product ID: ").upper()
                    if not rFunctions.checkUniqueData("product", "id", productId, productsDict):
                        raise ValueError(f"Invalid Input ☹️ : Product ID '{productId}' does not exists")
                    rFunctions.clearPreviousLine()
                    for i, product in enumerate(productsDict["products"]):
                        if product["id"] == productId:
                            productDict = product
                            productDetails = [[key.capitalize(), value] for key, value in product.items() if key in ["id", "category", "name", "flavour", "price", "description", "ingredients", "nutrition info", "allergen info"]]
                            del productsDict["products"][i]
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            print("\033c" + "Remove Existing Product".center(40, "-"))
            print("Product Details:\n" + tabulate(productDetails, ["Field", "Details"], tablefmt = "simple_grid", maxcolwidths = [None, 60]) + "\n\nProduct Recipe Instructions:")
            displayRecipeInstructions(productDict)
            confirm = input("Enter <CONFIRM> to Delete Product: ").lower()
            rFunctions.clearPreviousLine()
            if confirm != "confirm":
                print(f"{rFunctions.color('red', 'foreground')}Product '{productDict["id"]}' is not deleted ☹️{rFunctions.color('reset', None)}")
            else:
                rFunctions.writeFile("product", productsDict)
                print(f"{rFunctions.color('green', 'foreground')}Product '{productDict["id"]}' is successfully deleted 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


def inventoryReport():
    while True:
        try:
            inventoriesDict = rFunctions.readFile("inventorie")
            print("\033c" + rFunctions.color('bold', None) + "-"*40 + "\n" + "Inventory Report".center(40) + "\n" + "-"*40 + rFunctions.color('reset', None))
            categories = []
            for ingredient in inventoriesDict["inventories"]:
                categories.append(ingredient["category"]) if ingredient["category"] not in categories else categories
            categoriesList = []
            for i, category in enumerate(categories, 1):
                categoriesList.append((i, category))
            print("Ingredient Categories:\n" + rFunctions.tabulateGivenData(["No", "Categories"], categoriesList, tbfmt = "simple_grid"))
            category = input("Enter category to view stock levels: ").lower()
            if category not in [category.lower() for category in categories]:
                raise ValueError(f"Invalid Input ☹️ : {category} not found")
            ingredientListOfList = []
            for ingredient in inventoriesDict["inventories"]:
                if ingredient["category"].lower() == category:
                    stockLevel = f"{rFunctions.color('green', 'foreground')}Sufficient{rFunctions.color('reset', None)}"
                    if rFunctions.extractNumber(ingredient["available quantity"]) <= rFunctions.extractNumber(ingredient["threshold quantity"]):
                        stockLevel = f"{rFunctions.color('red', 'foreground')}Low{rFunctions.color('reset', None)}"
                    ingredientList = [ingredient["name"], ingredient["threshold quantity"], ingredient["available quantity"], stockLevel]
                    ingredientListOfList.append(ingredientList)
            print("\033c" + rFunctions.color('bold', None) + "="*40 + "\n" + f"Inventory Report for {datetime.now().strftime("%B")} {datetime.now().strftime("%Y")}".center(40) + "\n" + "="*40 + rFunctions.color('reset', None))
            print(f"\n{category.capitalize()}:\n" + rFunctions.tabulateGivenData(["Name", "Threshold Quantity", "Available Stocks", "Stock Level"], ingredientListOfList, tbfmt = "simple_grid", align = ("left", "right", "right", "center")) + "\n")
            time.sleep(2)
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


def displayProductionRecords():
    while True:
        try:
            productRecordsDict = rFunctions.readFile("product record")
            print("\033c" + rFunctions.color('bold', None) + "Display Monthly Production Record".center(40, "-") + rFunctions.color('reset', None) + "\nList of Available Production Records:")
            yearMonth = []
            for record in productRecordsDict["product records"]:
                recordMonthInt = datetime.strptime(record["production_datetime"], "%Y-%m-%d").date().month
                recordYearInt = datetime.strptime(record["production_datetime"], "%Y-%m-%d").date().year
                recordMonth, recordYear, _ = rFunctions.validMonthYear(recordMonthInt, recordYearInt)
                yearMonth.append([recordYear, recordMonth]) if [recordYear, recordMonth] not in yearMonth else yearMonth
            print(rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            productIdNames = []
            allRecords = []
            if [year, month] in yearMonth and valid:
                print("\033c" + "="*40 + "\n" + f"Production Records in {month} {year}".center(40) + "\n" + "="*40)
                for record in productRecordsDict["product records"]:
                    recordMonthInt = datetime.strptime(record["production_datetime"], "%Y-%m-%d").date().month
                    recordYearInt = datetime.strptime(record["production_datetime"], "%Y-%m-%d").date().year
                    recordMonth, recordYear, _ = rFunctions.validMonthYear(recordMonthInt, recordYearInt)
                    if recordMonth == month and recordYear == year:
                        productIdNames.append([record["id"], record["name"]]) if [record["id"], record["name"]] not in productIdNames else productIdNames
                        allRecords.append([record["id"], record["production_datetime"], record["production_quantity"], record["expired_date"]])
                for product in productIdNames:
                    records = []
                    index = 1
                    for record in allRecords:
                        if record[0] == product[0]:
                            records.append([index, record[1], record[2], record[3]])
                            index += 1
                    print(f"{product[0]} {product[1]}\n" + rFunctions.tabulateGivenData(["No", "Production Date", "Production Quantity", "Expiration Date"], records, tbfmt = "simple_grid", align = ("center", "center", "right", "center")) + "\n")
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for order in {month} {year}")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


def productAvailability():
    while True:
        productsDict = rFunctions.readFile("product")
        print("\033c" + rFunctions.color('bold', None) + "="*40 + "\n" + "Current Product Availability".center(40) + "\n" + "="*40 + rFunctions.color('reset', None) + "\n")
        productCategories = []
        for product in productsDict["products"]:
            productCategories.append(product["category"]) if product["category"] not in productCategories else productCategories
        for category in productCategories:
            products = []
            for product in productsDict["products"]:
                if product["category"] == category:
                    if int(product["quantity"]) > int(product["threshold quantity"]):
                        products.append([product["id"], product["name"], product["threshold quantity"], product["quantity"], f"{rFunctions.color('green', 'foreground')}Sufficient{rFunctions.color('reset', None)}"])
                    else:
                        products.append([product["id"], product["name"], product["threshold quantity"], product["quantity"], f"{rFunctions.color('red', 'foreground')}Low{rFunctions.color('reset', None)}"])
            print(f"{category}:\n{rFunctions.tabulateGivenData(["Product ID", "Product Name", "Threshold Quantity", "Available Goods", "Goods Level"], products, tbfmt = "simple_grid", align = ("left", "left", "right", "right", "center"))}\n")
        time.sleep(2)
        while True:
            try:
                exit = input("Enter 0 to <EXIT>: ")
                if not exit.isdigit():
                    raise ValueError("Invalid Input :(" + "\n" + "Please Try Again...")
                elif int(exit) == 0:
                    break
                else:
                    raise ValueError("Invalid Input :(" + "\n" + "Please Try Again...")
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        break


def displayEquipment():
    while True:
        try:
            equipmentsDict = rFunctions.readFile("equipment")
            print("\033c" + rFunctions.color('bold', None) + "Display Equipments".center(40, "-") + rFunctions.color('reset', None) + "\nList of Equipments:")
            #eqid,eqname,model,purchased date,status,last_maintenance,next_maintenance
            print(rFunctions.tabulateCsvData("equipment", ["eqid", "eqname"], tbfmt = "simple_grid", headerName = ["Equipment ID", "Equipment Name"]))
            equipmentId = input("Enter Equipment ID to view details: ").upper()
            if not rFunctions.checkUniqueData("equipment", "eqid", equipmentId, equipmentsDict):
                raise ValueError(f"Invalid input ☹️ : Equipment ID '{equipmentId}' does not exists.")
            for equipment in equipmentsDict["equipments"]:
                if equipment["eqid"] == equipmentId:
                    equipmentData = {
                    "Equipment ID": equipment.get("eqid", ""),
                    "Equipment Name": equipment.get("eqname", ""),
                    "Model": equipment.get("model", ""),
                    "Purchased Date": equipment.get("purchased date", ""),
                    "Status": equipment.get("status", ""),
                    "Last Maintenance": equipment.get("last_maintenance") if equipment.get("last_maintenance") != '' else "N/A",
                    "Next Maintenance": equipment.get("next_maintenance") if equipment.get("next_maintenance") != '' else "N/A"
                    }
            equipmentTable = [(key, value) for key, value in equipmentData.items()]
            print(f"\033c{rFunctions.color('underline', None)}Equipment Details for {equipmentId}:{rFunctions.color('reset', None)}\n\n" + tabulate(equipmentTable, headers = ["Field", "Details"], tablefmt = "simple_grid", colalign = ("left", "left")))
            print()
            time.sleep(2)
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


def displayEquipmentReport():
    while True:
        try:
            equipmentReportsDict = rFunctions.readFile("equipment report")
            yearMonth = []
            for data in equipmentReportsDict["equipment reports"]:
                dataMonthInt = datetime.strptime(data["date"], "%Y-%m-%d").month
                dataYearInt = datetime.strptime(data["date"], "%Y-%m-%d").year
                dataMonth, dataYear, _ = rFunctions.validMonthYear(dataMonthInt, dataYearInt)
                yearMonth.append([dataYear, dataMonth]) if [dataYear, dataMonth] not in yearMonth else yearMonth
            print("\033c" + rFunctions.color('bold', None) + "Display Equipment Report".center(40, "-") + rFunctions.color('reset', None) + "\nList of Available Equipment Records:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            if [year, month] in yearMonth and valid:
                equipmentReports = []
                for report in equipmentReportsDict["equipment reports"]:
                    reportMonthInt = datetime.strptime(report["date"], "%Y-%m-%d").month
                    reportYearInt = datetime.strptime(report["date"], "%Y-%m-%d").year
                    reportMonth, reportYear, _ = rFunctions.validMonthYear(reportMonthInt, reportYearInt)
                    if reportYear == year and reportMonth == month:
                        bakerId = report["bakerID"]
                        reportDate = report["date"]
                        equipmentsDict = rFunctions.readFile("equipment")
                        for equipment in equipmentsDict["equipments"]:
                            if equipment["eqid"] == report["eqid"]:
                                equipmentName = equipment["eqname"]
                                break
                        if report["condition"] == "Good":
                            equipmentReports.append([report["eqid"], equipmentName, f"{rFunctions.color('green', 'foreground')}{report["condition"]}{rFunctions.color('reset', None)}", report["comments"]])
                        elif report["condition"] == "Fair":
                            equipmentReports.append([report["eqid"], equipmentName, f"{rFunctions.color('yellow', 'foreground')}{report["condition"]}{rFunctions.color('reset', None)}", report["comments"]])
                        else:
                            equipmentReports.append([report["eqid"], equipmentName, f"{rFunctions.color('red', 'foreground')}{report["condition"]}{rFunctions.color('reset', None)}", report["comments"]])
                bakersDict = rFunctions.readFile("baker")
                for baker in bakersDict["bakers"]:
                    if baker["id"] == bakerId:
                        print("\033c" + "="*40 + "\n" + f"Equipment Records in {month} {year}".center(40) + "\n" + "="*40)
                        print(f"Reported by: {bakerId} {baker["name"]}\nReport Date: {reportDate}\n" + rFunctions.tabulateGivenData(["Equipment ID", "Equipment Name", "Condition", "Baker Comments"], equipmentReports, tbfmt = "simple_grid") + "\n")
                        break
                time.sleep(2)
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for equipments in {month} {year}")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


def displayMalfunctionReport():
    while True:
        try:
            malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction")
            equipmentsDict = rFunctions.readFile("equipment")
            bakersDict = rFunctions.readFile("baker")
            print("\033c" + rFunctions.color('bold', None) + "Display Malfunction Report".center(40, "-") + rFunctions.color('reset', None) + "\nList of Equipments:")
            #eqid,eqname,model,purchased date,status,last_maintenance,next_maintenance
            print(rFunctions.tabulateCsvData("equipment", ["eqid", "eqname"], tbfmt = "simple_grid", headerName = ["Equipment ID", "Equipment Name"]))
            equipmentId = input("Enter Equipment ID to view malfunction report: ").upper()
            if not rFunctions.checkUniqueData("equipment", "eqid", equipmentId, equipmentsDict):
                raise ValueError(f"Invalid input ☹️ : Equipment ID '{equipmentId}' does not exists.")
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
    malfunctionIds = []
    malfunctionReports = []
    for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
        if equipment["eqid"] == equipmentId:
            #malfunctionID,report date,eqid,bakerID,issue,urgency level,status,resolution date,resolution comments
            for baker in bakersDict["bakers"]:
                if baker["id"] == equipment["bakerID"]:
                    bakerName = baker["name"]
                    break
            malfunctionIds.append(equipment["malfunctionID"])
            malfunctionReports.append([equipment["malfunctionID"], equipment["report date"], f"{equipment["bakerID"]} {bakerName}"])
    while True:
        try:
            if len(malfunctionReports) != 0:
                print("\033c" + f"{rFunctions.color('underline', None)}List of Malfunction Reports for {equipmentId}:{rFunctions.color('reset', None)}\n\n" + rFunctions.tabulateGivenData(["Report ID", "Report Date", "Reported By"], malfunctionReports, tbfmt = "simple_grid"))
                reportId = input("Enter Malfunction Report ID: ").upper()
                if reportId not in malfunctionIds:
                    raise ValueError(f"Invalid input ☹️ : Malfunction Report ID '{reportId}' does not exists or is for another equipment.")
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
    if len(malfunctionReports) == 0:
        print(f"{rFunctions.color('yellow', 'foreground')}No Malfunction Reports for {equipmentId} 🙂{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()
        print()
        return
    for item in equipmentsDict["equipments"]:
        if item["eqid"] == equipmentId:
            equipmentName = item["eqname"]
    for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
        if equipment["malfunctionID"] == reportId:
            if equipment["status"] == "Resolved":
                color = rFunctions.color('green', 'foreground')
            elif equipment["status"] == "In Progress":
                color = rFunctions.color('yellow', 'foreground')
            else:
                color = rFunctions.color('red', 'foreground')
            equipmentData = {
            "Equipment ID": equipment.get("eqid", ""),
            "Equipment Name": equipmentName,
            "Issue": equipment.get("issue", ""),
            "Urgency Level": equipment.get("urgency level", ""),
            "Status": f"{color}{equipment.get("status", "")}{rFunctions.color('reset', None)}",
            "Resolution Date": equipment.get("resolution date") if equipment.get("resolution date") != '' else "N/A",
            "Resolution Comment by Manager": equipment.get("resolution comments") if equipment.get("resolution comments") != '' else "N/A"
            }
    malfunctionTable = [(key, value) for key, value in equipmentData.items()]
    print(f"\033c{rFunctions.color('underline', None)}Malfunction Report for {equipmentId}:{rFunctions.color('reset', None)}\n\n" + tabulate(malfunctionTable, headers = ["Field", "Details"], tablefmt = "simple_grid", colalign = ("left", "left")) + "\n")
    time.sleep(2)
