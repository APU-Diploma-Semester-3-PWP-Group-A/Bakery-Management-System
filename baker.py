import os, time, custom_modules.reusableFunctions as rFunctions, sharedFunctions as sFunctions
from datetime import datetime

#(B)(iii) Baker Page
def bakerPage(username):
    while True:
        os.system('cls')
        print(f"{rFunctions.color('bold', None)}" + "="*40 + "\n" + "Baker Home Page".center(40) + "\n" + "="*40 + f"{rFunctions.color('reset', None)}")
        print(f"Welcome {username},")
        print("1. 🍴 Recipe Management")
        print("2. 🚛 Inventory Check")
        print("3. 🧺 Production Record-keeping")
        print("4. 🛠 Equipment Management")
        print("5. 🔚 Log Out")
        print("-"*40)
        try:
            selection = input("Enter your selection: ").lower()
            if selection.isdigit():
                    selection = int(selection)
            if selection in [1, "recipe management", "1. recipe management"]:
                sFunctions.recipeManagement()
            elif selection in [2, "inventory check", "2. inventory check"]:
                sFunctions.inventoryReport()
            elif selection in [3, "production record-keeping", "3. production record-keeping"]:
                production_record_management()
            elif selection in [4, "equipment management", "4. equipment management"]:
                bakersDict = rFunctions.readFile("baker")
                for baker in bakersDict["bakers"]:
                    if baker["username"] == username:
                        bakerId = baker["id"]
                        break
                equipment_management(bakerId)
            elif selection in [5, "log out", "5. log out"]:
                while True:
                    try:
                        confirm = input("Enter <YES> to confirm log out or <NO> to cancel: ").lower()
                        if confirm == "yes":
                            logOut = True
                            break
                        elif confirm == "no":
                            logOut = False
                            break
                        else:
                            raise ValueError("Invalid input ☹️")
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


# Production record management
def production_record_management():
    while True:
        os.system('cls')
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Production Record Management".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print("1. 📋 View Production Availability")
        print("2. 📃 View Production Record")
        print("3. 🔐 Create Production Record")
        print("4. 🔙 Back")
        try:
            choice = input("Enter your choice: ").lower()
            if choice.isdigit():
                choice = int(choice)
            if choice in [1, "view product availability", "1. view product availability"]:
                sFunctions.productAvailability()
            elif choice in [2, "view production record", "2. view production record"]:
                sFunctions.displayProductionRecords()
            elif choice in [3, "create production record", "3. create production record"]:
                create_productRecord()
            elif choice in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()


def create_productRecord():
    while True:
        os.system('cls')
        productRecordsDict = rFunctions.readFile("product record")
        productsDict = rFunctions.readFile("product")
        inventoriesDict = rFunctions.readFile("inventorie")
        print("Create New Production Record".center(40, "-"))
        products = [(product["id"], product["name"]) for product in productsDict["products"]]
        print("List of Products:\n" + rFunctions.tabulateGivenData(["Product ID", "Name"], products, tbfmt = "simple_grid"))
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        try:
            productId = input("Enter Product ID Produced: ").upper()
            for product in productsDict['products']:
                if product['id'] == productId:
                    product_name = product['name']
                    ingredients = product["ingredients"]
                    break
            else:
                raise ValueError(f"Product ID '{productId}' not found.")
            production_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            production_quantity = int(input("Enter Production Quantity: "))
            if production_quantity <= 0:
                raise ValueError("Production Quantity cannot be 0 or negative.")
            product_specification = input("Enter Product Specification: ").strip()
            batch_number = rFunctions.assignId("product record", productRecordsDict)
            expiration_date = input("Enter Expiration Date (YYYY-MM-DD): ").strip()
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d").date()
            if expiration_date.year < datetime.now().year or (expiration_date.year == datetime.now().year and expiration_date.month < datetime.now().month) or (expiration_date.year == datetime.now().year and expiration_date.month == datetime.now().month and expiration_date.day < datetime.now().day):
                raise ValueError("Expiration Date cannot be in the past.")
            new_record = {
                "id": productId,
                "name": product_name,
                "production_datetime": production_datetime,
                "production_quantity": production_quantity,
                "product_specification": product_specification,
                "batch_num": batch_number,
                "expired_date": expiration_date
            }
            for product in productsDict["products"]:
                if product["id"] == productId:
                    product["quantity"] = int(product["quantity"]) + production_quantity
            rFunctions.appendFile("product record", productRecordsDict, new_record)
            rFunctions.writeFile("product", productsDict)
            updateMsg = ["Production record added successfully! 😄", "Product Quantity is updated! 😄"]
            for msg in updateMsg:
                print(f"{rFunctions.color('green', 'foreground')}{msg}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
            for ingredient in ingredients.split(", "):
                if rFunctions.extractChar(ingredient.split()[len(ingredient.split()) - 1]) in ["kg", "g", "ml", "liter", "liters"] or (ingredient.split())[len(ingredient.split()) - 1].isdigit():
                    ingredientQuantity = ingredient.rsplit(" ", 1)
                else:
                    quantityWithUnit = ingredient.split()
                    ingredientQuantity = [' '.join(quantityWithUnit[:len(quantityWithUnit) - 2]), f"{quantityWithUnit[len(quantityWithUnit) - 2]} {quantityWithUnit[len(quantityWithUnit) - 1]}"]
                quantity = rFunctions.extractNumber(ingredientQuantity[1])
                ingredientUnit = rFunctions.extractChar(ingredientQuantity[1])
                for inventory in inventoriesDict["inventories"]:
                    if inventory["name"].lower() == ingredientQuantity[0].lower():
                        inventoryUnit = rFunctions.extractChar(inventory["available quantity"])
                        if ingredientUnit != inventoryUnit:
                            if ingredientUnit in ["g", "ml"]:
                                quantity /= 1000
                        quantity *= production_quantity
                        availableQuantity = rFunctions.extractNumber(inventory["available quantity"]) - quantity
                        if inventoryUnit in ["kg", "g"]:
                            inventory["available quantity"] = f"{availableQuantity}{inventoryUnit}"
                        else:
                            inventory["available quantity"] = f"{availableQuantity} {inventoryUnit}"
            rFunctions.writeFile("inventorie", inventoriesDict)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


# Equipment Management
def equipment_management(bakerId):
    while True:
        os.system('cls')
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Equipment Management".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print("1. 🔧 Display Equipments")
        print("2. 📋 Monthly Maintenance Report")
        print("3. 📄 Malfunction Report")
        print("4. Back\n" + "-"*40)
        try:
            choice = input("Enter your choice: ").lower()
            if choice.isdigit():
                choice = int(choice)
            if choice in [1, "display equipments", "1. display equipments"]:
                sFunctions.displayEquipment()
            elif choice in [2, "monthly maintenance report", "2. monthly maintenance report"]:
                equipmentReport(bakerId)
            elif choice in [3, "malfunction report", "3. malfunction report"]:
                malfunctionReport(bakerId)
            elif choice in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()


def equipmentReport(bakerId):
    while True:
        os.system('cls')
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Monthly Equipment Maintenance Report".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print("1. 📋 Display Report")
        print("2. 📝 Add New Report")
        print("3. 🔙 Back")
        try:
            choice = input("Enter your selection: ").lower()
            if choice.isdigit():
                choice = int(choice)
            if choice in [1, "display report", "1. display report"]:
                sFunctions.displayEquipmentReport()
            elif choice in [2, "add new report", "2. add new report"]:
                addEquipmentReport(bakerId)
            elif choice in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()


def addEquipmentReport(bakerId):
    while True:
        try:
            equipmentReportsDict = rFunctions.readFile("equipment report")
            oldEquipmentReportsDict = rFunctions.readFile("equipment report")
            equipmentsDict = rFunctions.readFile("equipment")
            yearMonth = []
            for data in equipmentReportsDict["equipment reports"]:
                dataMonthInt = datetime.strptime(data["date"], "%Y-%m-%d").month
                dataYearInt = datetime.strptime(data["date"], "%Y-%m-%d").year
                dataMonth, dataYear, _ = rFunctions.validMonthYear(dataMonthInt, dataYearInt)
                yearMonth.append([dataYear, dataMonth]) if [dataYear, dataMonth] not in yearMonth else yearMonth
            month, year, _ = rFunctions.validMonthYear(datetime.now().month, datetime.now().year)
            os.system('cls')
            print(f"{rFunctions.color('bold', None)}" + "="*40 + "\n" + f"Add Equipment Report for {month} {year}".center(40) + "\n" + "="*40 + f"{rFunctions.color('reset', None)}")
            foundReport = False
            for data in yearMonth:
                if data[0] == year and data[1] == month:
                    foundReport = True
            if foundReport:
                print(f"{rFunctions.color('yellow', 'foreground')}Equipment Report for {month} {year} already existed 🙂{rFunctions.color('reset', None)}")
                if not rFunctions.askContinue():
                    break
            else:
                for equipment in equipmentsDict["equipments"]:
                    equipmentReportsDict = rFunctions.readFile("equipment report")
                    reportId = rFunctions.assignId("equipment report", equipmentReportsDict)
                    print(f"Report for {equipment["eqid"]} {equipment["eqname"]}:")
                    while True:
                        try:
                            condition = input("Enter equipment's condition [Good/ Fair/ Poor]: ").title()
                            rFunctions.clearPreviousLine()
                            if condition.lower() not in ["good", "fair", "poor"]:
                                raise ValueError("Invalid Input ☹️ : Equipment condition can only be 'Good', 'Fair', or 'Poor'.")
                            print(f"Condition: {condition}")
                            comments = input("Enter your comments: ").replace(",", ", ").replace(",  ", ", ")
                            rFunctions.clearPreviousLine()
                            print(f"Comments: {comments}\n")
                            report = {"reportID": reportId, "date": datetime.now().date(), "eqid": equipment["eqid"], "bakerID": bakerId, "condition": condition, "comments": comments}
                            rFunctions.appendFile("equipment report", equipmentReportsDict, report)
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                confirm = input("Enter <YES> to confirm: ").lower()
                rFunctions.clearPreviousLine()
                if confirm == "yes":
                    print(f"{rFunctions.color('green', 'foreground')}Equipment Report for {month} {year} is successfully added 😄{rFunctions.color('reset', None)}")
                else:
                    rFunctions.writeFile("equipment report", oldEquipmentReportsDict)
                    print(f"\n{rFunctions.color('red', 'foreground')}Equipment Report for {month} {year} is not added ☹️{rFunctions.color('reset', None)}")
                time.sleep(2)
                break
        except ValueError as vE:
            rFunctions.writeFile("equipment report", oldEquipmentReportsDict)
            print(f"\n{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break


def malfunctionReport(bakerId):
    while True:
        os.system('cls')
        print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Equipment Malfunction Report".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
        print("1. 📋 Display Report")
        print("2. 📝 Add New Report")
        print("3. 🔙 Back\n" + "-"*40)
        try:
            choice = input("Enter your selection: ").lower()
            if choice.isdigit():
                choice = int(choice)
            if choice in [1, "display report", "1. display report"]:
                while True:
                    sFunctions.displayMalfunctionReport()
                    time.sleep(2)
                    if not rFunctions.askContinue():
                        break
            elif choice in [2, "add new report", "2. add new report"]:
                malfunctionEquipment(bakerId)
            elif choice in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()


def malfunctionEquipment(bakerId):
    while True:
        try:
            malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction")
            equipmentsDict = rFunctions.readFile("equipment")
            print("\033c" + rFunctions.color('bold', None) + "Malfunction Equipment Report".center(40, "-") + rFunctions.color('reset', None) + "\nList of Equipments:")
            #eqid,eqname,model,purchased date,status,last_maintenance,next_maintenance
            print(rFunctions.tabulateCsvData("equipment", ["eqid", "eqname"], tbfmt = "simple_grid", headerName = ["Equipment ID", "Equipment Name"]))
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            equipmentId = input("Enter Equipment ID to report malfunction: ").upper()
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
            print(f"\033c{rFunctions.color('underline', None)}Equipment Details for {equipmentId}:{rFunctions.color('reset', None)}\n\n" + rFunctions.tabulateGivenData(["Field", "Details"], equipmentTable, tbfmt = "simple_grid", align = ("left", "left")) + "\n")
            malfunctionId = rFunctions.assignId("equipment malfunction", malfunctionEquipmentsDict)
            reportDate = datetime.now().date()
            issue = input("Enter Equipment Issue: ").replace(",", ", ").replace(",  ", ", ")
            rFunctions.clearPreviousLine()
            print(f"Issue: {issue}\n")
            while True:
                try:
                    urgencyLevel = input("Enter Urgency Level [High/Medium/Low]: ").title()
                    if urgencyLevel.lower() not in ["high", "medium", "low"]:
                        raise ValueError("Invalid Input ☹️ : Urgency level can only be 'High', 'Medium', or 'Low'.")
                    rFunctions.clearPreviousLine()
                    print(f"Urgency Level: {urgencyLevel}\n")
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            malfunctionDict = {"malfunctionID": malfunctionId, "report date": reportDate, "eqid": equipmentId, "bakerID": bakerId, "issue": issue, "urgency level": urgencyLevel, "status": "Unresolved", "resolution date": "", "resolution comments": ""}
                #malfunctionID,report date,eqid,bakerID,issue,urgency level,status,resolution date,resolution comments
            confirm = input("Enter <YES> to confirm: ").lower()
            rFunctions.clearPreviousLine()
            if confirm == "yes":
                for equipment in equipmentsDict["equipments"]:
                    if equipment["eqid"] == equipmentId:
                        equipment["status"] = "Need Maintenance"
                rFunctions.writeFile("equipment", equipmentsDict)
                rFunctions.appendFile("equipment malfunction", malfunctionEquipmentsDict, malfunctionDict)
                print(f"{rFunctions.color('green', 'foreground')}Equipment Malfunction Report for {equipmentId} is successfully reported 😄{rFunctions.color('reset', None)}")
            else:
                print(f"\n{rFunctions.color('red', 'foreground')}Equipment Malfunction Report for {equipmentId} is not reported ☹️{rFunctions.color('reset', None)}")
            time.sleep(2)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

