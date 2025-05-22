import os, time, custom_modules.reusableFunctions as rFunctions, sharedFunctions as sFunctions
#AttributeError if just import datetime.
#the strptime function is part of the datetime class within the datetime module
from datetime import datetime

#(B)(i) Manager Page
def managerPage(username: str):
    while True:
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}{"="*40}
{"Manager Page".center(40)}
{"="*40}{rFunctions.color('reset', None)}
Welcome Manager {username},
1. 🖥️  System Administration
2. 🧾 Order Management
3. 💰 Financial Management
4. 🚛 Inventory Control
5. 🎛️  Equipment Management
6. ⭐ Customer Feedback
7. 🔒 Log out
{"-"*40}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit(): #if functionality consist of all digits
                functionality = int(functionality)
            if functionality in [1, "system administration", "1. system administration"]:
                systemAdministration()
            elif functionality in [2, "order management", "2. order management"]:
                orderManagement()
            elif functionality in [3, "financial management", "3. financial management"]:
                financialManagement()
            elif functionality in [4, "inventory control", "4. inventory control"]:
                inventoryControl()
            elif functionality in [5, "equipment management", "5. equipment management"]:
                equipmentManagement()
            elif functionality in [6, "customer feedback", "6. customer feedback"]:
                viewCustomerFeedback()
            elif functionality in [7, "log out", "7. log out"]:
                rFunctions.clearPreviousLine()
                while True: #to keep confirm log out until get 'yes' or 'no'
                    try:
                        confirm = input("Enter <YES> to confirm log out or <NO> to cancel: ").lower()
                        if confirm == "yes":
                            logOut = True
                            break
                        elif confirm == "no":
                            logOut = False
                            break
                        else:
                            raise ValueError("Invalid input ☹️") #invalid input, trigger exception handling
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

# Functionality 01: System Administration
def systemAdministration():
    while True:
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}
{"-"*40}
{"System Administration".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🛠️  Employee Management
2. 🙋 Customer Management
3. 🔙 Back
{"-"*40}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit(): #if functionality consist of all digits
                functionality = int(functionality)
            if functionality in [1, "employee management", "1. employee management"]:
                employeeManagement()
            elif functionality in [2, "customer management", "2. customer management"]:
                customerManagement()
            elif functionality in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2) #loop continues

#(i) Employee Management
def employeeManagement():
    while True: #infinite outer while loop
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}
{"-"*40}
{"Employee Management".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🔐 Create New Account
2. 📝 Update Account
3. 🗑️  Delete Account
4. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        operation = input("Enter selection: ").lower()
        try:
            if operation.isdigit():
                operation = int(operation)
            if operation in [1, "create new account", "1. create new account"]:
                addEmployee()
            elif operation in [2, "update account", "2. update account"]:
                modifyEmployee()
            elif operation in [3, "delete account", "3. delete account"]:
                deleteEmployee()
            elif operation in [4, "back", "4. back"]:
                break #break outer while loop, exit function
            else:
                raise ValueError("Invalid input ☹️") #invalid input triggers error handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2) #loop continues

def addEmployee():
    while True:
        cashiersDict = rFunctions.readFile("cashier") #read cashiers data
        bakersDict = rFunctions.readFile("baker") #read bakers data
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"New Employee Enrolment".center(40)}
{"-"*40}{rFunctions.color('reset', None)}""")
        try:
            role = input("Enter Employee Role [Cashier/ Baker]: ").lower()
            if role != "cashier" and role != "baker":
                raise ValueError("Invalid role ☹️ : role either Cashier or Baker")
            id = rFunctions.assignId("cashier", cashiersDict) if role == "cashier" else rFunctions.assignId("baker", bakersDict)
            name = input("Enter Employee's Name: ")
            username = input("Enter Employee's Username: ")
            if rFunctions.checkUniqueData("cashier", "username", username, cashiersDict) or rFunctions.checkUniqueData("baker", "username", username, bakersDict):
                raise ValueError(f"Invalid employee username ☹️ : Employee username {username} already existed")
            errorMsg, validUsername = rFunctions.validData(username = username) #check the validity of username
            if not validUsername:
                raise ValueError(f"Invalid employee username ☹️ : {errorMsg}")
            password = input("Enter password: ")
            errorMsg, validPassword = rFunctions.validData(password = password) #check validity of password
            if not validPassword:
                raise ValueError(f"Invalid employee password ☹️ : {errorMsg}")
            age = int(input("Enter Employee's Age: "))
            if age <= 15: #check whether age of employee is above 15
                raise ValueError(f"Invalid employee age ☹️ : Employee age cannot be younger than 15 years old.")
            gender = input("Enter Employee's Gender: ")
            errorMsg, validGender = rFunctions.validData(gender = gender) #check validity of gender
            if not validGender:
                raise ValueError(f"Invalid employee gender ☹️ : {errorMsg}")
            phoneNum = input("Enter Employee's Phone Number (01X-XXX XXXX): ")
            errorMsg, validPhoneNum = rFunctions.validData(phoneNumber = phoneNum) #check validity of phone number
            if not validPhoneNum:
                raise ValueError(f"Invalid employee phone number ☹️ : {errorMsg}")
            email = input("Enter Employee's Email: ")
            errorMsg, validEmail = rFunctions.validData(email = email) #check validity of email
            if not validEmail:
                raise ValueError(f"Invalid employee email ☹️ : {errorMsg}")
            newEmployee = {"id": id, "name": name, "username": username, "password": password, "age": age, "gender": gender, "phone number": phoneNum, "email": email}
            if role == "cashier":
                rFunctions.appendFile("cashier", cashiersDict, newEmployee) #add new employee to cashier csv file
                time.sleep(2)
                print(f"{rFunctions.color('green', 'foreground')}New cashier '{name}' is enrolled 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            elif role == "baker":
                rFunctions.appendFile("baker", bakersDict, newEmployee) #add new employee to baker csv file
                time.sleep(2)
                print(f"{rFunctions.color('green', 'foreground')}New baker '{name}' is enrolled 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            break
        except ValueError as vE:
            print(f"\n{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue(): #ask to continue or to exit
                break #if False, break outer while loop, exit function

def modifyEmployee():
    while True:
        cashiersDict = rFunctions.readFile("cashier") #read cashiers data
        bakersDict = rFunctions.readFile("baker") #read bakers data
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Employee Account Update".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🪪  Employee Name
2. 💻 Account Username
3. 🔑 Account Password
4. 🕰️  Age
5. ♂️ ♀️ Gender
6. 📱 Phone Number
7. 📧 Email
8. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        modify = input("Enter selection: ").lower()
        if modify.isdigit(): #if modify consists of all digits
            modify = int(modify)
        try:
            if modify in [1, "employee name", "1. employee name"]:
                data = "name"
            elif modify in [2, "account username", "2. account username"]:
                data = "username"
            elif modify in [3, "account password", "3. account password"]:
                data = "password"
            elif modify in [4, "age", "4. age"]:
                data = "age"
            elif modify in [5, "gender", "5. gender"]:
                data = "gender"
            elif modify in [6, "phone number", "6. phone number"]:
                data = "phone number"
            elif modify in [7, "email", "7. email"]:
                data = "email"
            elif modify in [8, "back", "8. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
        os.system('cls')
        print(f"Update Employee {data.title()}".center(40, "-"))
        showID = input("Enter <YES> to display all Employee IDs: ").lower() #allow user to choose to view all employee IDs
        rFunctions.clearPreviousLine()
        if showID == "yes": #display all employee IDs in table
            print("Cashier:\n" + rFunctions.tabulateCsvData("cashier", ["id", "name", "username"], tbfmt = "simple_grid"))
            print("\nBaker:\n" + rFunctions.tabulateCsvData("baker", ["id", "name", "username"], tbfmt = "simple_grid") + "\n")
        if not rFunctions.askContinue():
            break
        while True: #infinite while loop, prompt employee ID
            try:
                rFunctions.clearPreviousLine()
                id = input("Enter Employee ID: ").upper()
                if rFunctions.checkUniqueData("cashier", "id", id, cashiersDict): #check if employee ID in cashier dictionary
                    role = "cashier"
                    break
                elif rFunctions.checkUniqueData("baker", "id", id, bakersDict): #check if employee ID in baker dictionary
                    role = "baker"
                    break
                else: #employee ID not found
                    raise ValueError(f"Invalid Input ☹️ : Employee ID '{id}' does not exists")
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
        print("\n" + "Employee Information".center(40, "-"))
        if role == "cashier":
            for cashier in cashiersDict["cashiers"]: #find specific cashier based on employee ID
                if cashier["id"] == id:
                    print(f"""Role: Cashier
ID: {cashier["id"]}
Name: {cashier["name"]}
Username: {cashier["username"]}
Password: {cashier["password"]}
Age: {cashier["age"]}
Gender: {cashier["gender"]}
Phone Number: {cashier["phone number"]}
Email: {cashier["email"]}\n{"-"*40}""")
                    while True: #infinite while loop, modify employee data
                        try:
                            if data == "name": #modify employee name
                                newCashierName = input("Enter New Employee Name: ")
                                cashier["name"] = newCashierName
                            elif data == "username": #modify employee username
                                newCashierUsername = input("Enter New Employee Username: ")
                                if rFunctions.checkUniqueData("cashier", "username", newCashierUsername, cashiersDict) or rFunctions.checkUniqueData("baker", "username", newCashierUsername, bakersDict):
                                    raise ValueError(f"Invalid input ☹️ : Employee Username '{newCashierUsername}' already existed")
                                errorMsg, validUsername = rFunctions.validData(username = newCashierUsername) #check validity of username
                                if not validUsername:
                                    raise ValueError(f"Invalid input ☹️ : {errorMsg}")
                                cashier["username"] = newCashierUsername
                            elif data == "password": #modify emplyee password
                                newCashierPassword = input("Enter New Employee Password: ")
                                errorMsg, validPassword = rFunctions.validData(password = newCashierPassword) #check validity of password
                                if not validPassword:
                                    raise ValueError(f"Invalid input ☹️ : {errorMsg}")
                                cashier["password"] = newCashierPassword
                            elif data == "age": #modify employee age
                                newCashierAge = int(input("Enter New Employee Age: "))
                                if newCashierAge <= 15: #check whether employee age > 15
                                    raise ValueError(f"Invalid employee age ☹️ : Employee age cannot be younger than 15 years old.")
                                cashier["age"] = newCashierAge
                            elif data == "gender": #modify employee gender
                                newCashierGender = input("Enter New Employee Gender: ").capitalize()
                                errorMsg, validGender = rFunctions.validData(gender = newCashierGender) #check validity of gender
                                if not validGender:
                                    raise ValueError(f"Invalid employee gender ☹️ : {errorMsg}")
                            elif data == "phone number": #modify employee phone number
                                newCashierPhoneNum = input("Enter New Employee Phone Number (01X-XXX XXXX): ")
                                errorMsg, validPhoneNum = rFunctions.validData(phoneNumber = newCashierPhoneNum) #check validity of phone number
                                if not validPhoneNum:
                                    raise ValueError(f"Invalid employee phone number ☹️ : {errorMsg}")
                            elif data == "email": #modify employee email
                                newCashierEmail = input("Enter New Employee Email: ")
                                errorMsg, validEmail = rFunctions.validData(email = newCashierEmail) #check validity of email
                                if not validEmail:
                                    raise ValueError(f"Invalid employee email ☹️ : {errorMsg}")
                            break #break while loop, done modify employee data
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine() #while loop continues, prompt valid new employee data
            rFunctions.writeFile("cashier", cashiersDict)
            time.sleep(2)
            print(f"{rFunctions.color('green', 'foreground')}Employee Name for '{id}' has been updated successfully 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
        elif role == "baker":
            for baker in bakersDict["bakers"]: #find specific baker based on employee ID
                if baker["id"] == id:
                    print(f"""Role: Baker
ID: {baker["id"]}
Name: {baker["name"]}
Username: {baker["username"]}
Password: {baker["password"]}
Age: {baker["age"]}
Gender: {baker["gender"]}
Phone Number: {baker["phone number"]}
Email: {baker["email"]}\n{"-"*40}""")
                    while True: #infinite while loop, modify employee data
                        try:
                            if data == "name": #modify employee name
                                newBakerName = input("Enter New Employee Name: ")
                                baker["name"] = newBakerName
                            elif data == "username": #modify employee username
                                newBakerUsername = input("Enter New Employee Username: ")
                                if rFunctions.checkUniqueData("cashier", "username", newBakerUsername, cashiersDict) or rFunctions.checkUniqueData("baker", "username", newBakerUsername, bakersDict):
                                    raise ValueError(f"Invalid input ☹️ : Employee Username '{newBakerUsername}' already existed")
                                errorMsg, validUsername = rFunctions.validData(username = newBakerUsername) #check validity of username
                                if not validUsername:
                                    raise ValueError(f"Invalid input ☹️ : {errorMsg}")
                                baker["username"] = newBakerUsername
                            elif data == "password": #modify employee password
                                newBakerPassword = input("Enter New Employee Password: ")
                                errorMsg, validPassword = rFunctions.validData(password = newBakerPassword) #check validity of password
                                if not validPassword:
                                    raise ValueError(f"Invalid input ☹️ : {errorMsg}")
                                baker["password"] = newBakerPassword
                            elif data == "age": #modify employee age
                                newBakerAge = int(input("Enter New Employee Age: "))
                                if newBakerAge <= 15: #check whether employee age > 15
                                    raise ValueError(f"Invalid employee age ☹️ : Employee age cannot be younger than 15 years old.")
                                baker["age"] = newBakerAge
                            elif data == "gender": #modify employee gender
                                newBakerGender = input("Enter New Employee Gender: ")
                                errorMsg, validGender = rFunctions.validData(gender = newBakerGender) #check validity of gender
                                if not validGender:
                                    raise ValueError(f"Invalid employee gender ☹️ : {errorMsg}")
                                baker["gender"] = newBakerGender
                            elif data == "phone number": #modify employee phone number
                                newBakerPhoneNum = input("Enter New Employee Phone Number (01X-XXX XXXX): ")
                                errorMsg, validPhoneNum = rFunctions.validData(phoneNumber = newCashierPhoneNum) #check validity of phone number
                                if not validPhoneNum:
                                    raise ValueError(f"Invalid employee phone number ☹️ : {errorMsg}")
                                baker["phone number"] = newBakerPhoneNum
                            elif data == "email": #modify employee email
                                newBakerEmail = input("Enter New Employee Email: ")
                                errorMsg, validEmail = rFunctions.validData(email = newBakerEmail) #check validity of email
                                if not validEmail:
                                    raise ValueError(f"Invalid employee email ☹️ : {errorMsg}")
                                baker["email"] = newBakerEmail
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine() #while loop continues, prompt valid new employee data
            rFunctions.writeFile("baker", bakersDict)
            time.sleep(2)
            print(f"{rFunctions.color('green', 'foreground')}Employee Name for '{id}' has been updated successfully 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
        break

def deleteEmployee():
    while True:
        cashiersDict = rFunctions.readFile("cashier") #read cashiers data
        bakersDict = rFunctions.readFile("baker") #read bakers data
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Employee Account Deletion".center(40)}
{"-"*40}{rFunctions.color('reset', None)}""")
        showID = input("Enter <YES> to display all Employee IDs: ")
        rFunctions.clearPreviousLine()
        if showID == "yes": #display all employee IDs in table
            print("Cashier:\n" + rFunctions.tabulateCsvData("cashier", ["id", "name", "username"], tbfmt = "simple_grid"))
            print("\nBaker:\n" + rFunctions.tabulateCsvData("baker", ["id", "name", "username"], tbfmt = "simple_grid") + "\n")
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        while True: #infinite while loop, prompt employee ID to delete
            try:
                delEmployeeId = input("Enter Employee ID to delete: ").upper()
                if rFunctions.checkUniqueData("cashier", "id", delEmployeeId, cashiersDict):
                    print("\n" + "Employee Information".center(40, "-"))
                    for i, cashier in enumerate(cashiersDict["cashiers"]):
                        if cashier["id"] == delEmployeeId:
                            print(f"""Role: Cashier
ID: {cashier["id"]}
Name: {cashier["name"]}
Username: {cashier["username"]}
Passowrd: {cashier["password"]}
Age: {cashier["age"]}
Gender: {cashier["gender"]}
Phone Number: {cashier["phone number"]}
Email: {cashier["email"]}\n{"-"*40}""")
                            indexOfCashier = i
                    confirm = input("Enter <CONFIRM> to delete: ").lower() #confirm cashier account deletion
                    rFunctions.clearPreviousLine()
                    if confirm == "confirm":
                        del cashiersDict["cashiers"][indexOfCashier]
                        rFunctions.writeFile("cashier", cashiersDict)
                        cashiersDict = rFunctions.readFile("cashier") #still need if already read at the start of the function?
                        time.sleep(2)
                        print(f"{rFunctions.color('green', 'foreground')}Employee '{delEmployeeId}' has been deleted successfully 😄{rFunctions.color('reset', None)}")
                        time.sleep(2)
                    else:
                        print(f"{rFunctions.color('red', 'foreground')}Employee '{delEmployeeId}' has not been deleted ☹️{rFunctions.color('reset', None)}")
                        time.sleep(2)
                elif rFunctions.checkUniqueData("baker", "id", delEmployeeId, bakersDict):
                    print("\n" + "Employee Information".center(40, "-"))
                    for i, baker in enumerate(bakersDict["bakers"]):
                        if baker["id"] == delEmployeeId:
                            print(f"""Role: Baker
ID: {baker["id"]}
Name: {baker["name"]}
Username: {baker["username"]}
Password: {baker["password"]}
Age: {baker["age"]}
Gender: {baker["gender"]}
Phone Number: {baker["phone number"]}
Email: {baker["email"]}\n{"-"*40}""")
                            indexOfBaker = i
                    confirm = input("Enter <CONFIRM> to delete: ").lower() #confirm baker account deletion
                    rFunctions.clearPreviousLine()
                    if confirm == "confirm":
                        del bakersDict["bakers"][indexOfBaker]
                        rFunctions.writeFile("baker", bakersDict)
                        bakersDict = rFunctions.readFile("baker") #still need if already read at the start of the function?
                        time.sleep(0.5)
                        print(f"{rFunctions.color('green', 'foreground')}Employee '{delEmployeeId}' has been deleted successfully 😄{rFunctions.color('reset', None)}")
                        time.sleep(2)
                    else:
                        print(f"{rFunctions.color('red', 'foreground')}Employee '{delEmployeeId}' has not been deleted ☹️{rFunctions.color('reset', None)}")
                        time.sleep(2)
                else:
                    raise ValueError(f"Invalid Input ☹️ : Employee ID '{delEmployeeId}' does not exists")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        if not rFunctions.askContinue():
            break

#(ii) Customer Management
def customerManagement():
    while True:
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Customer Management".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🔐 Create New Account
2. 📝 Update Account
3. 🗑️  Delete Account
4. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        try:
            operation = input("Enter selection: ").lower()
            if operation.isdigit():
                operation = int(operation)
            if operation in [1, "create new account", "1. create new account"]:
                addCustomer()
            elif operation in [2, "update account", "2. update account"]:
                modifyCustomer()
            elif operation in [3, "delete account", "3. delete account"]:
                deleteCustomer()
            elif operation in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def addCustomer():
    while True:
        customersDict = rFunctions.readFile("customer")
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"New Customer Registration".center(40)}
{"-"*40}{rFunctions.color('reset', None)}""")
        try:
            id = rFunctions.assignId("customer", customersDict)
            name = input("Enter Customer's Name: ")
            username = input("Enter Customer's Username: ")
            if rFunctions.checkUniqueData("customer", "username", username, customersDict):
                raise ValueError(f"Invalid customer username ☹️ : Username {username} already existed")
            errorMsg, validUsername = rFunctions.validData(username = username)
            if not validUsername:
                raise ValueError(f"Invalid customer username ☹️ : {errorMsg}")
            password = input("Enter Password: ")
            errorMsg, validPassword = rFunctions.validData(password = password)
            if not validPassword:
                raise ValueError(f"Invalid customer password ☹️ : {errorMsg}")
            age = int(input("Enter Customer's Age: "))
            if age <= 0 :
                raise ValueError(f"Invalid customer age ☹️ : Customer age cannot be 0 years old or negative.{errorMsg}")
            gender = input("Enter Customer's Gender: ").capitalize()
            errorMsg, validGender = rFunctions.validData(gender = gender)
            if not validGender:
                raise ValueError(f"Invalid employee gender ☹️ : {errorMsg}")
            phoneNum = input("Enter Customer's Phone Number (01X-XXX XXXX): ")
            errorMsg, validPhoneNum = rFunctions.validData(phoneNumber = phoneNum)
            if not validPhoneNum:
                raise ValueError(f"Invalid employee phone number ☹️ : {errorMsg}")
            email = input("Enter Customer's Email: ")
            errorMsg, validEmail = rFunctions.validData(email = email)
            if not validEmail:
                raise ValueError(f"Invalid employee email ☹️ : {errorMsg}")
            address = input("Enter Customer's Address: ")
            newCustomer = {"id": id, "name": name, "username": username, "password": password, "age": age, "gender": gender, "phone number": phoneNum, "email": email, "address": address}
            rFunctions.appendFile("customer", customersDict, newCustomer)
            customersDict = rFunctions.readFile("customer")
            print(f"\n{rFunctions.color('green', 'foreground')}New customer '{name}' is added 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            print(f"\n{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break

def modifyCustomer():
    while True:
        customersDict = rFunctions.readFile("customer")
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Customer Account Update".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🪪  Customer Name
2. 💻 Account Username
3. 🔑 Account Password
4. 🕰️  Age
5. ♂️ ♀️ Gender
6. 📱 Phone Number
7. 📧 Email
8. 🏠 Address
9. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        modify = input("Enter selection: ").lower()
        if modify.isdigit():
            modify = int(modify)
        try:
            if modify in [1, "employee name", "1. employee name"]:
                data = "name"
            elif modify in [2, "account username", "2. account username"]:
                data = "username"
            elif modify in [3, "account password", "3. account password"]:
                data = "password"
            elif modify in [4, "age", "4. age"]:
                data = "age"
            elif modify in [5, "gender", "5. gender"]:
                data = "gender"
            elif modify in [6, "phone number", "6. phone number"]:
                data = "phone number"
            elif modify in [7, "email", "7. email"]:
                data = "email"
            elif modify in [8, "address", "8. address"]:
                data = "address"
            elif modify in [9, "back", "9. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
            os.system('cls')
            print(f"Update Customer {data.title()}".center(40, "-"))
            showID = input("Enter <YES> to display all Customer ID: ").lower()
            rFunctions.clearPreviousLine()
            if showID == "yes":
                print("Customers:")
                print(rFunctions.tabulateCsvData("customer", ["id", "name", "username"], tbfmt = "simple_grid") + "\n")
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            while True:
                customersDict = rFunctions.readFile("customer")
                try:
                    id = input("Enter Customer ID: ").upper()
                    if not rFunctions.checkUniqueData("customer", "id", id, customersDict):
                        raise ValueError(f"Invalid Input ☹️ : Customer ID '{id}' does not exists")
                    print("\n" + "Customer Information".center(40, "-"))
                    for customer in customersDict["customers"]:
                        if customer["id"] == id:
                            print(f"""ID: {customer["id"]}
Name: {customer["name"]}
Username: {customer["username"]}
Passowrd: {customer["password"]}
Age: {customer["age"]}
Gender: {customer["gender"]}
Phone Number: {customer["phone number"]}
Email: {customer["email"]}
Address: {customer["address"]}
{"-"*40}""")
                            while True:
                                try:
                                    if data == "name":
                                        newCustomerName = input("Enter New Customer Name: ")
                                        customer["name"] = newCustomerName
                                    elif data == "username":
                                        newCustomerUsername = input("Enter New Customer Username: ")
                                        if rFunctions.checkUniqueData("customer", "username", newCustomerUsername, customersDict):
                                            raise ValueError(f"Invalid input ☹️ : Customer Username '{newCustomerUsername}' already existed")
                                        errorMsg, validUsername = rFunctions.validData(username = newCustomerUsername)
                                        if not validUsername:
                                            raise ValueError(f"Invalid input ☹️ : {errorMsg}")
                                        customer["username"] = newCustomerUsername
                                    elif data == "password":
                                        newCustomerPassword = input("Enter New Customer Password: ")
                                        errorMsg, validPassword = rFunctions.validData(password = newCustomerPassword)
                                        if not validPassword:
                                            raise ValueError(f"Invalid input ☹️ : {errorMsg}")
                                        customer["password"] = newCustomerPassword
                                    elif data == "age":
                                        newCustomerAge = int(input("Enter New Customer Age: "))
                                        if newCustomerAge <= 15:
                                            raise ValueError(f"Invalid customer age ☹️ : Customer age cannot be 0 years old or negative.")
                                        customer["age"] = newCustomerAge
                                    elif data == "gender":
                                        newCustomerGender = input("Enter New Customer Gender: ")
                                        errorMsg, validGender = rFunctions.validData(gender = newCustomerGender)
                                        if not validGender:
                                            raise ValueError(f"Invalid customer gender ☹️ : {errorMsg}")
                                        customer["gender"] = newCustomerGender
                                    elif data == "phone number":
                                        newCustomerPhoneNum = input("Enter New Customer Phone Number (01X-XXX XXXX): ")
                                        errorMsg, validPhoneNum = rFunctions.validData(phoneNumber = newCustomerPhoneNum)
                                        if not validPhoneNum:
                                            raise ValueError(f"Invalid customer phone number ☹️ : {errorMsg}")
                                        customer["phone number"] = newCustomerPhoneNum
                                    elif data == "email":
                                        newCustomerEmail = input("Enter New Customer Email: ")
                                        errorMsg, validEmail = rFunctions.validData(email = newCustomerEmail)
                                        if not validEmail:
                                            raise ValueError(f"Invalid customer email ☹️ : {errorMsg}")
                                        customer["email"] = newCustomerEmail
                                    elif data == "address":
                                        newCustomerAddress = input("Enter New Customer Address: ")
                                        customer["address"] = newCustomerAddress
                                    break
                                except ValueError as vE:
                                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                                    time.sleep(2)
                                    rFunctions.clearPreviousLine()
                                    rFunctions.clearPreviousLine()
                    rFunctions.writeFile("customer", customersDict)
                    time.sleep(2)
                    print(f"{rFunctions.color('green', 'foreground')}Customer {data.title()} for '{id}' has been updated successfully 😄{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break

def deleteCustomer():
    while True:
        customersDict = rFunctions.readFile("customer")
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Customer Account Deletion".center(40) }
{"-"*40}{rFunctions.color('reset', None)}""")
        showID = input("Enter <YES> to display all Customer ID: ").lower()
        rFunctions.clearPreviousLine()
        if showID == "yes":
            print("Customer IDs".center(40, "-"))
            print(rFunctions.tabulateCsvData("customer", ["id", "name", "username"], tbfmt = "simple_grid") + "\n")
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        while True:
            try:
                delCustomerId = input("Enter Customer ID to delete: ").upper()
                if not rFunctions.checkUniqueData("customer", "id", delCustomerId, customersDict):
                    raise ValueError(f"Invalid Input ☹️ : Customer ID '{delCustomerId}' does not exists")
                print("\n" + "Customer Information".center(40, "-"))
                for i, customer in enumerate(customersDict["customers"]):
                    if customer["id"] == delCustomerId:
                        print(f"""ID: {customer["id"]}
Name: {customer["name"]}
Username: {customer["username"]}
Passowrd: {customer["password"]}
Age: {customer["age"]}
Gender: {customer["gender"]}
Phone Number: {customer["phone number"]}
Email: {customer["email"]}
Address: {customer["address"]}
{"-"*40}""")
                        indexOfCustomer = i
                confirm = input("Enter <CONFIRM> to delete: ").lower()
                rFunctions.clearPreviousLine()
                if confirm == "confirm":
                    del customersDict["customers"][indexOfCustomer]
                    rFunctions.writeFile("customer", customersDict)
                    customersDict = rFunctions.readFile("customer")
                    time.sleep(0.5)
                    print(f"{rFunctions.color('green', 'foreground')}Employee '{delCustomerId}' has been deleted successfully 😄{rFunctions.color('reset', None)}")
                    time.sleep(2)
                else:
                    print(f"{rFunctions.color('red', 'foreground')}Employee '{delCustomerId}' has not been deleted ☹️{rFunctions.color('reset', None)}")
                    time.sleep(2)
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        if not rFunctions.askContinue():
            break

# Functionality 02: Order Management
def orderManagement():
    while True:
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Order Management".center(40) }
{"-"*40}{rFunctions.color('reset', None)}
1. 🗒️  View Order Details
2. ⏰ Update Order Status
3. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit(): #if functiionality consists of all digits
                functionality = int(functionality)
            if functionality in [1, "view order details", "1. view order details"]:
                viewOrderDetails()
            elif functionality in [2, "update order status", "2. update order status"]:
                updateOrderStatus()
            elif functionality in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️") #invalid input, trigger exception handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2) #loop continue

def viewOrderDetails(orderId: str = ""):
    if orderId != '':
        ordersDict = rFunctions.readFile("order")
        customersDict = rFunctions.readFile("customer")
        print(rFunctions.color('bold', None) + "="*40 + "\n" + f"Order Details for {orderId}".center(40) + "\n" + "="*40 + rFunctions.color('reset', None))
        for order in ordersDict["orders"]:
            if order["orderID"] == orderId:
                orderDate = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date()
                orderTime = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").time()
                for customer in customersDict["customers"]:
                    if customer["id"] == order["userID"]:
                        customerUsername = customer["username"]
                productList, totalOrder = [], 0
                for product in eval(order["products"]):
                    productList.append([product[0], product[1], product[2], f"RM {product[3]:.2f}", f"RM {product[4]:.2f}"])
                    totalOrder += 1
                if order["completionStatus"] == "completed":
                    status = f"{rFunctions.color('green', 'foreground')}{order["completionStatus"].capitalize()}{rFunctions.color('reset', None)}"
                else:
                    status = f"{rFunctions.color('yellow', 'foreground')}{order["completionStatus"].capitalize()}{rFunctions.color('reset', None)}"
                print(f"""\nCustomer Username: {customerUsername}\n\nOrder Date: {orderDate}\n\nProcessed Time: {orderTime}\n
{rFunctions.tabulateGivenData(["Product ID", "Product Name", "Quantity", "Price", "Total Price"], productList, tbfmt = "outline")}\n
{"-"*40}\nTotal Order: {totalOrder}\n{"-"*40}\n\nOrder Status: {status}\n""")
    else:
        while True:
            try:
                ordersDict = rFunctions.readFile("order")
                customersDict = rFunctions.readFile("customer")
                print("\033c" + "View Order Details".center(40, "-") + "\nList of Months with Orders:")
                yearMonth = []
                for order in ordersDict["orders"]:
                    orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date().month
                    orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date().year
                    orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
                    yearMonth.append([orderYear, orderMonth]) if [orderYear, orderMonth] not in yearMonth else yearMonth
                print(rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
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
                    print(rFunctions.tabulateGivenData(["Order ID", "Customer ID", "Customer Username", "Order Date"], orderList, tbfmt = "simple_grid") + "\n")
                    if not rFunctions.askContinue():
                        break
                    rFunctions.clearPreviousLine()
                    while True:
                        try:
                            orderId = input("Enter Order ID: ").upper()
                            if orderId not in orderIds:
                                raise ValueError(f"Invalid input ☹️ : Order ID {orderId} is not found.")
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine()
                    print("\033c" + rFunctions.color('bold', None) + "="*40 + "\n" + f"Order Details for {orderId}".center(40) + "\n" + "="*40 + rFunctions.color('reset', None))
                    for order in ordersDict["orders"]:
                        if order["orderID"] == orderId:
                            orderDate = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date()
                            orderTime = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").time()
                            for customer in customersDict["customers"]:
                                if customer["id"] == order["userID"]:
                                    customerUsername = customer["username"]
                            productList, totalOrder = [], 0
                            for product in eval(order["products"]):
                                productList.append([product[0], product[1], product[2], f"RM {product[3]:.2f}", f"RM {product[4]:.2f}"])
                                totalOrder += 1
                            if order["completionStatus"] == "completed":
                                status = f"{rFunctions.color('green', 'foreground')}{order["completionStatus"].capitalize()}{rFunctions.color('reset', None)}"
                            else:
                                status = f"{rFunctions.color('yellow', 'foreground')}{order["completionStatus"].capitalize()}{rFunctions.color('reset', None)}"
                            print(f"""\nCustomer Username: {customerUsername}\n\nOrder Date: {orderDate}\n\nProcessed Time: {orderTime}\n
{rFunctions.tabulateGivenData(["Product ID", "Product Name", "Quantity", "Price", "Total Price"], productList, tbfmt = "outline")}\n
{"-"*40}\nTotal Order: {totalOrder}\n{"-"*40}\n\nOrder Status: {status}\n""")
                    time.sleep(2)
                    if not rFunctions.askContinue():
                        break
                elif not valid:
                    continue
                elif [year, month] not in yearMonth:
                    raise ValueError(f"Invalid input ☹️ : No records for order in {month} {year}")
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)

def updateOrderStatus():
    while True:
        ordersDict = rFunctions.readFile("order")
        customersDict = rFunctions.readFile("customer")
        productsDict = rFunctions.readFile("product")
        print("\033c" + "Update Order Status".center(40, "-") + "\nList of Pending Orders:")
        orderList, orderIds = [], []
        for order in ordersDict["orders"]:
            if order["completionStatus"] == "pending":
                date = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").date()
                for customer in customersDict["customers"]:
                    if customer["id"] == order["userID"]:
                        customerUsername = customer["username"]
                orderList.append([order["orderID"], customerUsername, date])
                orderIds.append(order["orderID"])
        print(rFunctions.tabulateGivenData(["Order ID", "Customer Username", "Order Date"], orderList, tbfmt = "simple_grid") + "\n")
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        while True:
            try:
                orderId = input("Enter Order ID: ").upper()
                if orderId not in orderIds:
                    raise ValueError(f"Invalid input ☹️ : Order ID {orderId} is completed or not found.")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        print("\033c" + "Update Order Status".center(40, "-") + "\n")
        viewOrderDetails(orderId)
        updateStatus = input("Enter <COMPLETED> to update the order status: ").lower()
        rFunctions.clearPreviousLine()
        if updateStatus == "completed":
            for order in ordersDict["orders"]:
                if order["orderID"] == orderId:
                    order["completionStatus"] = "completed"
            rFunctions.writeFile("order", ordersDict)
            for order in ordersDict["orders"]:
                if order["orderID"] == orderId:
                    productList = eval(order["products"])
                    for item in productList:
                        for product in productsDict["products"]:
                            #to update the product quantity after order is completed
                            if product["id"] == item[0]:
                                product["quantity"] = int(product["quantity"]) - int(item[2])
                                break
            rFunctions.writeFile("product", productsDict)
            print(f"{rFunctions.color('green', 'foreground')}Completion status for '{orderId}' is successfully updated 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
            print("\033c" + "Update Order Status".center(40, "-") + "\n")
            viewOrderDetails(orderId)
            print()
        else:
            print(f"{rFunctions.color('red', 'foreground')}Completion status for '{orderId}' is not updated ☹️{rFunctions.color('reset', None)}")
            time.sleep(2)
        rFunctions.clearPreviousLine()
        if not rFunctions.askContinue():
            break

# Functionality 03: Financial Management
def financialManagement(): #clear terminal
    while True:
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Financial Management".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🖋️  Budgeting and Cost Control
2. 📊 Financial Reporting
3. 🪙  Tax Management
4. 🛠️  Payroll Management
5. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit(): #if functionality consists of all digits
                functionality = int(functionality)
            if functionality in [1, "budgeting and cost control", "budgeting", "cost control", "1. budgeting and cost control", "1. budgeting", "1. cost control"]:
                budgetingCostCtrl()
            elif functionality in [2, "financial reporting", "2. financial reporting"]:
                financialReporting()
            elif functionality in [3, "tax management", "3. tax management"]:
                taxManagement()
            elif functionality in [4, "payroll management", "4. payroll management"]:
                payrollManagement()
            elif functionality in [5, "back", "5. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️") #invalid input, trigger error handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2) #loop continues

#(i) Budgeting and cost control
def budgetingCostCtrl():
    while True:
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"Budgeting and Cost Control".center(40, "-")}{rFunctions.color('reset', None)}
1. 🎯 Projected Income
2. 📈 Projected Net Profit
3. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        operation = input("Enter selection: ")
        try:
            if operation.isdigit():
                operation = int(operation)
            if operation in [1, "projected income", "1. projected income"]:
                projectedIncome()
            elif operation in [2, "projected net profit", "2. projected net profit"]:
                netProfit()
            elif operation in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid Input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def projectedIncome(all: bool = False, year: str = "", month: str = "", yearMonth: list = [], valid: bool = False):
    while True:
        try:
            projInDict = rFunctions.readFile("projected income")
            if all:
                totalRevenue = 0.00
                for data in projInDict["projected incomes"]:
                    if data["month"] == month and data["year"] == year:
                        totalRevenue += rFunctions.extractNumber(data["revenue"])
                print(f"""{rFunctions.color('underline', None)}Projected Income Summary for {month} {year}{rFunctions.color('reset', None)}
Total Projected Revenue: RM {totalRevenue:.2f}\n""")
                return totalRevenue
            else:
                os.system('cls')
                print(f"""{rFunctions.color('bold', None)}{"Projected Income".center(40, "-")}{rFunctions.color('reset', None)}
1. 📑 Display
2. ➕ Add
3. 🔧 Modify
4. 🗑️  Delete
5. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
                operation = input("Enter selection: ").lower()
                if operation.isdigit():
                    operation = int(operation)
                if operation in [1, "display", "1. display"]:
                    displayProjectedIncome()
                elif operation in [2, "add", "2. add"]:
                    addProjectedIncome()
                elif operation in [3, "modify", "3. modify"]:
                    modifyProjectedIncome()
                elif operation in [4, "delete", "4. delete"]:
                    deleteProjectedIncome()
                elif operation in [5, "exit", "5. exit"]:
                    break
                else:
                    raise ValueError("Invalid Input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def displayProjectedIncome():
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            projInDict = rFunctions.readFile("projected income")
            os.system('cls')
            print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Display Projected Income".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
            yearMonth = []
            print("List of Projected Income Available:")
            for data in projInDict["projected incomes"]:
                if [data["year"], data["month"]] not in yearMonth:
                    yearMonth.append([data["year"], data["month"]])
            print(rFunctions.tabulateGivenData(header = ["Year", "Month"], data = yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            if valid and [year, month] in yearMonth:
                rFunctions.clearPreviousLine()
                print("\033c" + f"Projected income in {month} {year}".center(40, "-"))
                categories = []
                for data in productsDict["products"]:
                    if data["category"] not in categories:
                        categories.append(data["category"])
                for category in categories:
                    dataList = []
                    for data in projInDict["projected incomes"]:
                        if data["year"] == year and data["month"] == month and data["category"] == category:
                            dataList.append([data["id"], data["name"], data["selling price"], data["forecast sales volume"], data["revenue"]])
                    print(f"{category}:")
                    print(rFunctions.tabulateGivenData(["ID", "Name", "Selling Price", "Forecast Sales Volume", "Revenue"], dataList, tbfmt = "simple_grid") + "\n")
                totalRevenue = 0.00
                for data in projInDict["projected incomes"]:
                    if data["month"] == month and data["year"] == year:
                        totalRevenue += rFunctions.extractNumber(data["revenue"])
                print(f"Total Projected Revenue for {month} {year}: RM %.2f"%(totalRevenue) + "\n")
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for projected income in {month} {year}")
            time.sleep(2)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def addProjectedIncome():
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            projInDict = rFunctions.readFile("projected income")
            os.system('cls')
            print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + "Add Projected Income".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
            monthYears = []
            for data in projInDict["projected incomes"]:
                monthYears.append({"year": data["year"], "month": datetime.strptime(data["month"], "%B").month})
            for i, data in enumerate(monthYears):
                if i == 0:
                    recentYear = data["year"]
                else:
                    recentYear = data["year"] if data["year"] > recentYear else recentYear
            lastMonthInt = None
            for data in monthYears:
                if data["year"] == recentYear:
                    if lastMonthInt == None:
                        lastMonthInt = data["month"]
                    else:
                        lastMonthInt = data["month"] if data["month"] > lastMonthInt else lastMonthInt
            lastMonth, year, _ = rFunctions.validMonthYear(lastMonthInt, recentYear)
            viewPrev = input(f"Enter <YES> to view {lastMonth} {year}'s Projected Income: ")
            if viewPrev == "yes":
                os.system('cls')
                print(f"Projected Income in {lastMonth}".center(40, "-"))
                categories = []
                for data in productsDict["products"]:
                    if data["category"] not in categories:
                        categories.append(data["category"])
                for category in categories:
                    dataList = []
                    for data in projInDict["projected incomes"]:
                        if data["year"] == year and data["month"] == lastMonth and data["category"] == category:
                            dataList.append([data["id"], data["name"], data["selling price"], data["forecast sales volume"], data["revenue"]])
                    print(f"{category}:")
                    print(rFunctions.tabulateGivenData(["ID", "Name", "Selling Price", "Forecast Sales Volume", "Revenue"], dataList, tbfmt = "simple_grid") + "\n")
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            nextMonthInt = 1 if lastMonthInt == 12 else lastMonthInt + 1
            recentYear = str(int(recentYear) +  1) if nextMonthInt == 1 else recentYear
            nextMonth = datetime(datetime.now().year, nextMonthInt, 1).strftime('%B').capitalize()
            print(f"""\n{f"Add Projected Income for {nextMonth} {recentYear}".center(40, "-")}
{rFunctions.color('underline', None)}Insert Forecast Sales Volume:{rFunctions.color('reset', None)}""")
            oldProjInDict = projInDict
            categories = []
            for data in productsDict["products"]:
                if data["category"] not in categories:
                    categories.append(data["category"])
            for category in categories:
                print(f"{category}:")
                for product in productsDict["products"]:
                    if product["category"] == category:
                        forecastSalesVol = int(input(f"{product["name"]} [Selling Price: {product["price"]}]: "))
                        newProjInDict = {"year": recentYear,
                        "month": nextMonth,
                        "id": product["id"],
                        "category": category,
                        "name": product["name"],
                        "selling price": product["price"],
                        "forecast sales volume": forecastSalesVol,
                        "revenue": f"RM%.2f"%(rFunctions.extractNumber(product["price"])*forecastSalesVol)}
                        rFunctions.appendFile("projected income", projInDict, newProjInDict)
                print()
            os.system('cls')
            print(f"Projected Income for {nextMonth} {recentYear}".center(40, "-"))
            projInDict = rFunctions.readFile("projected income")
            for category in categories:
                dataList = []
                for data in projInDict["projected incomes"]:
                    if data["month"] == nextMonth and data["year"] == recentYear and data["category"] == category:
                        dataList.append([data["id"], data["name"], data["selling price"], data["forecast sales volume"], data["revenue"]])
                print(f"{category}:")
                print(rFunctions.tabulateGivenData(["ID", "Name", "Selling Price", "Forecast Sales Volume", "Revenue"], dataList, tbfmt = "simple_grid") + "\n")
            confirm = input("Enter <CONFIRM> to Save Project Income: ").lower()
            if confirm != "confirm":
                rFunctions.writeFile("projected income", oldProjInDict)
                rFunctions.clearPreviousLine()
                print(f"{rFunctions.color('red', 'foreground')}Projected Income for {nextMonth} {datetime.now().year} is not saved ☹️{rFunctions.color('reset', None)}")
            else:
                rFunctions.clearPreviousLine()
                print(f"{rFunctions.color('green', 'foreground')}Projected Income for {nextMonth} {datetime.now().year} is successfully saved 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            rFunctions.writeFile("projected income", oldProjInDict)
            print(f"\n{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break

def modifyProjectedIncome():
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            projInDict = rFunctions.readFile("projected income")
            os.system('cls')
            print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Update Projected Income".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
            yearMonth = []
            print(f"{rFunctions.color('underline', None)}List of Projected Income Available:{rFunctions.color('reset', None)}")
            for data in projInDict["projected incomes"]:
                if [data["year"], data["month"]] not in yearMonth:
                    yearMonth.append([data["year"], data["month"]])
            print(rFunctions.tabulateGivenData(header = ["Year", "Month"], data = yearMonth, tbfmt = "simple_grid"))
            modifyMonth, modifyYear = input("Enter month and year to update: ").split()
            modifyMonth, modifyYear, valid = rFunctions.validMonthYear(modifyMonth, modifyYear)
            if valid and [modifyYear, modifyMonth] in yearMonth:
                while True:
                    try:
                        os.system('cls')
                        print(f"Projected Income in {modifyMonth} {modifyYear}".center(40, "-"))
                        categories = []
                        for data in productsDict["products"]:
                            if data["category"] not in categories:
                                categories.append(data["category"])
                        for category in categories:
                            dataList = []
                            for data in projInDict["projected incomes"]:
                                if data["year"] == modifyYear and data["month"] == modifyMonth and data["category"] == category:
                                    dataList.append([data["id"], data["name"], data["selling price"], data["forecast sales volume"], data["revenue"]])
                            print(f"{category}:")
                            print(rFunctions.tabulateGivenData(["ID", "Name", "Selling Price", "Forecast Sales Volume", "Revenue"], dataList, tbfmt = "simple_grid") + "\n")
                        totalRevenue = 0.00
                        for data in projInDict["projected incomes"]:
                            if data["month"] == modifyMonth and data["year"] == modifyYear:
                                totalRevenue += rFunctions.extractNumber(data["revenue"])
                        print(f"Total Projected Revenue for {modifyMonth} {modifyYear}: RM %.2f"%(totalRevenue) + "\n")
                        print("Insert Product ID".center(40, "-"))
                        productId = input("Enter Product ID to update or '-1' to exit: ").upper()
                        if productId != "-1":
                            if not rFunctions.checkUniqueData("product", "id", productId, productsDict):
                                raise ValueError(f"Invalid Input ☹️ : Product ID '{productId}' does not exists")
                            for data in projInDict["projected incomes"]:
                                if data["month"] == modifyMonth and data["year"] == modifyYear and data["id"] == productId:
                                    print("Insert Forecast Sales Volume".center(40, "-"))
                                    oldForecastSalesVol = data["forecast sales volume"]
                                    data["forecast sales volume"] = int(input("Enter forecast sales volume: "))
                                    if data["forecast sales volume"] < 0:
                                        data["forecast sales volume"] = oldForecastSalesVol
                                        raise ValueError(f"Invalid input ☹️ : forecast sales volume cannot be negative")
                                    data["revenue"] = f"RM %.2f"%(rFunctions.extractNumber(data["selling price"])*data["forecast sales volume"])
                                    time.sleep(2)
                                    print(f"{rFunctions.color('green', 'foreground')}Projected Income for {productId} in {modifyMonth} {modifyYear} is updated 😄{rFunctions.color('reset', None)}")
                                    time.sleep(2)
                            rFunctions.writeFile("projected income", projInDict)
                            projInDict = rFunctions.readFile("projected income")
                        else:
                            break
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                break
            elif not valid:
                continue
            elif [modifyYear, modifyMonth] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for projected income in {modifyMonth} {modifyYear}")
            time.sleep(2)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def deleteProjectedIncome():
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            projInDict = rFunctions.readFile("projected income")
            os.system('cls')
            print(f"{rFunctions.color('bold', None)}" + "-"*40 + "\n" + f"Delete Projected Income".center(40) + "\n" + "-"*40 + f"{rFunctions.color('reset', None)}")
            yearMonth = []
            print("List of Projected Income Available:")
            for data in projInDict["projected incomes"]:
                if [data["year"], data["month"]] not in yearMonth:
                    yearMonth.append([data["year"], data["month"]])
            print(rFunctions.tabulateGivenData(header = ["Year", "Month"], data = yearMonth, tbfmt = "simple_grid"))
            delMonth, delYear = input("Enter month and year to delete: ").split()
            delMonth, delYear, valid = rFunctions.validMonthYear(delMonth, delYear)
            if valid and [delYear, delMonth] in yearMonth:
                os.system('cls')
                print(f"Projected Income in {delMonth} {delYear}".center(40, "-"))
                categories = []
                for data in productsDict["products"]:
                    if data["category"] not in categories:
                        categories.append(data["category"])
                delIndex = []
                for category in categories:
                    dataList = []
                    for i, data in enumerate(projInDict["projected incomes"]):
                        if data["year"] == delYear and data["month"] == delMonth and data["category"] == category:
                            dataList.append([data["id"], data["name"], data["selling price"], data["forecast sales volume"], data["revenue"]])
                            delIndex.append(i)
                    print(f"{category}:")
                    print(rFunctions.tabulateGivenData(["ID", "Name", "Selling Price", "Forecast Sales Volume", "Revenue"], dataList, tbfmt = "simple_grid") + "\n")
                totalRevenue = 0.00
                for data in projInDict["projected incomes"]:
                    if data["month"] == delMonth and data["year"] == delYear:
                        totalRevenue += rFunctions.extractNumber(data["revenue"])
                print(f"Total Projected Revenue for {delMonth} {delYear}: RM %.2f"%(totalRevenue) + "\n")
                delIndex.sort(reverse = True)
                confirm = input("Enter <CONFIRM> to delete Projected Income: ").lower()
                if confirm == "confirm":
                    for indexNum in delIndex:
                        del projInDict["projected incomes"][indexNum]
                    rFunctions.writeFile("projected income", projInDict)
                    projInDict = rFunctions.readFile("projected income")
                    rFunctions.clearPreviousLine()
                    print(f"{rFunctions.color('green', 'foreground')}Projected Income for {delMonth} {delYear} is successfully deleted 😄{rFunctions.color('reset', None)}")
                else:
                    rFunctions.clearPreviousLine()
                    print(f"{rFunctions.color('red', 'foreground')}Projected Income for {delMonth} {delYear} is not deleted ☹️{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [delYear, delMonth] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for projected income in {delMonth} {delYear}")
            time.sleep(2)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)


def netProfit():
    while True:
        try:
            cogsDict = rFunctions.readFile("cogs")
            opExpDict = rFunctions.readFile("operating")
            payrollDict = rFunctions.readFile("payroll")
            taxesDict = rFunctions.readFile("taxe")
            loansDict = rFunctions.readFile("loan")
            print(f"""\033c{rFunctions.color('bold', None)}{"-"*40}
{"Net Profit".center(40) }
{"-"*40}{rFunctions.color('reset', None)}
List of available expenses for:""")
            dictsRole = ["cogs", "operating", "payroll", "taxe", "loan"]
            listofDicts = [cogsDict, opExpDict, payrollDict, taxesDict, loansDict]
            yearMonth, yearMonthInt = [], []
            for i, role in enumerate(dictsRole):
                for data in listofDicts[i][f"{role}s"]:
                    dataMonthInt = datetime.strptime(data["date"], "%Y-%m-%d").month
                    dataYearInt = datetime.strptime(data["date"], "%Y-%m-%d").year
                    dataMonth, dataYear, _ = rFunctions.validMonthYear(dataMonthInt, dataYearInt)
                    if [dataYear, dataMonth] not in yearMonth:
                        yearMonth.append([dataYear, dataMonth])
                        yearMonthInt.append([dataYearInt, dataMonthInt])
            for i, yearmonth in enumerate(yearMonthInt):
                if yearmonth[1] != 1:
                    previousyearmonth = [yearmonth[0], (yearmonth[1] - 1)]
                else:
                    previousyearmonth = [(yearmonth[0] -1 ), 12]
                if previousyearmonth not in yearMonthInt:
                    del yearMonthInt[i]
                    del yearMonth[i]
            print(rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            if valid and [year, month] in yearMonth:
                print("\033c" + rFunctions.color('bold', None) + "Projected Net Profit".center(40, "-") + rFunctions.color('reset', None) + "\n")
                projIn = projectedIncome(all = True, year = year, month = month, yearMonth = yearMonth, valid = valid)
                for i, yearmonth in enumerate(yearMonth):
                    if [year, month] == yearmonth:
                        [yearInt, monthInt] =yearMonthInt[i]
                if monthInt != 1:
                    previousYearInt, previousMonthInt = yearInt, (monthInt - 1)
                else:
                    previousYearInt, previousMonthInt = (yearInt - 1), 12
                previousMonth, previousYear, _ = rFunctions.validMonthYear(previousMonthInt, previousYearInt)
                _ , requiredExpenses, _ = totalExpenses(all = True, year = previousYear, month = previousMonth, yearMonth = yearMonth, valid = valid) #changed to projected expenses
                print(f"""{rFunctions.color('underline', None)}Net Profit{rFunctions.color('reset', None)}
Projected Revenue - Required Expenses [Based on {previousMonth} {previousYear}] = RM {(projIn - requiredExpenses):.2f}\n""")
                if not rFunctions.askContinue():
                    break
                time.sleep(2)
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for projected income in {month} {year}")
            time.sleep(2)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

#(ii) Financial reporting
def financialReporting():
    while True:
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Financial Reporting".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 💲 Total Revenue
2. 💸 Total Expenses
3. 🗃️  Financial Report
4. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit():
                functionality = int(functionality)
            if functionality in [1, "total revenue", "1. total revenue"]:
                totalRevenue()
            elif functionality in [2, "total expenses", "2. total expenses"]:
                totalExpenses()
            elif functionality in [3, "financial report", "3. financial report"]:
                financialReport()
            elif functionality in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def totalRevenue(all: bool = False, year: str = "", month: str = "", yearMonth: list = [], valid: bool = False, askPrint = True):
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            ordersDict = rFunctions.readFile("order")
            if all:
                totalRevenue = 0.00
                for order in ordersDict["orders"]:
                    orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").month
                    orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").year
                    orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
                    if orderMonth == month and orderYear == year:
                        totalBill = 0.00
                        for bill in eval(order["products"]):
                            totalBill += bill[4]
                        totalRevenue = round(totalRevenue + totalBill, 2)
                if askPrint:
                    print(f"{rFunctions.color('underline', None)}Total Income Summary for {month} {year}{rFunctions.color('reset', None)}\nTotal Revenue: RM %.2f"%(totalRevenue) + "\n")
                return totalRevenue
            else:
                while True:
                    try:
                        os.system('cls')
                        print(f"{rFunctions.color('bold', None)}" + "Total Income".center(40, "-") + f"{rFunctions.color('reset', None)}")
                        yearMonth = []
                        print("List of Monthly Income Available:")
                        for order in ordersDict["orders"]:
                            orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").month
                            orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").year
                            orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
                            if [orderYear, orderMonth] not in yearMonth:
                                yearMonth.append([orderYear, orderMonth])
                        print(rFunctions.tabulateGivenData(header = ["Year", "Month"], data = yearMonth, tbfmt = "simple_grid"))
                        month, year = input("Enter month and year: ").split()
                        month, year, valid = rFunctions.validMonthYear(month, year)
                        if valid and [year, month] in yearMonth:
                            print("\033c" + f"Total income in {month} {year}".center(40, "-"))
                            productRevenue = []
                            finalTotalRevenue = 0.00
                            for product in productsDict["products"]:
                                totalRevenue = 0.00
                                totalSales = 0
                                for order in ordersDict["orders"]:
                                    orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").month
                                    orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").year
                                    orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
                                    if orderMonth == month and orderYear == year:
                                        sales = 0
                                        totalBill = 0.00
                                        for bill in eval(order["products"]):
                                            if bill[0] == product["id"]:
                                                sales += bill[2]
                                                totalBill += bill[4]
                                        totalSales += sales
                                        totalRevenue = round(totalRevenue + totalBill, 2)
                                finalTotalRevenue += totalRevenue
                                if totalRevenue != 0.00:
                                    productRevenue.append([product["id"], product["name"], product["price"], totalSales, f"RM {totalRevenue:.2f}"])
                            print(rFunctions.tabulateGivenData(["Product ID", "Name", "Price", "Sales", "Revenue"], productRevenue, tbfmt = "simple_grid"))
                            print(f"Total Revenue for {month} {year}: RM %.2f"%(finalTotalRevenue) + "\n")
                            if not rFunctions.askContinue():
                                break
                        elif not valid:
                            continue
                        elif [year, month] not in yearMonth:
                            raise ValueError(f"Invalid input ☹️ : No records for income in {month} {year}")
                        time.sleep(2)
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def totalExpenses(all: bool = False, year: str = "", month: str = "", yearMonth: list = [], valid: bool = False, askPrint = True): #later then think how to simplify the tabulate section
    while True:
        cogsDict = rFunctions.readFile("cogs")
        opExpDict = rFunctions.readFile("operating")
        payrollDict = rFunctions.readFile("payroll")
        taxesDict = rFunctions.readFile("taxe")
        loansDict = rFunctions.readFile("loan")
        if all:
            dictsRole = ["cogs", "operating", "payroll", "taxe", "loan"]
            listofDicts = [cogsDict, opExpDict, payrollDict, taxesDict, loansDict]
            cogs = 0.00
            operatingExp, requiredOpExp = 0.00, 0.00
            payroll, requiredPayroll = 0.00, 0.00
            taxes, requiredTaxes = 0.00, 0.00
            loans, requiredLoans = 0.00, 0.00
            for i, role in enumerate(dictsRole):
                for data in listofDicts[i][f"{role}s"]:
                    dataMonthInt = datetime.strptime(data["date"], "%Y-%m-%d").month
                    dataYearInt = datetime.strptime(data["date"], "%Y-%m-%d").year
                    dataMonth, dataYear, _ = rFunctions.validMonthYear(dataMonthInt, dataYearInt)
                    if dataMonth == month and dataYear == year:
                        if i == 0:
                            cogs += rFunctions.extractNumber(data["amount"])
                        elif i == 1:
                            if data["status"].lower() == "paid":
                                operatingExp += rFunctions.extractNumber(data["amount"])
                            requiredOpExp += rFunctions.extractNumber(data["amount"])
                        elif i == 2:
                            if data["status"].lower() == "paid":
                                payroll += rFunctions.extractNumber(data["amount"])
                            requiredPayroll += rFunctions.extractNumber(data["amount"])
                        elif i == 3:
                            if data["status"].lower() == "paid":
                                taxes += rFunctions.extractNumber(data["amount"])
                            requiredTaxes += rFunctions.extractNumber(data["amount"])
                        elif i == 4:
                            if data["status"].lower() == "paid":
                                loans += rFunctions.extractNumber(data["amount"])
                            requiredLoans += rFunctions.extractNumber(data["amount"])
            if askPrint:
                print(f"{rFunctions.color('underline', None)}Expenses Summary for {month} {year}{rFunctions.color('reset', None)}\n")
            dataList = [
                ["Cost of Goods Sold", "RM %.2f"%(cogs)],
                ["Operating Expenses", "RM %.2f"%(operatingExp) + rFunctions.color('red', 'foreground') + " (- RM %.2f)"%(requiredOpExp - operatingExp) + rFunctions.color('reset', None)],
                ["Payroll Expenses", "RM %.2f"%(payroll) + rFunctions.color('red', 'foreground') + " (- RM %.2f)"%(requiredPayroll - payroll) + rFunctions.color('reset', None)],
                ["Taxes", "RM %.2f"%(taxes) + rFunctions.color('red', 'foreground') + " (- RM %.2f)"%(requiredTaxes - taxes) + rFunctions.color('reset', None)],
                ["Miscellaneous Loans", "RM %.2f"%(loans) + rFunctions.color('red', 'foreground') + " (- RM %.2f)"%(requiredLoans - loans) + rFunctions.color('reset', None)],
            ]
            if askPrint:
                print(rFunctions.tabulateGivenData(["Type of Expenses", "Amount"], dataList, tbfmt = "github") + "\n")
            return (cogs + operatingExp + payroll + taxes + loans), (cogs + requiredOpExp + requiredPayroll + requiredTaxes + requiredLoans), cogs
        else:
            try:
                # print("\033c") #clear entire terminal, works better than os.system('cls')
                print("\033c" + rFunctions.color('bold', None) + "-"*40 + "\n" + "Total Expenses".center(40) + "\n" + "-"*40 + rFunctions.color('reset', None))
                print(rFunctions.tabulateGivenData(["No", "Type of Expenses"], [[1, "Cost of Goods Sold (COGS)"], [2, "Operating Expenses"], [3, "Payroll Expenses"], [4, "Taxes"], [5, "Miscellaneous Loans"]], tbfmt = "simple_grid"))
                expensesType = input("Enter you selection: ").lower()
                rFunctions.clearPreviousLine()
                if expensesType.isdigit():
                    expensesType = int(expensesType)
                if expensesType in [1, "cost of goods sold", "cost of goods sold (cogs)", "cogs"]:
                    dataDict = cogsDict
                    role = "cogs"
                    type = "Cost of Goods Sold"
                    print(f"\n{rFunctions.color('underline', None)}Cost of Goods Sold{rFunctions.color('reset', None)}")
                elif expensesType in [2,  "operating expenses", "operating"]:
                    dataDict = opExpDict
                    role = "operating"
                    type = "Operating Expenses"
                    print(f"\n{rFunctions.color('underline', None)}Operating Expenses{rFunctions.color('reset', None)}")
                elif expensesType in [3, "payroll expenses", "payroll"]:
                    dataDict = payrollDict
                    role = "payroll"
                    type = "Payroll Expenses"
                    print(f"\n{rFunctions.color('underline', None)}Payroll Expenses{rFunctions.color('reset', None)}")
                elif expensesType in [4, "taxes", "tax"]:
                    dataDict = taxesDict
                    role = "taxe"
                    type = "Taxes"
                    print(f"\n{rFunctions.color('underline', None)}Taxes{rFunctions.color('reset', None)}")
                elif expensesType in [5,  "miscellaneous loans", "loans"]:
                    dataDict = loansDict
                    role = "loan"
                    type = "Miscellaneous Loans"
                    print(f"\n{rFunctions.color('underline', None)}Miscellaneous Loans{rFunctions.color('reset', None)}")
                else:
                    raise ValueError(f"Invalid type of expenses ☹️ : {expensesType} is not found")
                print("List of available expenses for:")
                yearMonth = []
                for data in dataDict[f"{role}s"]:
                    dataMonthInt = datetime.strptime(data["date"], "%Y-%m-%d").month
                    dataYearInt = datetime.strptime(data["date"], "%Y-%m-%d").year
                    dataMonth, dataYear, _ = rFunctions.validMonthYear(dataMonthInt, dataYearInt)
                    if [dataYear, dataMonth] not in yearMonth:
                        yearMonth.append([dataYear, dataMonth])
                print(rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
                while True:
                    try:
                        month, year = input("Enter month and year: ").split()
                        rFunctions.clearPreviousLine()
                        month, year, valid = rFunctions.validMonthYear(month, year)
                        if valid and [year, month] in yearMonth:
                            print("\033c")
                            print(f"{type} for {month} {year}".center(40, "-"))
                            expenses = []
                            bakerPayroll = []
                            cashierPayroll = []
                            totalExpenses = 0.00
                            requiredExpenses = 0.00
                            for data in dataDict[f"{role}s"]:
                                dataMonthInt = datetime.strptime(data["date"], "%Y-%m-%d").month
                                dataYearInt = datetime.strptime(data["date"], "%Y-%m-%d").year
                                dataMonth, dataYear, _ = rFunctions.validMonthYear(dataMonthInt, dataYearInt)
                                if dataMonth == month and dataYear == year:
                                    if type in ["Taxes", "Operating Expenses", "Miscellaneous Loans"]:
                                        if data["status"].lower() == "paid":
                                            expenses.append([data["category"], data["name"], data["amount"], data["date"], f"{rFunctions.color('green', 'foreground')}{data["status"]}{rFunctions.color('reset', None)}"])
                                            totalExpenses += rFunctions.extractNumber(data["amount"])
                                        else:
                                            expenses.append([data["category"], data["name"], data["amount"], data["date"], f"{rFunctions.color('red', 'foreground')}{data["status"]}{rFunctions.color('reset', None)}"])
                                    elif type == "Cost of Goods Sold":
                                        expenses.append([data["category"], data["name"], data["quantity"], data["amount"], data["suppliers"], data["date"]])
                                    elif type == "Payroll Expenses":
                                        if data["status"].lower() == "paid":
                                            if data["position"].lower() == "baker":
                                                bakerPayroll.append([data["category"], data["id"], data["amount"], data["date"], f"{rFunctions.color('green', 'foreground')}{data["status"]}{rFunctions.color('reset', None)}"])
                                            elif data["position"].lower() == "cashier":
                                                cashierPayroll.append([data["category"], data["id"], data["amount"], data["date"], f"{rFunctions.color('green', 'foreground')}{data["status"]}{rFunctions.color('reset', None)}"])
                                            totalExpenses += rFunctions.extractNumber(data["amount"])
                                        else:
                                            if data["position"].lower() == "baker":
                                                bakerPayroll.append([data["category"], data["id"], data["amount"], data["date"], f"{rFunctions.color('red', 'foreground')}{data["status"]}{rFunctions.color('reset', None)}"])
                                            elif data["position"].lower() == "cashier":
                                                cashierPayroll.append([data["category"], data["id"], data["amount"], data["date"], f"{rFunctions.color('red', 'foreground')}{data["status"]}{rFunctions.color('reset', None)}"])
                                    requiredExpenses += rFunctions.extractNumber(data["amount"])
                            if type in ["Taxes", "Operating Expenses", "Miscellaneous Loans"]:
                                print(f"""{rFunctions.tabulateGivenData(["Category", "Name", "Amount", "Due Date", "Status"], expenses, tbfmt = "simple_grid")}
Total Expenses: RM {totalExpenses:.2f}
Total Required Expenses: RM {requiredExpenses:.2f}{rFunctions.color('red', 'foreground')} (- RM {(requiredExpenses - totalExpenses):.2f}){rFunctions.color('reset', None) }\n""")
                            elif type == "Cost of Goods Sold":
                                print(rFunctions.tabulateGivenData(["Category", "Name", "Quantity", "Amount", "Supplier", "Date"], expenses, tbfmt = "simple_grid") + "\n" + "Total Expenses: RM %.2f\n"%(requiredExpenses))
                            elif type == "Payroll Expenses":
                                print("Baker: \n" + rFunctions.tabulateGivenData(["Category", "Employee ID", "Amount", "Scheduled Date", "Status"], bakerPayroll, tbfmt = "simple_grid"))
                                print(f"""\nCashier:
{rFunctions.tabulateGivenData(["Category", "Employee ID", "Amount", "Scheduled Date", "Status"], cashierPayroll, tbfmt = "simple_grid")}
Total Expenses: RM {totalExpenses:.2f}
Total Required Expenses: RM {requiredExpenses:.2f}{rFunctions.color('red', 'foreground') } (- RM {(requiredExpenses - totalExpenses):.2f}){rFunctions.color('reset', None)}\n""")
                            break
                        elif not valid:
                            continue
                        elif [year, month] not in yearMonth:
                            raise ValueError(f"Invalid input ☹️ : No records for total expenses in {month} {year}")
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                if not rFunctions.askContinue():
                    break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)

def financialReport():
    while True:
        ordersDict = rFunctions.readFile("order")
        try:
            os.system('cls')
            print(f"{rFunctions.color('bold', None)}" + "Monthly Financial Report".center(40, "-") + f"{rFunctions.color('reset', None)}")
            yearMonth = []
            print("List of Monthly Income Available:")
            for order in ordersDict["orders"]:
                orderMonthInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").month
                orderYearInt = datetime.strptime(order["orderCreatedDateTime"], "%Y-%m-%d %H:%M:%S").year
                orderMonth, orderYear, _ = rFunctions.validMonthYear(orderMonthInt, orderYearInt)
                if [orderYear, orderMonth] not in yearMonth:
                    yearMonth.append([orderYear, orderMonth])
            print(rFunctions.tabulateGivenData(header = ["Year", "Month"], data = yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            monthInt, yearInt = datetime.strptime(month, "%B").month, datetime.strptime(year, "%Y").year
            if valid and [year, month] in yearMonth:
                print(f"""\033c{rFunctions.color('bold', None)}{"="*40}
{f"Financial Report for {month} {year}".center(40) }
{"="*40}\n
{"Profit and Loss Summary".center(40, "-")}{rFunctions.color('reset', None)}\n""")
                income = totalRevenue(all = True, year = year, month = month, yearMonth = yearMonth, valid = valid)
                expenses, _, _ = totalExpenses(all = True, year = year, month = month, yearMonth = yearMonth, valid = valid)
                print(f"""{rFunctions.color('underline', None)}Net Profit for {month} {year}{rFunctions.color('reset', None)}
Total Income - Total Expenses = RM {(income - expenses):.2f}\n""")
                print(rFunctions.color('bold', None) + "Cash Flow Summary".center(40, "-") + rFunctions.color('reset', None))
                if monthInt != 1:
                    previousMonth, previousYear, _ = rFunctions.validMonthYear((monthInt - 1), yearInt)
                else:
                    previousMonth, previousYear, _ = rFunctions.validMonthYear(12, (yearInt - 1))
                previousMonthIncome = totalRevenue(all = True, year = previousYear, month = previousMonth, yearMonth = yearMonth, valid = valid, askPrint = False)
                previousMonthExpenses, _, _ = totalExpenses(all = True, year = previousYear, month = previousMonth, yearMonth = yearMonth, valid = valid, askPrint = False)
                print(previousMonth, previousYear)
                print(f"""\nOpening Cash Balance: RM {(previousMonthIncome - previousMonthExpenses):.2f}\n
Cash Inflows: RM {income:.2f}\n
Cash Outflows: RM {expenses:.2f}\n
Closing Cash Balance: RM {(((previousMonthIncome - previousMonthExpenses) + income) - expenses):.2f}\n
{"-"*40}\n""")
                time.sleep(2)
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for total expenses in {month} {year}")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

#(iii) Tax management
def taxManagement():
    while True:
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Tax Management".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🗓️  Monthly Tax Report
2. ➕ Add Tax
3. ⏰ Update Tax Status
4. 📈 Update Tax Rates
5. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit():
                functionality = int(functionality)
            if functionality in [1, "monthly tax report", "1. monthly tax report"]:
                monthlyTaxReport()
            elif functionality in [2, "add tax", "2. add tax"]:
                addTax()
            elif functionality in [3, "update tax status", "3. update tax status"]:
                updateTaxStatus()
            elif functionality in [4, "update tax rates", "4. update tax rates"]:
                updateTaxRates()
            elif functionality in [5, "back", "5. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def monthlyTaxReport():
    while True:
        taxRateDict = rFunctions.readFile("tax rate")
        taxesDict = rFunctions.readFile("taxe")
        payrollDict = rFunctions.readFile("payroll")
        try:
            print("\033c" + "Monthly Tax Report".center(40, "-"))
            yearMonth = []
            for tax in taxesDict["taxes"]:
                taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                taxMonth, taxYear, _ = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                yearMonth.append([taxYear, taxMonth]) if [taxYear, taxMonth] not in yearMonth else yearMonth
            print("List of available Taxes:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            if [year, month] in yearMonth and valid:
                print(f"""\033c{rFunctions.color('bold', None)}{"="*40}
{f"Tax Management Report for {month} {year}".center(40)}
{"="*40}{rFunctions.color('reset', None)}""")
                taxRates = []
                for rate in taxRateDict["tax rates"]:
                    taxRates.append((rate["tax type"], rate["rate (%)"])) if (rate["tax type"], rate["rate (%)"]) not in taxRates else taxRates
                categories = ["sales tax", "income tax", "payroll tax"]
                totalTax = 0.00
                for category in categories:
                    for tax in taxesDict["taxes"]:
                        taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                        taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                        taxMonth, taxYear, _ = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                        if taxMonth == month and taxYear == year:
                            if tax["category"].lower() == category:
                                taxOwed = tax["amount"]
                                for rate in taxRates:
                                    if rate[0].lower() == category:
                                        taxRate = f"{float(rate[1]):.1f}"
                                if tax["status"].lower() == "paid":
                                    taxStatus = f"{rFunctions.color('green', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"
                                else:
                                    taxStatus = f"{rFunctions.color('red', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"
                                if category == "sales tax":
                                    total = "Total Sales"
                                    totalData = f"RM {round((totalRevenue(all = True, year = taxYear, month = taxMonth, yearMonth = yearMonth, valid = valid, askPrint = False)), 2)}"
                                elif category == "income tax":
                                    total = "Net Profit"
                                    income = totalRevenue(all = True, year = taxYear, month = taxMonth, yearMonth = yearMonth, valid = valid, askPrint = False)
                                    expenses, _, _ = totalExpenses(all = True, year = taxYear, month = taxMonth, yearMonth = yearMonth, valid = valid, askPrint = False)
                                    totalData = f"RM {round((income - expenses), 2)}"
                                elif category == "payroll tax":
                                    total = "Total Payroll"
                                    totalPayroll = 0.00
                                    for payroll in payrollDict["payrolls"]:
                                        payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").month
                                        payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").year
                                        payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
                                        if payrollMonth == month and payrollYear == year:
                                            totalPayroll += rFunctions.extractNumber(payroll["amount"])
                                    totalData = f"RM {round(totalPayroll, 2)}"
                                taxData = [[f"{total}", totalData], [f"{category.capitalize()} Rate (%)", taxRate], [f"{category.capitalize()} Owed", taxOwed], ["Status", taxStatus]]
                                print(f"{category.capitalize()}:\n" + rFunctions.tabulateGivenData(["Field", "Details"], taxData, tbfmt = "simple_grid") + "\n")
                                totalTax += round(rFunctions.extractNumber(taxOwed), 2)
                print("-"*40 + f"\nTotal Tax Liability: RM {totalTax:.2f}\n" + "-"*40 + "\n")
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No tax records for {month} {year}")
            time.sleep(2)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def addTax():
    while True:
        try:
            print("\033c" + "Add New Tax".center(40, "-") + "\n1. Sales Tax\n2. Income Tax\n3. Payroll Tax\n4. 🔙 Back\n" + "-"*40)
            print(f"""{rFunctions.color('blue', 'foreground')}Important 📍:
(i) Income Tax calculated without including tax expenses
(ii) Payroll Tax calculated for both paid and unpaid payroll expenses{rFunctions.color('reset', None)}\n""")
            tax = input("Enter your selection: ").lower()
            if tax.isdigit():
                tax = int(tax)
            if tax in  [1, "sales tax", "1. sales tax"]:
                addSalesTax()
            elif tax in [2, "income tax", "2. income tax"]: #how to exclude the tax expenses??
                addIncomeTax()
            elif tax in [3, "payroll tax", "3. payroll tax"]:
                addPayrollTax()
            elif tax in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid Input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def addSalesTax():
    taxRateDict = rFunctions.readFile("tax rate")
    taxesDict = rFunctions.readFile("taxe")
    print("\033c" + "Add New Sales Tax".center(40, "-"))
    category = "Sales Tax"
    for rate in taxRateDict["tax rates"]:
        if rate["tax type"].lower() == category.lower():
            taxRate = rFunctions.extractNumber(rate["rate (%)"])/100
    yearMonth = []
    for tax in taxesDict["taxes"]:
        if tax["category"] == category:
            taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
            taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
            taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
            yearMonth.append([taxYear, taxMonth]) if [taxYear, taxMonth] not in yearMonth else yearMonth
    print("List of available Sales Taxes:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
    while True:
        try:
            update = input("Enter <UPDATE> to update existing sales tax: ").lower()
            rFunctions.clearPreviousLine()
            if update == "update":
                updateMonth, updateYear = input("Enter month and year: ").split()
                updateMonth, updateYear, valid = rFunctions.validMonthYear(updateMonth, updateYear)
                if [updateYear, updateMonth] not in yearMonth: #not complete????
                    raise ValueError(f"Invalid input ☹️ : No records for sales tax in {updateMonth} {updateYear}")
                break
            else:
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
    if update == "update":
        print(f"""\033c{"Update Sales Tax".center(40, "-")}
{rFunctions.color('blue', 'foreground')}Important 📍:
(i) Sales Tax calculated based on current sales
(ii) Due Date cannot be modified{rFunctions.color('reset', None)}\n""")
        for tax in taxesDict["taxes"]:
            if tax["category"] == category:
                taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                taxMonth, taxYear, _ = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                if taxMonth == updateMonth and taxYear == updateYear:
                    date, category, name, status = tax["date"], tax["category"], tax["name"], tax["status"]
                    tax["amount"] = f"RM {round((totalRevenue(all = True, year = taxYear, month = taxMonth, yearMonth = yearMonth, valid = valid, askPrint = False))*taxRate, 2)}"
                    amount = tax["amount"]
                    while True:
                        try:
                            status = input("Status of Sales Tax [paid/ unpaid]: ").lower()
                            if status != "paid" and status != "unpaid":
                                raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                            tax["status"] = status.capitalize()
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Date: {date}\n\nCategory: {category}\n\nName: {name}\n\nAmount: {amount}\n\nStatus: {status.capitalize()}\n\nLast Updated: {currentDate}\n")
        confirm = input("Enter <YES> to update tax: ")
        rFunctions.clearPreviousLine()
        if confirm != "yes":
            print(f"{rFunctions.color('red', 'foreground')}{category} '{name}' is not updated ☹️{rFunctions.color('reset', None)}")
        else:
            rFunctions.writeFile("taxe", taxesDict)
            print(f"{rFunctions.color('green', 'foreground')}{category} '{name}' is successfully updated 😄{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()
    else:
        while True:
            try:
                print("\033c" + "Add New Sales Tax".center(40, "-"))
                currentDate = datetime.now().date()
                date = input("Due Date [YYYY-MM-DD]: ")
                date = datetime.strptime(date, "%Y-%m-%d").date()
                if date.month < currentDate.month or date.year < currentDate.year or (date.month == currentDate.month and date.day < currentDate.day):
                    raise ValueError("Due date given is overdue.")
                month, year, valid = rFunctions.validMonthYear(date.month, date.year)
                if [year, month] in yearMonth:
                    raise ValueError(f"Sales tax for {month} {year} already exist")
                if valid:
                    break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
        amount = f"RM {round((totalRevenue(all = True, year = year, month = month, yearMonth = [[year, month]], valid = valid, askPrint = False))*taxRate, 2)}"
        name = f"{category} for {month} {year}"
        print()
        while True:
            try:
                status = input("Status of Sales Tax [paid/ unpaid]: ").lower()
                if status != "paid" and status != "unpaid":
                    raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Date: {date}\n\nCategory: {category}\n\nName: {name}\n\nAmount: {amount}\n\nStatus: {status.capitalize()}\n\nLast Updated: {currentDate}")
        newTax = {"date": date, "category": category, "name": name, "amount": amount, "status": status.capitalize(), "last updated": currentDate}
        print()
        confirm = input("Enter <YES> to save tax: ")
        rFunctions.clearPreviousLine()
        if confirm != "yes":
            print(f"{rFunctions.color('red', 'foreground')}{category} '{name}' is not saved ☹️{rFunctions.color('reset', None)}")
        else:
            rFunctions.appendFile("taxe", taxesDict, newTax)
            print(f"{rFunctions.color('green', 'foreground')}{category} '{name}' is successfully saved 😄{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()

def addIncomeTax():
    taxRateDict = rFunctions.readFile("tax rate")
    taxesDict = rFunctions.readFile("taxe")
    print("\033c" + "Add New Income Tax".center(40, "-"))
    category = "Income Tax"
    for rate in taxRateDict["tax rates"]:
        if rate["tax type"].lower() == category.lower():
            taxRate = rFunctions.extractNumber(rate["rate (%)"])/100
    yearMonth = []
    for tax in taxesDict["taxes"]:
        if tax["category"] == category:
            taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
            taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
            taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
            yearMonth.append([taxYear, taxMonth]) if [taxYear, taxMonth] not in yearMonth else yearMonth
    print("List of available Income Taxes:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
    while True:
        try:
            update = input("Enter <UPDATE> to update existing income tax: ").lower()
            rFunctions.clearPreviousLine()
            if update == "update":
                updateMonth, updateYear = input("Enter month and year: ").split()
                updateMonth, updateYear, valid = rFunctions.validMonthYear(updateMonth, updateYear)
                if [updateYear, updateMonth] not in yearMonth:
                    raise ValueError(f"Invalid input ☹️ : No records for income tax in {updateMonth} {updateYear}")
                break
            else:
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
    if update == "update":
        print(f"""\033c{"Update Income Tax".center(40, "-")}
{rFunctions.color('blue', 'foreground')}Important 📍:
(i) Sales Tax calculated based on current sales
(ii) Due Date cannot be modified{rFunctions.color('reset', None)}\n""")
        for tax in taxesDict["taxes"]:
            if tax["category"] == category:
                taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                taxMonth, taxYear, _ = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                if taxMonth == updateMonth and taxYear == updateYear:
                    date, category, name, status = tax["date"], tax["category"], tax["name"], tax["status"]
                    income = totalRevenue(all = True, year = taxYear, month = taxMonth, yearMonth = yearMonth, valid = valid, askPrint = False)
                    _, _, expenses = totalExpenses(all = True, year = taxYear, month = taxMonth, yearMonth = yearMonth, valid = valid, askPrint = False)
                    tax["amount"] = f"RM {round((income - expenses)*taxRate, 2)}"
                    amount = tax["amount"]
                    while True:
                        try:
                            status = input("Status of Income Tax [paid/ unpaid]: ").lower()
                            if status != "paid" and status != "unpaid":
                                raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                            tax["status"] = status.capitalize()
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Date: {date}\n\nCategory: {category}\n\nName: {name}\n\nAmount: {amount}\n\nStatus: {status.capitalize()}\n\nLast Updated: {currentDate}\n")
        confirm = input("Enter <YES> to update tax: ")
        rFunctions.clearPreviousLine()
        if confirm != "yes":
            print(f"{rFunctions.color('red', 'foreground')}{category} '{name}' is not updated ☹️{rFunctions.color('reset', None)}")
        else:
            rFunctions.writeFile("taxe", taxesDict)
            print(f"{rFunctions.color('green', 'foreground')}{category} '{name}' is successfully updated 😄{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()
    else:
        while True:
            try:
                print("\033c" + "Add New Income Tax".center(40, "-"))
                currentDate = datetime.now()
                date = input("Due Date [YYYY-MM-DD]: ")
                date = datetime.strptime(date, "%Y-%m-%d").date()
                if date.month < currentDate.month or date.year < currentDate.year or (date.month == currentDate.month and date.day < currentDate.day):
                    raise ValueError("Due date is overdue.")
                month, year, valid = rFunctions.validMonthYear(date.month, date.year)
                if [year, month] in yearMonth:
                    raise ValueError(f"Income tax for {month} {year} already exist")
                if valid:
                    break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
        income = totalRevenue(all = True, year = year, month = month, yearMonth = [[year, month]], valid = valid, askPrint = False)
        _, _, expenses = totalExpenses(all = True, year = year, month = month, yearMonth = [[year, month]], valid = valid, askPrint = False)
        amount = f"RM {round((income - expenses)*taxRate, 2)}"
        name = f"{category} for {month} {year}"
        print()
        while True:
            try:
                status = input("Status of Income Tax [paid/ unpaid]: ").lower()
                if status != "paid" and status != "unpaid":
                    raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Date: {date}\n\nCategory: {category}\n\nName: {name}\n\nAmount: {amount}\n\nStatus: {status.capitalize()}\n\nLast Updated: {currentDate}")
        newTax = {"date": date, "category": category, "name": name, "amount": amount, "status": status.capitalize(), "last updated": currentDate}
        print()
        confirm = input("Enter <YES> to save tax: ")
        rFunctions.clearPreviousLine()
        if confirm != "yes":
            print(f"{rFunctions.color('red', 'foreground')}{category} '{name}' is not saved ☹️{rFunctions.color('reset', None)}")
        else:
            rFunctions.appendFile("taxe", taxesDict, newTax)
            print(f"{rFunctions.color('green', 'foreground')}{category} '{name}' is successfully saved 😄{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()

def addPayrollTax():
    taxRateDict = rFunctions.readFile("tax rate")
    taxesDict = rFunctions.readFile("taxe")
    payrollDict = rFunctions.readFile("payroll")
    print("\033c" + "Add New Payroll Tax".center(40, "-"))
    category = "Payroll Tax"
    for rate in taxRateDict["tax rates"]:
        if rate["tax type"].lower() == category.lower():
            taxRate = rFunctions.extractNumber(rate["rate (%)"])/100
    yearMonth = []
    for tax in taxesDict["taxes"]:
        if tax["category"] == category:
            taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
            taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
            taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
            yearMonth.append([taxYear, taxMonth]) if [taxYear, taxMonth] not in yearMonth else yearMonth
    print("List of available Payroll Taxes:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
    while True:
        try:
            update = input("Enter <UPDATE> to update existing payroll tax: ").lower()
            rFunctions.clearPreviousLine()
            if update == "update":
                updateMonth, updateYear = input("Enter month and year: ").split()
                updateMonth, updateYear, valid = rFunctions.validMonthYear(updateMonth, updateYear)
                if [updateYear, updateMonth] not in yearMonth:
                    raise ValueError(f"Invalid input ☹️ : No records for payroll tax in {updateMonth} {updateYear}")
                break
            else:
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
    if update == "update":
        print(f"""\033c{"Update Payroll Tax".center(40, "-")}
{rFunctions.color('blue', 'foreground')}Important 📍:
(i) Sales Tax calculated based on current sales
(ii) Due Date cannot be modified{rFunctions.color('reset', None)}\n""")
        for tax in taxesDict["taxes"]:
            if tax["category"] == category:
                taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                taxMonth, taxYear, _ = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                if taxMonth == updateMonth and taxYear == updateYear: #heree
                    date, category, name, status = tax["date"], tax["category"], tax["name"], tax["status"]
                    totalPayroll = 0.00
                    for payroll in payrollDict["payrolls"]:
                        payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").month
                        payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").year
                        payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
                        if payrollMonth == taxMonth and payrollYear == taxYear:
                            totalPayroll += rFunctions.extractNumber(payroll["amount"])
                    tax["amount"] = f"RM {round(totalPayroll*taxRate, 2)}"
                    amount = tax["amount"]
                    while True:
                        try:
                            status = input("Status of Payroll Tax [paid/ unpaid]: ").lower()
                            if status != "paid" and status != "unpaid":
                                raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                            tax["status"] = status.capitalize()
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Date: {date}\n\nCategory: {category}\n\nName: {name}\n\nAmount: {amount}\n\nStatus: {status.capitalize()}\n\nLast Updated: {currentDate}\n")
        confirm = input("Enter <YES> to update tax: ")
        rFunctions.clearPreviousLine()
        if confirm != "yes":
            print(f"{rFunctions.color('red', 'foreground')}{category} '{name}' is not updated ☹️{rFunctions.color('reset', None)}")
        else:
            rFunctions.writeFile("taxe", taxesDict)
            print(f"{rFunctions.color('green', 'foreground')}{category} '{name}' is successfully updated 😄{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()
    else:
        while True:
            try:
                print("\033c" + "Add New Payroll Tax".center(40, "-"))
                currentDate = datetime.now().date()
                date = input("Due Date [YYYY-MM-DD]: ")
                date = datetime.strptime(date, "%Y-%m-%d").date()
                if date.month < currentDate.month or date.year < currentDate.year or (date.month == currentDate.month and date.day < currentDate.day):
                    raise ValueError("Due date is overdue.")
                month, year, valid = rFunctions.validMonthYear(date.month, date.year)
                if [year, month] in yearMonth:
                    raise ValueError(f"Payroll tax for {month} {year} already exist")
                if valid:
                    break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
        totalPayroll = 0.00
        for payroll in payrollDict["payrolls"]:
            payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").month
            payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").year
            payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
            if payrollMonth == month and payrollYear == year:
                totalPayroll += rFunctions.extractNumber(payroll["amount"])
        amount = f"RM {round(totalPayroll*taxRate, 2)}"
        name = f"{category} for {month} {year}"
        print()
        while True:
            try:
                status = input("Status of Payroll Tax [paid/ unpaid]: ").lower()
                if status != "paid" and status != "unpaid":
                    raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        rFunctions.clearPreviousLine()
        currentDate = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"Date: {date}\n\nCategory: {category}\n\nName: {name}\n\nAmount: {amount}\n\nStatus: {status.capitalize()}\n\nLast Updated: {currentDate}")
        newTax = {"date": date, "category": category, "name": name, "amount": amount, "status": status.capitalize(), "last updated": currentDate}
        print()
        confirm = input("Enter <YES> to save tax: ")
        rFunctions.clearPreviousLine()
        if confirm != "yes":
            print(f"{rFunctions.color('red', 'foreground')}{category} '{name}' is not saved ☹️{rFunctions.color('reset', None)}")
        else:
            rFunctions.appendFile("taxe", taxesDict, newTax)
            print(f"{rFunctions.color('green', 'foreground')}{category} '{name}' is successfully saved 😄{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()

def updateTaxStatus():
    while True:
        taxesDict = rFunctions.readFile("taxe")
        try:
            print("\033c" + "Update Tax Status".center(40, "-") + "\n1. Sales Tax\n2. Income Tax\n3. Payroll Tax\n4. 🔙 Back\n" + "-"*40)
            tax = input("Enter your selection: ").lower()
            if tax.isdigit():
                tax = int(tax)
            if tax in  [1, "sales tax", "1. sales tax"]:
                print("\033c" + "Update Sales Tax Status".center(40, "-"))
                category = "Sales Tax"
                yearMonth = []
                for tax in taxesDict["taxes"]:
                    if tax["category"] == category:
                        taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                        taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                        taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                        yearMonth.append([taxYear, taxMonth]) if [taxYear, taxMonth] not in yearMonth else yearMonth
                print("List of available Sales Taxes:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
                while True:
                    try:
                        updateMonth, updateYear = input("Enter month and year: ").split()
                        updateMonth, updateYear, valid = rFunctions.validMonthYear(updateMonth, updateYear)
                        if valid and [updateYear, updateMonth] not in yearMonth:
                            raise ValueError(f"Invalid input ☹️ : No records for sales tax in {updateMonth} {updateYear}")
                        elif not valid:
                            rFunctions.clearPreviousLine()
                        elif valid:
                            break
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                        rFunctions.clearPreviousLine()
                print("\033c" + f"Sales Tax for {updateMonth} {updateYear}".center(40, "-"))
                salesTax = []
                for tax in taxesDict["taxes"]:
                    if tax["category"] == category:
                        taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                        taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                        taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                        if taxMonth == updateMonth and taxYear == updateYear:
                            taxName = tax["name"]
                            if tax["status"].lower() == "paid":
                                salesTax = [["Due Date", tax["date"]],
                                            ["Name", tax["name"]],
                                            ["Tax Amount", tax["amount"]],
                                            ["Status", f"{rFunctions.color('green', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"],
                                            ["Last Updated", tax["last updated"]]]
                            else:
                                salesTax = [["Due Date", tax["date"]],
                                            ["Name", tax["name"]],
                                            ["Tax Amount", tax["amount"]],
                                            ["Status", f"{rFunctions.color('red', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"],
                                            ["Last Updated", tax["last updated"]]]
                print(rFunctions.tabulateGivenData(["Field", "Details"], salesTax, tbfmt = "simple_grid") + "\n")
                for tax in taxesDict["taxes"]:
                    if tax["name"] == taxName:
                        while True:
                            try:
                                status = input("Status of Sales Tax [paid/ unpaid]: ").lower()
                                if status != "paid" and status != "unpaid":
                                    raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                                break
                            except ValueError as vE:
                                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                                time.sleep(2)
                                rFunctions.clearPreviousLine()
                                rFunctions.clearPreviousLine()
                        tax["status"] = status.capitalize()
                rFunctions.clearPreviousLine()
                rFunctions.writeFile("taxe", taxesDict)
                print(f"{rFunctions.color('green', 'foreground')}{category} '{taxName}' is successfully updated 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            elif tax in  [2, "income tax", "2. income tax"]:
                print("\033c" + "Update Income Tax Status".center(40, "-"))
                category = "Income Tax"
                yearMonth = []
                for tax in taxesDict["taxes"]:
                    if tax["category"] == category:
                        taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                        taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                        taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                        yearMonth.append([taxYear, taxMonth]) if [taxYear, taxMonth] not in yearMonth else yearMonth
                print("List of available Income Taxes:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
                while True:
                    try:
                        updateMonth, updateYear = input("Enter month and year: ").split()
                        updateMonth, updateYear, valid = rFunctions.validMonthYear(updateMonth, updateYear)
                        if valid and [updateYear, updateMonth] not in yearMonth:
                            raise ValueError(f"Invalid input ☹️ : No records for income tax in {updateMonth} {updateYear}")
                        elif not valid:
                            rFunctions.clearPreviousLine()
                        elif valid:
                            break
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                        rFunctions.clearPreviousLine()
                print("\033c" + f"Income Tax for {updateMonth} {updateYear}".center(40, "-"))
                salesTax = []
                for tax in taxesDict["taxes"]:
                    if tax["category"] == category:
                        taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                        taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                        taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                        if taxMonth == updateMonth and taxYear == updateYear:
                            taxName = tax["name"]
                            if tax["status"].lower() == "paid":
                                salesTax = [["Due Date", tax["date"]],
                                            ["Name", tax["name"]],
                                            ["Tax Amount", tax["amount"]],
                                            ["Status", f"{rFunctions.color('green', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"],
                                            ["Last Updated", tax["last updated"]]]
                            else:
                                salesTax = [["Due Date", tax["date"]],
                                            ["Name", tax["name"]],
                                            ["Tax Amount", tax["amount"]],
                                            ["Status", f"{rFunctions.color('red', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"],
                                            ["Last Updated", tax["last updated"]]]
                print(rFunctions.tabulateGivenData(["Field", "Details"], salesTax, tbfmt = "simple_grid") + "\n")
                for tax in taxesDict["taxes"]:
                    if tax["name"] == taxName:
                        while True:
                            try:
                                status = input("Status of Income Tax [paid/ unpaid]: ").lower()
                                if status != "paid" and status != "unpaid":
                                    raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                                tax["status"] = status.capitalize()
                                break
                            except ValueError as vE:
                                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                                time.sleep(2)
                                rFunctions.clearPreviousLine()
                                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                rFunctions.writeFile("taxe", taxesDict)
                print(f"{rFunctions.color('green', 'foreground')}{category} '{taxName}' is successfully updated 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            elif tax in  [3, "payroll tax", "3. payroll tax"]:
                print("\033c" + "Update Payroll Tax Status".center(40, "-"))
                category = "Payroll Tax"
                yearMonth = []
                for tax in taxesDict["taxes"]:
                    if tax["category"] == category:
                        taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                        taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                        taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                        yearMonth.append([taxYear, taxMonth]) if [taxYear, taxMonth] not in yearMonth else yearMonth
                print("List of available Payroll Taxes:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
                while True:
                    try:
                        updateMonth, updateYear = input("Enter month and year: ").split()
                        updateMonth, updateYear, valid = rFunctions.validMonthYear(updateMonth, updateYear)
                        if valid and [updateYear, updateMonth] not in yearMonth:
                            raise ValueError(f"Invalid input ☹️ : No records for payroll tax in {updateMonth} {updateYear}")
                        elif not valid:
                            rFunctions.clearPreviousLine()
                        elif valid:
                            break
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                        rFunctions.clearPreviousLine()
                print("\033c" + f"Payroll Tax for {updateMonth} {updateYear}".center(40, "-"))
                salesTax = []
                for tax in taxesDict["taxes"]:
                    if tax["category"] == category:
                        taxMonthInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().month
                        taxYearInt = datetime.strptime(tax["date"], "%Y-%m-%d").date().year
                        taxMonth, taxYear, valid = rFunctions.validMonthYear(taxMonthInt, taxYearInt)
                        if taxMonth == updateMonth and taxYear == updateYear:
                            taxName = tax["name"]
                            if tax["status"].lower() == "paid":
                                salesTax = [["Due Date", tax["date"]],
                                            ["Name", tax["name"]],
                                            ["Tax Amount", tax["amount"]],
                                            ["Status", f"{rFunctions.color('green', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"],
                                            ["Last Updated", tax["last updated"]]]
                            else:
                                salesTax = [["Due Date", tax["date"]],
                                            ["Name", tax["name"]],
                                            ["Tax Amount", tax["amount"]],
                                            ["Status", f"{rFunctions.color('red', 'foreground')}{tax["status"]}{rFunctions.color('reset', None)}"],
                                            ["Last Updated", tax["last updated"]]]
                print(rFunctions.tabulateGivenData(["Field", "Details"], salesTax, tbfmt = "simple_grid") + "\n")
                for tax in taxesDict["taxes"]:
                    if tax["name"] == taxName:
                        while True:
                            try:
                                status = input("Status of Payroll Tax [paid/ unpaid]: ").lower()
                                if status != "paid" and status != "unpaid":
                                    raise ValueError("Invalid Input ☹️ : Tax status can only be paid or unpaid")
                                tax["status"] = status.capitalize()
                                break
                            except ValueError as vE:
                                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                                time.sleep(2)
                                rFunctions.clearPreviousLine()
                                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                rFunctions.writeFile("taxe", taxesDict)
                print(f"{rFunctions.color('green', 'foreground')}{category} '{taxName}' is successfully updated 😄{rFunctions.color('reset', None)}")
                time.sleep(2)
            elif tax in [4, "back", "4. back"]:
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def updateTaxRates():
    while True:
        taxRateDict = rFunctions.readFile("tax rate")
        print(f"""\033c{"Update Tax Rate".center(40, "-")}
{rFunctions.color('blue', 'foreground')}Important 📍: To keep tax records current and accurate, update tax records after tax rate is updated under 
{rFunctions.color('bold', None)}[Tax Management -> 1. Add Tax]{rFunctions.color('reset', None)}""")
        print(rFunctions.tabulateCsvData("tax rate", ["tax type", "rate (%)", "last updated"], tbfmt = "simple_grid"))
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        while True:
            try:
                taxType = input("Enter type of tax: ").capitalize()
                if taxType.lower() not in ["sales tax", "income tax", "payroll tax"]:
                    raise ValueError("Invalid input ☹️ : Type of tax must be either 'Sales Tax', 'Income Tax', or 'Payroll Tax'")
                newTaxRate = input("\nEnter new tax rate (%): ").replace("%", "").replace(" ", "")
                foundDigit = False
                for i, char in enumerate(newTaxRate):
                    if char.isalpha():
                        raise ValueError(f"Invalid Input ☹️ :Provide only numbers for tax rate")
                    if i == 0 and char.isdigit():
                        foundDigit = True
                        newTaxRate = rFunctions.extractNumber(newTaxRate)
                        break
                    if char.isdigit():
                        foundDigit = True
                        if newTaxRate[i - 1] == "-":
                            raise ValueError(f"Invalid Input ☹️ :Tax rate cannot be negative")
                        newTaxRate = rFunctions.extractNumber(newTaxRate)
                        break
                if not foundDigit:
                    raise ValueError(f"Invalid Input ☹️ :Tax rate not given")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        for rate in taxRateDict["tax rates"]:
            if rate["tax type"].lower() == taxType.lower():
                rate["rate (%)"] = round(newTaxRate, 1)
                rate["last updated"] = datetime.now().date()
        rFunctions.writeFile("tax rate", taxRateDict)
        print(f"\n{rFunctions.color('green', 'foreground')}Tax rate for {taxType} is successfully updated 😄{rFunctions.color('reset', None)}")
        time.sleep(2)
        rFunctions.clearPreviousLine()
        print(f"{rFunctions.color('green', 'foreground')}Proceed to {rFunctions.color('bold', None)}[Tax Management -> 1. Add Tax] to keep tax records up-to-date😄{rFunctions.color('reset', None)}")
        time.sleep(5)
        break

#(iv) Payroll management
def payrollManagement():
    while True:
        os.system('cls')
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Payroll Management".center(40) }
{"-"*40}{rFunctions.color('reset', None)}
1. 🗓️  Monthly Payroll Report
2. ➕ Add Payroll
3. ⏰ Update Payroll Status
4. 🔙 Back
{"-"*40}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit():
                functionality = int(functionality)
            if functionality in [1, "monthly payroll report", "1. monthly payroll report"]:
                monthlyPayrollReport()
            elif functionality in [2, "add payroll", "2. add payroll"]:
                addPayroll()
            elif functionality in [3, "update payroll status", "3. update payroll status"]:
                updatePayroll()
            elif functionality in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def monthlyPayrollReport():
    while True:
        try:
            taxRateDict = rFunctions.readFile("tax rate")
            payrollDict = rFunctions.readFile("payroll")
            bakersDict = rFunctions.readFile("baker")
            cashiersDict = rFunctions.readFile("cashier")
            print("\033c" + "Monthly Tax Report".center(40, "-"))
            yearMonth = []
            for payroll in payrollDict["payrolls"]:
                payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().month
                payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().year
                payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
                yearMonth.append([payrollYear, payrollMonth]) if [payrollYear, payrollMonth] not in yearMonth else yearMonth
            print("List of available payrolls:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            if [year, month] in yearMonth and valid:
                print(f"""\033c{rFunctions.color('bold', None)}{"="*40}
{f"Payroll Management Report for {month} {year}".center(40)}
{"="*40}{rFunctions.color('reset', None)}""")
                for rate in taxRateDict["tax rates"]:
                    if rate["tax type"].lower() == "payroll tax":
                        taxRate = rFunctions.extractNumber(rate["rate (%)"])/100
                totalSalaryPaid = 0.00
                totalBonusPaid = 0.00
                totalTaxPaid = 0.00
                payrollData = []
                for payroll in payrollDict["payrolls"]:
                    payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().month
                    payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().year
                    payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
                    if payrollMonth == month and payrollYear == year:
                        for baker in bakersDict["bakers"]:
                            if baker["id"] == payroll["id"]:
                                payrollTax = rFunctions.extractNumber(payroll["amount"])*taxRate
                                totalSalary = rFunctions.extractNumber(payroll["amount"]) + payrollTax
                                if payroll["status"].lower() == "paid":
                                    if payroll["category"].lower() == "salary":
                                        totalSalaryPaid += rFunctions.extractNumber(payroll["amount"])
                                    elif payroll["category"].lower() == "bonus":
                                        totalBonusPaid += rFunctions.extractNumber(payroll["amount"])
                                    totalTaxPaid += payrollTax
                                    payrollData.append([payroll["id"], baker["name"],
                                                        payroll["category"], payroll["amount"],
                                                        f"RM {payrollTax:.2f}",
                                                        f"RM {totalSalary:.2f}",
                                                        f"{rFunctions.color('green', 'foreground')}{payroll["status"]}{rFunctions.color('reset', None)}"])
                                else:
                                    payrollData.append([payroll["id"],
                                                        baker["name"],
                                                        payroll["category"],
                                                        payroll["amount"],
                                                        f"RM {payrollTax:.2f}",
                                                        f"RM {totalSalary:.2f}",
                                                        f"{rFunctions.color('red', 'foreground')}{payroll["status"]}{rFunctions.color('reset', None)}"])
                        for cashier in cashiersDict["cashiers"]:
                            if cashier["id"] == payroll["id"]:
                                payrollTax = rFunctions.extractNumber(payroll["amount"])*taxRate
                                totalSalary = rFunctions.extractNumber(payroll["amount"]) + payrollTax
                                if payroll["status"].lower() == "paid":
                                    if payroll["category"].lower() == "salary":
                                        totalSalaryPaid += rFunctions.extractNumber(payroll["amount"])
                                    elif payroll["category"].lower() == "bonus":
                                        totalBonusPaid += rFunctions.extractNumber(payroll["amount"])
                                    totalTaxPaid += payrollTax
                                    payrollData.append([payroll["id"],
                                                        cashier["name"],
                                                        payroll["category"],
                                                        payroll["amount"],
                                                        f"RM {payrollTax:.2f}",
                                                        f"RM {totalSalary:.2f}",
                                                        f"{rFunctions.color('green', 'foreground')}{payroll["status"]}{rFunctions.color('reset', None)}"])
                                else:
                                    payrollData.append([payroll["id"],
                                                        cashier["name"],
                                                        payroll["category"],
                                                        payroll["amount"],
                                                        f"RM {payrollTax:.2f}",
                                                        f"RM {totalSalary:.2f}",
                                                        f"{rFunctions.color('red', 'foreground')}{payroll["status"]}{rFunctions.color('reset', None)}"])
                print(rFunctions.tabulateGivenData(["Employee ID", "Employee Name", "Type of Payroll", "Amount", "Payroll Tax", "Total Salary", "Status"], payrollData, tbfmt = "simple_grid") + "\n")
                print("-"*40 + f"\nTotal Salary Paid: RM {totalSalaryPaid:.2f}\n\nTotal Bonus Paid: RM {totalBonusPaid:.2f}\n\nTotal Payroll Tax Paid: RM {totalTaxPaid:.2f}\n" + "-"*40 + "\n")
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"Invalid input ☹️ : No records for payroll in {month} {year}")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def addPayroll():
    while True:
        try:
            payrollDict = rFunctions.readFile("payroll")
            print("\033c" + "Add New Payroll".center(40, "-") + "\n1. Basic Salary\n2. Bonus\n3. 🔙 Back\n" + "-"*40)
            payroll = input("Enter your selection: ").lower()
            if payroll.isdigit():
                payroll = int(payroll)
            if payroll in [1, "basic salary", "1. basic salary"]:
                while True:
                    payrollDict = rFunctions.readFile("payroll")
                    print("\033c" + "Add New Payroll".center(40, "-"))
                    yearMonth = []
                    for payroll in payrollDict["payrolls"]:
                        payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().month
                        payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().year
                        payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
                        yearMonth.append([payrollYear, payrollMonth]) if [payrollYear, payrollMonth] not in yearMonth else yearMonth
                    print("List of available Payrolls:\n" + rFunctions.tabulateGivenData(["Year", "Month"], yearMonth, tbfmt = "simple_grid"))
                    previousMonthInt = payrollMonthInt
                    previousYearInt = payrollYearInt
                    previousMonth, previousYear, _ = rFunctions.validMonthYear(previousMonthInt, previousYearInt)
                    if not rFunctions.askContinue():
                        break
                    if payrollMonthInt != 12:
                        monthInt = previousMonthInt + 1
                        yearInt = previousYearInt
                    elif payrollMonthInt == 12:
                        monthInt = 1
                        yearInt = previousYearInt + 1
                    month, year, _ = rFunctions.validMonthYear(monthInt, yearInt)
                    while True:
                        try:
                            print("\033c" + f"Add Basic Salary for {month} {year}".center(40, "-"))
                            bakers = []
                            cashiers = []
                            date = datetime.now().date()
                            for payroll in payrollDict["payrolls"]:
                                payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().month
                                payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().year
                                payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
                                if payrollMonth == previousMonth and payrollYear == previousYear:
                                    if payroll["position"].lower() == "baker" and payroll["category"].lower() == "salary":
                                        bakerBasicSalary = payroll["amount"]
                                        bakers.append(payroll["id"])
                                    if payroll["position"].lower() == "cashier" and payroll["category"].lower() == "salary":
                                        cashierBasicSalary = payroll["amount"]
                                        cashiers.append(payroll["id"])
                            print(f"""Bakers:\n{rFunctions.tabulateCsvData("baker", ["id", "name"], tbfmt = "simple_grid")}\nBasic Salary: {bakerBasicSalary}\n
Cashiers:\n{rFunctions.tabulateCsvData("cashier", ["id", "name"], tbfmt = "simple_grid")}\nBasic Salary: {cashierBasicSalary}\n""")
                            date = input("Enter due date for payroll payment [YYYY-MM-DD]: ")
                            date = datetime.strptime(date, "%Y-%m-%d").date()
                            currentDate = datetime.now().date()
                            ddMonth, ddYear, _ = rFunctions.validMonthYear(date.month, date.year)
                            if date.month < currentDate.month or date.year < currentDate.year or (date.month == currentDate.month and date.day < currentDate.day):
                                raise ValueError("Due date given is overdue.")
                            if [ddYear, ddMonth] in yearMonth:
                                raise ValueError(f"Due Date for {ddMonth} {ddYear} already exist.")
                            while True:
                                try:
                                    status = input("\nStatus for all Payroll Payment [paid/ unpaid]: ").lower()
                                    if status != "paid" and status != "unpaid":
                                        raise ValueError("Invalid Input ☹️ : Payroll status can only be paid or unpaid")
                                    break
                                except ValueError as vE:
                                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                                    time.sleep(2)
                                    rFunctions.clearPreviousLine()
                                    rFunctions.clearPreviousLine()
                            print()
                            bakerPayroll = []
                            cashierPayroll = []
                            for id in bakers:
                                bakerPayroll.append({"date": date, "category": "Salary", "position": "Baker", "id": id, "amount": bakerBasicSalary, "status": status.capitalize()})
                            for id in cashiers:
                                cashierPayroll.append({"date": date, "category": "Salary", "position": "Cashier", "id": id, "amount": cashierBasicSalary, "status": status.capitalize()})
                            confirm = input("Enter <YES> to save payroll records: ").lower()
                            if confirm != "yes":
                                print(f"\n{rFunctions.color('red', 'foreground')}Payroll records for {month} {year} is not updated ☹️{rFunctions.color('reset', None)}")
                            else:
                                for baker in bakerPayroll:
                                    rFunctions.appendFile("payroll", payrollDict, baker)
                                for cashier in cashierPayroll:
                                    rFunctions.appendFile("payroll", payrollDict, cashier)
                                print(f"\n{rFunctions.color('green', 'foreground')}Payroll records for {month} {year}is successfully updated 😄{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}Invalid Input ☹️ : {vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                    break
            elif payroll in [2, "bonus", "2. bonus"]:
                while True:
                    payrollDict = rFunctions.readFile("payroll")
                    bakersDict = rFunctions.readFile("baker")
                    cashierDict = rFunctions.readFile("cashier")
                    print("\033c" + "Add New Payroll".center(40, "-"))
                    yearMonthBonus = []
                    employeesBonus = []
                    for payroll in payrollDict["payrolls"]:
                        if payroll["category"].lower() == "bonus":
                            payrollMonthInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().month
                            payrollYearInt = datetime.strptime(payroll["date"], "%Y-%m-%d").date().year
                            payrollMonth, payrollYear, _ = rFunctions.validMonthYear(payrollMonthInt, payrollYearInt)
                            yearMonthBonus.append([payrollYear, payrollMonth]) if [payrollYear, payrollMonth] not in yearMonthBonus else yearMonthBonus
                            for baker in bakersDict["bakers"]:
                                if baker["id"] == payroll["id"]:
                                    employeeName = baker["name"]
                            for cashier in cashierDict["cashiers"]:
                                    if cashier["id"] == payroll["id"]:
                                        employeeName = cashier["name"]
                            employeesBonus.append([f"{payrollMonth} {payrollYear}", payroll["id"], employeeName, payroll["amount"]])
                    print("Employees with Bonuses: \n" + rFunctions.tabulateGivenData(["Month Year", "Employee ID", "Employee Name", "Bonus"], employeesBonus, tbfmt = "simple_grid") + "\n")
                    if not rFunctions.askContinue():
                        break
                    currentDate = datetime.now().date()
                    month, year, _ = rFunctions.validMonthYear(currentDate.month, currentDate.year)
                    if [month, year] in yearMonthBonus:
                        if currentDate.month != 12:
                            month, year, _ = rFunctions.validMonthYear((currentDate.month + 1), currentDate.year)
                        else:
                            month, year, _ = rFunctions.validMonthYear(1, (currentDate.year + 1))
                    while True:
                        try:
                            print("\033c" + f"Add New Bonus for {month} {year}".center(40, "-"))
                            print(f"""Bakers:\n{rFunctions.tabulateCsvData("baker", ["id", "name"], tbfmt = "simple_grid")}\n
Cashiers:\n{rFunctions.tabulateCsvData("cashier", ["id", "name"], tbfmt = "simple_grid")}\n""")
                            employeeId = input("Enter Employee ID to add bonus: ").upper()
                            if rFunctions.checkUniqueData("baker", "id", employeeId, bakersDict):
                                position = "Baker"
                            elif rFunctions.checkUniqueData("cashier", "id", employeeId, cashierDict):
                                position = "Cashier"
                            else:
                                raise ValueError(f"Invalid input ☹️ : Employee ID {employeeId} does not exist.")
                            rFunctions.clearPreviousLine()
                            print(f"Employee ID: {employeeId}\n")
                            bonus = input("Enter amount of bonus: ")
                            foundDigit = False
                            for i, char in enumerate(bonus):
                                if i == 0 and char.isdigit():
                                    foundDigit = True
                                    bonus = rFunctions.extractNumber(bonus)
                                    break
                                elif char.isdigit():
                                    foundDigit = True
                                    if bonus[i - 1] == "-":
                                        raise ValueError(f"Invalid input ☹️ : Bonus cannot be negative.")
                                    bonus = rFunctions.extractNumber(bonus)
                                    break
                            if not foundDigit:
                                raise ValueError(f"Invalid input ☹️ : Bonus has no value.")
                            if int(bonus) == 0:
                                raise ValueError(f"Invalid input ☹️ : Bonus cannot be zero.")
                            rFunctions.clearPreviousLine()
                            print(f"Bonus: RM {bonus:.2f}\n")
                            date = input("Enter due date [YYYY-MM-DD]: ")
                            date = datetime.strptime(date, "%Y-%m-%d").date()
                            currentDate = datetime.now().date()
                            ddMonth, ddYear, _ = rFunctions.validMonthYear(date.month, date.year)
                            if date.month < currentDate.month or date.year < currentDate.year or (date.month == currentDate.month and date.day < currentDate.day):
                                raise ValueError("Invalid Input ☹️ : Due date given is overdue.")
                            if [ddYear, ddMonth] in yearMonthBonus:
                                raise ValueError(f"Invalid Input ☹️ : Due Date for {ddMonth} {ddYear} already exist.")
                            rFunctions.clearPreviousLine()
                            print(f"Due Date: {date}\n")
                            status = input("Status for Bonus [paid/ unpaid]: ").lower()
                            if status != "paid" and status != "unpaid":
                                raise ValueError("Invalid Input ☹️ : Payroll status can only be paid or unpaid")
                            rFunctions.clearPreviousLine()
                            print(f"Bonus Status: {status.capitalize()}\n")
                            confirm = input("Enter <YES> to save bonus: ").lower()
                            if confirm != "yes":
                                print(f"\n{rFunctions.color('red', 'foreground')}Bonus for {employeeId} in {month} {year} is not added ☹️{rFunctions.color('reset', None)}")
                            else:
                                newBonus = {"date": date,
                                            "category": "Bonus",
                                            "position": position,
                                            "id": employeeId,
                                            "amount": f"RM{bonus:.2f}",
                                            "status": status.capitalize()}
                                rFunctions.appendFile("payroll", payrollDict, newBonus)
                                print(f"\n{rFunctions.color('green', 'foreground')}Bonus for {employeeId} in {month} {year} is successfully added 😄{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                    break
            elif payroll in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid Input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def updatePayroll():
    while True:
        try:
            payrollDict = rFunctions.readFile("payroll")
            bakersDict = rFunctions.readFile("baker")
            cashiersDict = rFunctions.readFile("cashier")
            print("\033c" + "Update Payroll Status".center(40, "-"))
            show = input("Enter <YES> to show unpaid payrolls: ").lower()
            rFunctions.clearPreviousLine()
            for category in ["salary", "bonus"]:
                bakerUnpaidPayrolls = []
                cashierUnpaidPayrolls = []
                for payroll in payrollDict["payrolls"]:
                    if payroll["category"].lower() == category:
                        if payroll["status"].lower() == "unpaid":
                            if payroll["position"].lower() == "baker":
                                for baker in bakersDict["bakers"]:
                                    if baker["id"] == payroll["id"]:
                                        bakerUnpaidPayrolls.append([payroll["id"], baker["name"], payroll["amount"], payroll["date"]])
                            if payroll["position"].lower() == "cashier":
                                for cashier in cashiersDict["cashiers"]:
                                    if cashier["id"] == payroll["id"]:
                                        cashierUnpaidPayrolls.append([payroll["id"], cashier["name"], payroll["amount"], payroll["date"]])
                if category == "salary":
                    salaryBaker = bakerUnpaidPayrolls
                    salaryCashier = cashierUnpaidPayrolls
                else:
                    bonusBaker = bakerUnpaidPayrolls
                    bonusCashier = cashierUnpaidPayrolls
                if show == "yes":
                    print(f"""{rFunctions.color('underline', None)}{category.capitalize()}{rFunctions.color('reset', None)}
Bakers:\n{rFunctions.tabulateGivenData(["Employee ID", "Employee Name", "Amount", "Due Date"], bakerUnpaidPayrolls, tbfmt = "simple_grid")}
\nCashiers:\n{rFunctions.tabulateGivenData(["Employee ID", "Employee Name", "Amount", "Due Date"], cashierUnpaidPayrolls, tbfmt = "simple_grid")}\n""")
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            while True:
                try:
                    employeeId = input("Enter Employee ID to <UPDATE> payroll status: ").upper()
                    if not rFunctions.checkUniqueData("payroll", "id", employeeId, payrollDict):
                        raise ValueError(f"Invalid input ☹️ : {employeeId} have no payroll records.")
                    foundId = False
                    salaryInfo = []
                    bonusInfo = []
                    for unpaidBaker in salaryBaker:
                        if employeeId == unpaidBaker[0]:
                            foundId = True
                            salaryInfo.append([["Position", "Baker"], ["Employee ID", unpaidBaker[0]], ["Employee Name", unpaidBaker[1]], ["Amount", unpaidBaker[2]], ["Due Date", unpaidBaker[3]]])
                            # break
                    for unpaidCashier in salaryCashier:
                        if employeeId == unpaidCashier[0]:
                            foundId = True
                            salaryInfo.append([["Position", "Cashier"], ["Employee ID", unpaidCashier[0]], ["Employee Name", unpaidCashier[1]], ["Amount", unpaidCashier[2]], ["Due Date", unpaidCashier[3]]])
                            # break
                    for unpaidBaker in bonusBaker:
                        if employeeId == unpaidBaker[0]:
                            foundId = True
                            bonusInfo.append([["Amount", unpaidBaker[2]], ["Due Date", unpaidBaker[3]]])
                            # break
                    for unpaidCashier in bonusCashier:
                        if employeeId == unpaidCashier[0]:
                            foundId = True
                            bonusInfo.append([["Amount", unpaidCashier[2]], ["Due Date", unpaidCashier[3]]])
                            # break
                    if not foundId:
                        raise ValueError(f"Invalid input ☹️ : Payroll for {employeeId} was paid.")
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            if bonusInfo == []:
                print("\033c" + "Update Payroll Status".center(40, "-") + "\n\nBasic Salary:\n")
                for info in salaryInfo:
                    print(rFunctions.tabulateGivenData(["Field", "Details"], info, tbfmt = "simple_grid") + "\n")
            elif salaryInfo == []:
                print("\033c" + "Update Payroll Status".center(40, "-") + "\n\nBonus:\n")
                for info in bonusInfo:
                    print(rFunctions.tabulateGivenData(["Field", "Details"], bonusInfo, tbfmt = "simple_grid") + "\n")
            else:
                print("\033c" + "Update Payroll Status".center(40, "-") + "\n\nBasic Salary:\n")
                for info in salaryInfo:
                    print(rFunctions.tabulateGivenData(["Field", "Details"], info, tbfmt = "simple_grid") + "\n")
                print("Bonus:\n")
                for info in bonusInfo:
                    print(rFunctions.tabulateGivenData(["Field", "Details"], info, tbfmt = "simple_grid") + "\n")
            while True:
                try:
                    category = input("Salary / Bonus: ").lower()
                    if bonusInfo == []:
                        if category == "bonus":
                            raise ValueError(f"Invalid Input ☹️ : Bonus for {employeeId} is not available or is paid.")
                    elif salaryInfo == []:
                        if category == "salary":
                            raise ValueError(f"Invalid Input ☹️ : Salary for {employeeId} is not available or is paid.")
                    if category != "salary" and category != "bonus":
                        raise ValueError("Invalid Input ☹️ : Type of payroll can only be salary or bonus.")
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            while True:
                try:
                    month, year = input("Enter month and year: ").split() #wiii
                    month, year, valid = rFunctions.validMonthYear(month, year)
                    if valid:
                        if category == "salary":
                            listOfDueYearMonth = []
                            for info in salaryInfo:
                                dueMonthInt = datetime.strptime(info[4][1], "%Y-%m-%d").month
                                dueYearInt = datetime.strptime(info[4][1], "%Y-%m-%d").year
                                dueMonth, dueYear, _ = rFunctions.validMonthYear(dueMonthInt, dueYearInt)
                                listOfDueYearMonth.append([dueYear, dueMonth])
                            if [year, month] not in listOfDueYearMonth:
                                raise ValueError(f"Invalid Input ☹️ : Payroll for {month} {year} does not exists or is paid.")
                        elif category == "bonus":
                            listOfDueYearMonth = []
                            for info in bonusInfo:
                                dueMonthInt = datetime.strptime(info[1][1], "%Y-%m-%d").month
                                dueYearInt = datetime.strptime(info[1][1], "%Y-%m-%d").year
                                dueMonth, dueYear, _ = rFunctions.validMonthYear(dueMonthInt, dueYearInt)
                                listOfDueYearMonth.append([dueYear, dueMonth])
                            if [year, month] not in listOfDueYearMonth:
                                raise ValueError(f"Invalid Input ☹️ : Payroll for {month} {year} does not exists or is paid.")
                        break
                    else:
                        continue
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            while True:
                try:
                    status = input("Status of Payroll [paid/ unpaid]: ").lower()
                    if status != "paid" and status != "unpaid":
                        raise ValueError("Invalid Input ☹️ : Payroll status can only be paid or unpaid.")
                    for payroll in payrollDict["payrolls"]:
                        if payroll["id"] == employeeId:
                            if payroll["category"].lower() == category:
                                if salaryInfo != [] and bonusInfo != []:
                                    for info in salaryInfo:
                                        dueMonthInt = datetime.strptime(info[4][1], "%Y-%m-%d").month
                                        dueYearInt = datetime.strptime(info[4][1], "%Y-%m-%d").year
                                        dueMonth, dueYear, _ = rFunctions.validMonthYear(dueMonthInt, dueYearInt)
                                        if dueMonth == month and dueYear == year:
                                            dates = info[4][1]
                                    for info in bonusInfo:
                                        dueMonthInt = datetime.strptime(info[1][1], "%Y-%m-%d").month
                                        dueYearInt = datetime.strptime(info[1][1], "%Y-%m-%d").year
                                        dueMonth, dueYear, _ = rFunctions.validMonthYear(dueMonthInt, dueYearInt)
                                        if dueMonth == month and dueYear == year:
                                            dates = info[1][1]
                                elif salaryInfo != []:
                                    for info in salaryInfo:
                                        dueMonthInt = datetime.strptime(info[4][1], "%Y-%m-%d").month
                                        dueYearInt = datetime.strptime(info[4][1], "%Y-%m-%d").year
                                        dueMonth, dueYear, _ = rFunctions.validMonthYear(dueMonthInt, dueYearInt)
                                        if dueMonth == month and dueYear == year:
                                            dates = info[4][1]
                                else:
                                    for info in bonusInfo:
                                        dueMonthInt = datetime.strptime(info[1][1], "%Y-%m-%d").month
                                        dueYearInt = datetime.strptime(info[1][1], "%Y-%m-%d").year
                                        dueMonth, dueYear, _ = rFunctions.validMonthYear(dueMonthInt, dueYearInt)
                                        if dueMonth == month and dueYear == year:
                                            dates = info[1][1]
                                if payroll["date"] == dates:
                                    payroll["status"] = status.capitalize()
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
            rFunctions.writeFile("payroll", payrollDict)
            print(f"{rFunctions.color('green', 'foreground')}Payroll status for {employeeId} is successfully updated 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

# Functionality 04: Inventory Control
def inventoryControl():
    while True:
            os.system('cls') #clear terminal
            print(f"""{rFunctions.color('bold', None)}{"-"*40 }
{"Inventory Control".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🥐 Estimated Product Expenses
2. 🖊️  Production Record
3. 📋 Product Availability Report
4. 📋 Inventory Report
5. ⏰ Update Inventory
6. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
            operation = input("Enter your selection: ")
            operation = int(operation) if operation.isdigit() else operation #if operation consists of all digits
            try:
                if operation in [1, "estimated product expenses"]:
                    estimatedProductExpenses()
                elif operation in [2, "production record", "2. production record"]:
                    sFunctions.displayProductionRecords()
                elif operation in [3, "production report", "3. production report"]:
                    sFunctions.productAvailability()
                elif operation in [4, "inventory report", "4. inventory report"]:
                    sFunctions.inventoryReport()
                elif operation in [5, "update inventory", "5. update inventory"]:
                    updateInventory()
                elif operation in [6, "back", "6. back"]:
                    break
                else:
                    raise ValueError(f"Invalid Input ☹️") #invalid input, trigger exception handling
            except ValueError as vE:
                print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2) #loop continues

def estimatedProductExpenses():
    while True:
        try:
            productsDict = rFunctions.readFile("product")
            projInDict = rFunctions.readFile("projected income")
            cogsDict = rFunctions.readFile("cogs")
            print("\033c" + rFunctions.color('bold', None) + "-"*40 + "\n" + "Estimated Product Expenses".center(40) + "\n" + "-"*40 + rFunctions.color('reset', None))
            categories = []
            for product in productsDict["products"]:
                categories.append(product["category"]) if product["category"] not in categories else categories
            yearMonth = []
            print("Available Month and Year:")
            for data in projInDict["projected incomes"]:
                if [data["year"], data["month"]] not in yearMonth:
                    yearMonth.append([data["year"], data["month"]])
            print(rFunctions.tabulateGivenData(header = ["Year", "Month"], data = yearMonth, tbfmt = "simple_grid"))
            month, year = input("Enter month and year: ").split()
            month, year, valid = rFunctions.validMonthYear(month, year)
            if valid and [year, month] in yearMonth:
                print("\033c" + rFunctions.color('bold', None) + "-"*40 + "\n" + "Estimated Product Expenses".center(40) + "\n" + "-"*40 + rFunctions.color('reset', None))
                showID = input("Enter <YES> to display all Product IDs: ").lower()
                rFunctions.clearPreviousLine()
                if showID == "yes":
                    print("List of Products:")
                    for category in categories:
                        products = []
                        print(f"{rFunctions.color('underline', None)}{category}{rFunctions.color('reset', None)}")
                        for product in productsDict["products"]:
                            products.append([product["id"], product["name"]]) if product["category"] == category else products
                        print(rFunctions.tabulateGivenData(["Product ID", "Name"], products, tbfmt = "simple_grid") + "\n")
                if not rFunctions.askContinue():
                    break
                while True:
                    try:
                        rFunctions.clearPreviousLine()
                        productId = input("Enter product ID: ").upper()
                        if not rFunctions.checkUniqueData("product", "id", productId, productsDict):
                            raise ValueError(f"Product ID '{id}' does not exists")
                        else: break
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', 'foreground')}Invalid input ☹️ : {vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                print("\033c" + rFunctions.color('bold', None) + "="*50 + "\n" + f"Estimated Ingredients Expenses for {month} {year}".center(50) + "\n" + "="*50 + rFunctions.color('reset', None))
                for product in productsDict["products"]:
                    if product["id"] == productId:
                        ingredients = []
                        productUnitBudget = 0.00
                        for ingredient in product["ingredients"].split(", "):
                            if any(char.isdigit() for char in ingredient): #wait shouldnt be not in kg cuz it will be like 2kg
                                if rFunctions.extractChar(ingredient.split()[len(ingredient.split()) - 1]) in ["kg", "g", "ml", "liter", "liters"] or (ingredient.split())[len(ingredient.split()) - 1].isdigit():
                                    ingredientQuantity = ingredient.rsplit(" ", 1) #here the sponge fingers 2 pack cannot
                                else:
                                    quantityWithUnit = ingredient.split()
                                    ingredientQuantity = [' '.join(quantityWithUnit[:len(quantityWithUnit) - 2]),
                                                        f"{quantityWithUnit[len(quantityWithUnit) - 2]} {quantityWithUnit[len(quantityWithUnit) - 1]}"] #change here le
                                quantity = rFunctions.extractNumber(ingredientQuantity[1])
                                for expenses in cogsDict["cogss"]:
                                    expMonthInt = datetime.strptime(expenses["date"], "%Y-%m-%d").month
                                    expYearInt = datetime.strptime(expenses["date"], "%Y-%m-%d").year
                                    expMonth, expYear, _ = rFunctions.validMonthYear(expMonthInt, expYearInt)
                                    if expYear == year and expMonth == month:
                                        if expenses["name"].lower() == ingredientQuantity[0].lower():
                                            ingredientPrice = rFunctions.extractNumber(expenses["amount"])
                                            boughtIngredientQuantity = rFunctions.extractNumber(expenses["quantity"])
                                            quantityUnits = rFunctions.extractChar(expenses["quantity"])
                                            if quantityUnits.lower() in ["kg", "liter", "liters"]:
                                                boughtIngredientQuantity *= 1000
                                            unitPrice = round(ingredientPrice/boughtIngredientQuantity, 2)
                                            totalIngredientPrice = round(quantity*unitPrice, 2)
                                            productUnitBudget += totalIngredientPrice
                                            ingredients.append([ingredientQuantity[0],
                                                                ingredientQuantity[1],
                                                                f"RM {unitPrice:.2f}",
                                                                f"RM {totalIngredientPrice:.2f}"]) #stopped here, the ingredients de unit nid to changeeeee!!!!!
                for projIn in projInDict["projected incomes"]:
                    if projIn["year"] == year and projIn["month"] == month and projIn["id"] == productId:
                        productName = projIn["name"]
                        forecastSalesVol = rFunctions.extractNumber(projIn["forecast sales volume"])
                print(f"""{"-"*40}\n
Product: {productName}\nForecasted Sales Volume: {int(forecastSalesVol)} units\n
{"-"*40}\n
{rFunctions.color('underline', None)}Required Ingredients and Expenses{rFunctions.color('reset', None)}\n
{rFunctions.tabulateGivenData(["Ingredients", "Amount", "Unit Price", "Total Ingredient Price"], ingredients, tbfmt = "outline")}""")
                print("\nEstimated Budget for One Unit: RM %.2f"%(productUnitBudget) + "\nEstimated Total Budget: RM %.2f"%(productUnitBudget*forecastSalesVol) + "\n")
                time.sleep(2)
                if not rFunctions.askContinue():
                    break
            elif not valid:
                continue
            elif [year, month] not in yearMonth:
                raise ValueError(f"No records for projected income in {month} {year}")
            time.sleep(2)
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}Invalid input ☹️ : {vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def updateInventory():
    while True:
        try:
            os.system('cls') #clear terminal
            print(f"""{rFunctions.color('bold', None) }{"Update Inventory".center(40, "-")}{rFunctions.color('reset', None)}
1. 🥐 Products
2. 🧂 Ingredients
3. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
            operation = input("Enter your selection: ").lower()
            if operation.isdigit():
                operation = int(operation)
            if operation in [1, "products", "1. products"]:
                sFunctions.recipeManagement()
            elif operation in [2, "ingredients", "2. ingredients"]:
                ingredientManagement()
            elif operation in [3, "back", "3. back"]:
                break
            else:
                raise ValueError(f"Invalid Input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def ingredientManagement():
    while True:
        try:
            print("\033c" + rFunctions.color('bold', None) + "Update Ingredients".center(40, "-") + rFunctions.color('reset', None) + "\n1. ➕ Restock Ingredients\n2. 🔧 Modify Ingredient Details\n3. 🗑️  Remove Ingredients\n4. 🔙 Back\n" + "-"*40)
            functionality = input("Enter your selection: ").lower()
            if functionality.isdigit():
                functionality = int(functionality)
            if functionality in [1, "restock ingredients", "1. restock ingredients"]:
                restockIngredients()
            elif functionality in [2, "modify ingredient details", "2. modify ingredient details"]:
                modifyIngredients()
            elif functionality in [3, "remove ingredients", "3. remove ingredients"]:
                removeIngredients()
            elif functionality in [4, "back", "4. back"]:
                break
            else:
                raise ValueError(f"Invalid Input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def restockIngredients():
    while True:
        try:
            inventoriesDict = rFunctions.readFile("inventorie")
            cogsDict = rFunctions.readFile("cogs")
            print("\033c" + "Bought New Ingredients".center(40, "-"))
            showIngredients = input("Enter <YES> to show all available ingredients: ").lower()
            rFunctions.clearPreviousLine()
            if showIngredients == "yes":
                categories = []
                ingredients = []
                for ingredient in inventoriesDict["inventories"]:
                    categories.append(ingredient["category"]) if ingredient["category"] not in categories else categories
                for category in categories:
                    ingredients = []
                    index = 0
                    for ingredient in inventoriesDict["inventories"]:
                        if ingredient["category"] == category:
                            index += 1
                            ingredients.append((index, ingredient["name"]))
                    print(f"{rFunctions.color('underline', None)}{category}{rFunctions.color('reset', None)}\n" + rFunctions.tabulateGivenData(["No", "Name"], ingredients, tbfmt = "simple_grid") + "\n")
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            ingredientName = input("Enter ingredient name: ").title()
            sameIngredient = False
            if ingredientName.lower() in [ingredient["name"].lower() for ingredient in inventoriesDict["inventories"]]:
                sameIngredient = True
            rFunctions.clearPreviousLine()
            if sameIngredient == True:
                print("\033c" + "Add Existing Ingredients to Inventory".center(40, "-"))
                for ingredient in inventoriesDict["inventories"]:
                    if ingredient["name"].lower() == ingredientName.lower():
                        ingredientDetails = [[key.capitalize(), value] for key, value in ingredient.items() if key in ["category", "name", "bought quantity", "threshold quantity", "available quantity"]]
                print("\nIngredient Details:\n" + rFunctions.tabulateGivenData(["Field", "Details"], ingredientDetails, tbfmt = "simple_grid"))
                print(f"\n{rFunctions.color('underline', None)}If need to update ingredient details{rFunctions.color('reset', None)}")
                askModify = input("Enter <YES> to modify ingredient details:").lower()
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
                if askModify != "yes":
                    for expenses in cogsDict["cogss"]:
                        if expenses["name"].lower() == ingredientName.lower():
                            expensesDetail = expenses
                    expensesDetail["date"] = datetime.now().date()
                    for ingredient in inventoriesDict["inventories"]:
                        if ingredient["name"].lower() == ingredientName.lower():
                            boughtUnit= rFunctions.extractChar(ingredient["bought quantity"])
                            availableUnit = rFunctions.extractChar(ingredient["available quantity"])
                            if boughtUnit in ["kg", "liter", "liter"]:
                                ingredient["available quantity"] = f"{(rFunctions.extractNumber(ingredient["available quantity"]) + rFunctions.extractNumber(ingredient["bought quantity"])):.1f}{availableUnit}"
                            elif boughtUnit in ["g", "ml"]:
                                ingredient["available quantity"] = f"{int(rFunctions.extractNumber(ingredient["available quantity"]) + rFunctions.extractNumber(ingredient["bought quantity"]))}{availableUnit}"
                            else:
                                ingredient["available quantity"] = f"{int(rFunctions.extractNumber(ingredient["available quantity"]) + rFunctions.extractNumber(ingredient["bought quantity"]))} {availableUnit}"
                    rFunctions.appendFile("cogs", cogsDict, expensesDetail)
                    rFunctions.writeFile("inventorie", inventoriesDict)
                    for msg in ["Inventory is updated 😄", f"Available quantity of {ingredientName} is updated 😄", "COGS Expenses are recorded 😄"]:
                        print(f"{rFunctions.color('green', 'foreground')}{msg}{rFunctions.color('reset', None)}")
                        time.sleep(1.5)
                        rFunctions.clearPreviousLine()
                else:
                    rFunctions.clearPreviousLine()
                    print(f"{rFunctions.color('blue', 'foreground')}Can only modify{rFunctions.color('bold', None)} Threshold Quantity, Bought Quantity, Price, and, Suppliers{rFunctions.color('reset', None)}\n")
                    while True:
                        try:
                            modify = input("Enter what to modify: ").lower()
                            rFunctions.clearPreviousLine()
                            if modify not in ["threshold quantity", "bought quantity", "price", "suppliers"]:
                                raise ValueError(f"Invalid Input ☹️ : {modify} cannot be modified")
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine()
                    while True:
                        try:
                            for expenses in cogsDict["cogss"]:
                                if expenses["name"].lower() == ingredientName.lower():
                                    newExpenses = expenses
                            for ingredient in inventoriesDict["inventories"]:
                                if ingredient["name"].lower() == ingredientName.lower():
                                    if modify == "suppliers":
                                        newExpenses["suppliers"] = input(f"Enter new ingredient suppliers: ").title()
                                    elif modify in ["threshold quantity", "bought quantity"]:
                                        newQuantity = input(f"Enter new ingredient {modify} (with units): ")
                                        foundDigit = False
                                        for i, char in enumerate(newQuantity):
                                            if i == 0 and char.isdigit():
                                                foundDigit = True
                                                break
                                            elif char.isdigit():
                                                foundDigit = True
                                                if newQuantity[i - 1] == "-":
                                                    raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be negative")
                                        if foundDigit:
                                            if int(rFunctions.extractNumber(newQuantity)) == 0:
                                                raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be zero")
                                        else:
                                            raise ValueError(f"Invalid Input ☹️ :No ingredient quantity is given")
                                        newUnit = rFunctions.extractChar(newQuantity)
                                        availableUnit = rFunctions.extractChar(ingredient["available quantity"])
                                        if newUnit != availableUnit:
                                            raise ValueError(f"Invalid Input ☹️ :Ingredient quantity unit must be in {availableUnit}")
                                        if modify == "threshold quantity":
                                            if newUnit in ["kg", "liters", "liter", "g", "ml"]:
                                                ingredient["threshold quantity"] = f"{rFunctions.extractNumber(newQuantity):.1f}{newUnit}"
                                            else:
                                                ingredient["threshold quantity"] = newQuantity
                                        elif modify == "bought quantity":
                                            availableQuantity = rFunctions.extractNumber(ingredient["available quantity"]) + rFunctions.extractNumber(newQuantity)
                                            if availableUnit in ["kg", "liters", "liter", "g", "ml"]:
                                                ingredient["available quantity"] = f"{availableQuantity:.1f}{availableUnit}"
                                                newExpenses["quantity"] = newQuantity.replace(" ", "")
                                                ingredient["bought quantity"] = newQuantity.replace(" ", "")
                                            else:
                                                ingredient["available quantity"] = f"{int(availableQuantity)} {availableUnit}"
                                                newExpenses["quantity"] = newQuantity
                                                ingredient["bought quantity"] = newQuantity
                                            rFunctions.clearPreviousLine()
                                            changePrice = input("Enter <YES> to change price: ").lower()
                                            rFunctions.clearPreviousLine()
                                            if changePrice == "yes":
                                                newPrice = input("Enter new ingredient price: ")
                                                foundDigit = False
                                                for i, char in enumerate(newPrice):
                                                    if i == 0 and char.isdigit():
                                                        foundDigit = True
                                                        newPrice = rFunctions.extractNumber(newPrice)
                                                        break
                                                    elif char.isdigit():
                                                        foundDigit = True
                                                        if newPrice[i - 1] == "-":
                                                            raise ValueError(f"Invalid Input ☹️ :Ingredient price cannot be negative")
                                                        newPrice = rFunctions.extractNumber(newPrice)
                                                        break
                                                if foundDigit:
                                                    if int(newPrice) == 0:
                                                        raise ValueError(f"Invalid Input ☹️ :Ingredient price cannot be zero")
                                                else:
                                                    raise ValueError(f"Invalid Input ☹️ :Ingredient price not given")
                                                newExpenses["amount"] = f"RM{newPrice:.2f}"
                                            else:
                                                print()
                                    elif modify == "price":
                                        newPrice = input("Enter new ingredient price: ")
                                        foundDigit = False
                                        for i, char in enumerate(newPrice):
                                            if i == 0 and char.isdigit():
                                                foundDigit = True
                                                newPrice = rFunctions.extractNumber(newPrice)
                                                break
                                            elif char.isdigit():
                                                foundDigit = True
                                                if newPrice[i - 1] == "-":
                                                    raise ValueError(f"Invalid Input ☹️ :Ingredient price cannot be negative")
                                                newPrice = rFunctions.extractNumber(newPrice)
                                                break
                                        if foundDigit:
                                            if int(newPrice) == 0:
                                                raise ValueError(f"Invalid Input ☹️ :Ingredient price cannot be zero")
                                        else:
                                            raise ValueError(f"Invalid Input ☹️ :Ingredient price not given")
                                        newExpenses["amount"] = f"RM{newPrice:.2f}"
                                    newExpenses["date"] = datetime.now().date()
                                    if modify != "bought quantity":
                                        availableQuantity = rFunctions.extractNumber(ingredient["available quantity"]) + rFunctions.extractNumber(ingredient["bought quantity"])
                                        availableUnit = rFunctions.extractChar(ingredient["available quantity"])
                                        if availableUnit in ["kg", "liters", "liter", "g", "ml"]:
                                            ingredient["available quantity"] = f"{availableQuantity:.1f}{availableUnit}"
                                        else:
                                            ingredient["available quantity"] = f"{int(availableQuantity)} {availableUnit}"
                            rFunctions.clearPreviousLine()
                            rFunctions.appendFile("cogs", cogsDict, newExpenses)
                            rFunctions.writeFile("inventorie", inventoriesDict)
                            for msg in ["Inventory is updated 😄", f"Available quantity of {ingredientName} is updated 😄", "COGS Expenses are recorded 😄"]:
                                print(f"{rFunctions.color('green', 'foreground')}{msg}{rFunctions.color('reset', None)}")
                                time.sleep(1.5)
                                rFunctions.clearPreviousLine()
                            break
                        except ValueError as vE:
                            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                            time.sleep(2)
                            rFunctions.clearPreviousLine()
                            rFunctions.clearPreviousLine()
            elif sameIngredient == False:
                while True:
                    try:
                        print("\033c" + "Add New Ingredients to Inventory".center(40, "-"))
                        print(f"Name: {ingredientName}\n")
                        category = input("Enter ingredient category: ").title()
                        rFunctions.clearPreviousLine()
                        print(f"Category: {category}\n")
                        boughtQuantity = input("Enter bought ingredient quantity (with units): ")
                        foundDigit = False
                        for i, char in enumerate(boughtQuantity):
                            if i == 0 and char.isdigit():
                                foundDigit = True
                                break
                            elif char.isdigit():
                                foundDigit = True
                                if boughtQuantity[i - 1] == "-":
                                    raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be negative")
                        if foundDigit:
                            if int(rFunctions.extractNumber(boughtQuantity)) == 0:
                                raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be zero")
                        else:
                            raise ValueError(f"Invalid Input ☹️ :No ingredient quantity given")
                        rFunctions.clearPreviousLine()
                        if rFunctions.extractChar(boughtQuantity) in ["kg", "liter", "liters", "g", "ml"]:
                            boughtQuantity = boughtQuantity.replace(" ", "")
                        print(f"Bought Quantity (with units): {boughtQuantity}\n")
                        amount = input("Enter ingredient price (RM): ")
                        foundDigit = False
                        for i, char in enumerate(amount):
                            if i == 0 and char.isdigit():
                                foundDigit = True
                                amount = rFunctions.extractNumber(amount)
                                break
                            elif char.isdigit():
                                foundDigit = True
                                if amount[i - 1] == "-":
                                    raise ValueError(f"Invalid Input ☹️ :Product price cannot be negative")
                                amount = rFunctions.extractNumber(amount)
                        if foundDigit:
                            if int(amount) == 0:
                                raise ValueError(f"Invalid Input ☹️ :Ingredient price cannot be zero")
                        else:
                            raise ValueError(f"Invalid Input ☹️ :No ingredient price given")
                        rFunctions.clearPreviousLine()
                        print(f"Price: RM {amount:.2f}\n")
                        thresholdQuantity = input("Enter threshold quantity of ingredient (with units): ")
                        foundDigit = False
                        for i, char in enumerate(thresholdQuantity):
                            if i == 0 and char.isdigit():
                                foundDigit = True
                                break
                            elif char.isdigit():
                                foundDigit = True
                                if thresholdQuantity[i - 1] == "-":
                                    raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be negative")
                        if foundDigit:
                            if int(rFunctions.extractNumber(thresholdQuantity)) == 0:
                                raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be zero")
                        else:
                            raise ValueError(f"Invalid Input ☹️ :No ingredient quantity given")
                        rFunctions.clearPreviousLine()
                        if rFunctions.extractChar(thresholdQuantity) != rFunctions.extractChar(boughtQuantity):
                            raise ValueError(f"Invalid Input ☹️ :Ingredient quantity unit must be in {rFunctions.extractChar(boughtQuantity)}")
                        if rFunctions.extractChar(thresholdQuantity) in ["kg", "liter", "liters", "g", "ml"]:
                            thresholdQuantity = f"{rFunctions.extractNumber(thresholdQuantity):.1f}{rFunctions.extractChar(thresholdQuantity)}"
                        print(f"Threshold Quantity: {thresholdQuantity}\n")
                        supplier = input("Enter supplier of ingredient: ").title()
                        rFunctions.clearPreviousLine()
                        print(f"Supplier: {supplier}\n")
                        date = datetime.now().date()
                        print(f"Date Updated: {date}\n")
                        newIngredient = {"category": category,
                                        "name": ingredientName,
                                        "bought quantity": boughtQuantity,
                                        "threshold quantity": thresholdQuantity,
                                        "available quantity": boughtQuantity}
                        newIngredientExpenses = {"date": date,
                                                "category": category,
                                                "name": ingredientName,
                                                "quantity": boughtQuantity,
                                                "amount": f"RM {amount:.2f}",
                                                "suppliers": supplier}
                        time.sleep(2)
                        print("\033c" + "Add New Ingredients to Inventory".center(40, "-"))
                        newIngredientDetails = [(key.capitalize(), value) for key, value in newIngredient.items()]
                        newIngredientExpensesDetails = []
                        for key, value in newIngredientExpenses.items():
                            if key == "date":
                                newIngredientExpensesDetails.append(("Last Purchased", value))
                            elif key == "amount":
                                newIngredientExpensesDetails.append(("Prize", value))
                            elif key == "suppliers":
                                newIngredientExpensesDetails.append(("Suppliers", value))
                        print(f"""Ingredient Details:\n{rFunctions.tabulateGivenData(["Field", "Details"], newIngredientDetails, tbfmt = "simple_grid")}\n
Ingredient Expenses:\n{rFunctions.tabulateGivenData(["Field", "Details"], newIngredientExpensesDetails, tbfmt = "simple_grid")}""")
                        confirm = input("Enter <CONFIRM> to Save Ingredient: ").lower()
                        rFunctions.clearPreviousLine()
                        if confirm != "confirm":
                            print(f"{rFunctions.color('red', 'foreground')}Ingredient '{ingredientName}' is not saved ☹️{rFunctions.color('reset', None)}")
                        else:
                            rFunctions.appendFile("inventorie", inventoriesDict, newIngredient)
                            rFunctions.appendFile("cogs", cogsDict, newIngredientExpenses)
                            print(f"{rFunctions.color('green', 'foreground')}Product '{ingredientName}' is successfully saved 😄{rFunctions.color('reset', None)}")
                        time.sleep(2)
                        rFunctions.clearPreviousLine()
                        break
                    except ValueError as vE:
                        print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                        time.sleep(2)
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def modifyIngredients():
    while True:
        try:
            inventoriesDict = rFunctions.readFile("inventorie")
            cogsDict = rFunctions.readFile("cogs")
            print("\033c" + "Modify Existing Ingredients Details".center(40, "-"))
            showIngredients = input("Enter <YES> to show all available ingredients: ").lower()
            rFunctions.clearPreviousLine()
            if showIngredients == "yes":
                categories = []
                ingredients = []
                for ingredient in inventoriesDict["inventories"]:
                    categories.append(ingredient["category"]) if ingredient["category"] not in categories else categories
                for category in categories:
                    ingredients = []
                    index = 0
                    for ingredient in inventoriesDict["inventories"]:
                        if ingredient["category"] == category:
                            index += 1
                            ingredients.append((index, ingredient["name"]))
                    print(f"{rFunctions.color('underline', None)}{category}{rFunctions.color('reset', None)}\n" + rFunctions.tabulateGivenData(["No", "Name"], ingredients, tbfmt = "simple_grid") + "\n")
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            while True:
                try:
                    ingredientName = input("Enter ingredient name: ").lower()
                    if ingredientName not in [ingredient["name"].lower() for ingredient in inventoriesDict["inventories"]]:
                        raise ValueError(f"Invalid Input ☹️ : {ingredientName.title()} not found")
                    rFunctions.clearPreviousLine()
                    for ingredient in inventoriesDict["inventories"]:
                        if ingredient["name"].lower() == ingredientName:
                            ingredientDetails = [(key.capitalize(), value) for key, value in ingredient.items()]
                            for expenses in cogsDict["cogss"]:
                                if expenses["name"].lower() == ingredientName:
                                    expensesDetails = [("Last Purchased", expenses["date"]), ("Price", expenses["amount"]), ("Suppliers", expenses["suppliers"])]
                                    break
                    print("\033c" + "Modify Existing Ingredients Details".center(40, "-"))
                    print(f"""Ingredient Details:\n{rFunctions.tabulateGivenData(["Field", "Details"], ingredientDetails, tbfmt = "simple_grid")}\n
Expenses Details:\n{rFunctions.tabulateGivenData(["Field", "Details"], expensesDetails, tbfmt = "simple_grid")}""")
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            print(f"{rFunctions.color('blue', 'foreground')}Can only modify{rFunctions.color('bold', None)} Category, Threshold Quantity{rFunctions.color('reset', None)}\n")
            while True:
                try:
                    modify = input("Enter what to modify: ").lower()
                    if modify not in ["category", "threshold quantity"]:
                        raise ValueError(f"Invalid Input ☹️ : {modify} cannot be modified")
                    rFunctions.clearPreviousLine()
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            while True:
                try:
                    for ingredient in inventoriesDict["inventories"]:
                        if ingredient["name"].lower() == ingredientName.lower():
                            if modify == "category":
                                ingredient["category"] = input("Enter new ingredient category: ").title()
                            elif modify in ["threshold quantity", "bought quantity"]:
                                newQuantity = input(f"Enter new ingredient threshold quantity (with units): ")
                                foundDigit = False
                                for i, char in enumerate(newQuantity):
                                    if i == 0 and char.isdigit():
                                        foundDigit = True
                                        break
                                    elif char.isdigit():
                                        foundDigit = True
                                        if newQuantity[i - 1] == "-":
                                            raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be negative")
                                if foundDigit:
                                    if int(rFunctions.extractNumber(newQuantity)) == 0:
                                        raise ValueError(f"Invalid Input ☹️ :Ingredient quantity cannot be zero")
                                else:
                                    raise ValueError(f"Invalid Input ☹️ :No ingredient quantity is given")
                                newUnit = rFunctions.extractChar(newQuantity)
                                availableUnit = rFunctions.extractChar(ingredient["available quantity"])
                                if newUnit != availableUnit:
                                    raise ValueError(f"Invalid Input ☹️ :Ingredient quantity unit must be in {availableUnit}")
                                if newUnit in ["kg", "liters", "liter", "g", "ml"]:
                                    ingredient["threshold quantity"] = f"{rFunctions.extractNumber(newQuantity):.1f}{availableUnit}"
                                else:
                                    ingredient["threshold quantity"] = newQuantity
                    rFunctions.clearPreviousLine()
                    rFunctions.writeFile("inventorie", inventoriesDict)
                    print(f"{rFunctions.color('green', 'foreground')}Ingredient {modify} is updated successfully 😄{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def removeIngredients():
    while True:
        try:
            inventoriesDict = rFunctions.readFile("inventorie")
            cogsDict = rFunctions.readFile("cogs")
            print("\033c" + "Remove Existing Ingredients".center(40, "-"))
            showIngredients = input("Enter <YES> to show all available ingredients: ").lower()
            rFunctions.clearPreviousLine()
            if showIngredients == "yes":
                categories = []
                ingredients = []
                for ingredient in inventoriesDict["inventories"]:
                    categories.append(ingredient["category"]) if ingredient["category"] not in categories else categories
                for category in categories:
                    ingredients = []
                    index = 0
                    for ingredient in inventoriesDict["inventories"]:
                        if ingredient["category"] == category:
                            index += 1
                            ingredients.append((index, ingredient["name"]))
                    print(f"{rFunctions.color('underline', None)}{category}{rFunctions.color('reset', None)}\n" + rFunctions.tabulateGivenData(["No", "Name"], ingredients, tbfmt = "simple_grid") + "\n")
            if not rFunctions.askContinue():
                break
            rFunctions.clearPreviousLine()
            while True:
                try:
                    ingredientName = input("Enter ingredient name: ").lower()
                    if ingredientName not in [ingredient["name"].lower() for ingredient in inventoriesDict["inventories"]]:
                        raise ValueError(f"Invalid Input ☹️ : {ingredientName.title()} not found")
                    rFunctions.clearPreviousLine()
                    for i, ingredient in enumerate(inventoriesDict["inventories"]):
                        if ingredient["name"].lower() == ingredientName:
                            ingredientDict = ingredient #nid??
                            ingredientDetails = [[key.capitalize(), value] for key, value in ingredient.items() if key in ["category", "name", "bought quantity", "threshold quantity", "available quantity"]]
                            del inventoriesDict["inventories"][i]
                    for expenses in cogsDict["cogss"]:
                        if expenses["name"].lower() == ingredientName:
                            expensesDetails = [("Last Purchased", expenses["date"]), ("Price", expenses["amount"]), ("Suppliers", expenses["suppliers"])]
                    break
                except ValueError as vE:
                    print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
                    time.sleep(2)
                    rFunctions.clearPreviousLine()
                    rFunctions.clearPreviousLine()
            print("\033c" + "Remove Existing Ingredient".center(40, "-"))
            print(f"""Ingredient Details:\n{rFunctions.tabulateGivenData(["Field", "Details"], ingredientDetails, tbfmt = "simple_grid")}\n
Expenses Details:\n{rFunctions.tabulateGivenData(["Field", "Details"], expensesDetails, tbfmt = "simple_grid")}""")
            confirm = input("Enter <CONFIRM> to Delete Ingredient: ").lower()
            rFunctions.clearPreviousLine()
            if confirm != "confirm":
                print(f"{rFunctions.color('red', 'foreground')}Ingredient '{ingredientName}' is not deleted ☹️{rFunctions.color('reset', None)}")
            else:
                rFunctions.writeFile("inventorie", inventoriesDict)
                print(f"{rFunctions.color('green', 'foreground')}Ingredient '{ingredientName}' is successfully deleted 😄{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            if not rFunctions.askContinue():
                break
        except ValueError as vE:
            print(f"{rFunctions.color('red', "foreground")}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

# Functionality 05: Equipment Management
def equipmentManagement():
    while True:
        os.system('cls') #clear terminal
        malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction") #read malfunction equipment report data
        #to determine number of unresolved malfunction equipment reports
        unresolved = 0
        for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
            if equipment["status"] == "Unresolved" or equipment["status"] == "In Progress":
                unresolved += 1
        if unresolved != 0: #to display number of reports in red
            unresolved = f"{rFunctions.color('red', 'foreground')}{unresolved}{rFunctions.color('reset', None)}"
        else:
            unresolved = "" #to display nothing
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"Equipment Management".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 🍽️  Display Equipments
2. 🗓️  Monthly Equipment Report
3. 📋 Equipment Malfunction Report {unresolved}
4. 🔙 Back
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit(): #if functionality consists of all digits
                functionality = int(functionality)
            if functionality in [1, "display equipments", "1. display equipments"]:
                sFunctions.displayEquipment()
            elif functionality in [2, "monthly equipment report", "2. monthly equipment report"]:
                sFunctions.displayEquipmentReport()
            elif functionality in [3, "equipment malfunction report", "3. equipment malfunction report"]:
                equipmentMalfunctionReport()
            elif functionality in [4, "back", "4. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️") #invalid input, trigger error handling
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2) #loop continues

def equipmentMalfunctionReport():
    while True:
        malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction")
        unresolved = 0
        for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
            if equipment["status"] == "Unresolved" or equipment["status"] == "In Progress":
                unresolved += 1
        if unresolved != 0:
            unresolved = f"[{rFunctions.color('red', 'foreground')}{unresolved}{rFunctions.color('reset', None)} unresolved malfunction report(s)]"
        else:
            unresolved = f"[{rFunctions.color('green', 'foreground')}{unresolved}{rFunctions.color('reset', None)} unresolved malfunction report(s)]"
        print(f"""\033c{rFunctions.color('bold', None)}{"-"*40}
{"Equipment Malfunction Report".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 📋 Display Report
2. ✅ Resolve Malfunction
3. 🔙 Back
{unresolved}
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit():
                functionality = int(functionality)
            if functionality in [1, "display report", "1. display report"]:
                resolve, malfunctionId = displayMalfunctionReport()
                if resolve:
                    resolveMalfunction(malfunctionId)
            elif functionality in [2, "resolve malfunction", "2. resolve malfunction"]:
                resolveMalfunctionNoId()
            elif functionality in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def displayMalfunctionReport():
    while True:
        malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction")
        unresolved = 0
        for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
            if equipment["status"] == "Unresolved" or equipment["status"] == "In Progress":
                unresolved += 1
        if unresolved != 0:
            unresolved = f"[{rFunctions.color('red', 'foreground')}{unresolved}{rFunctions.color('reset', None)} unresolved malfunction report(s)]"
        else:
            unresolved = f"[{rFunctions.color('green', 'foreground')}{unresolved}{rFunctions.color('reset', None)} unresolved malfunction report(s)]"
        print(f"""\033c{rFunctions.color('bold', None)}{"-"*40}
{"Display Equipment Malfunction Report".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
1. 📋 Display All Reports
2. ❌ Display Unresolved Reports
3. 🔙 Back
{unresolved}
{rFunctions.color('bold', None)}{"-"*40}{rFunctions.color('reset', None)}""")
        functionality = input("Enter selection: ").lower()
        try:
            if functionality.isdigit():
                functionality = int(functionality)
            if functionality in [1, "display all reports", "1. display all reports"]:
                while True:
                    sFunctions.displayMalfunctionReport()
                    time.sleep(2)
                    if not rFunctions.askContinue():
                        break
            elif functionality in [2, "display unresolved reports", "2. display unresolved reports"]:
                resolve, malfunctionId = displayUnresolvedReports()
                if resolve:
                    return resolve, malfunctionId
            elif functionality in [3, "back", "3. back"]:
                return False, None
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)

def displayUnresolvedReports():
    while True:
        try:
            malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction")
            equipmentsDict = rFunctions.readFile("equipment")
            bakersDict = rFunctions.readFile("baker")
            print("\033c" + rFunctions.color('bold', None) + "-"*40 + "\n" + "Display Unresolved Malfunction Report".center(40) + "\n" + "-"*40 + rFunctions.color('reset', None))
            #malfunctionID,report date,eqid,bakerID,issue,urgency level,status,resolution date,resolution comments
            urgencyLevel = []
            for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
                urgencyLevel.append(equipment["urgency level"]) if equipment["urgency level"] not in urgencyLevel and equipment["status"] != "Resolved" else urgencyLevel
            malfunctionIds = []
            for level in urgencyLevel:
                unresolvedReports = []
                for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
                    if equipment["urgency level"] == level:
                        if equipment["status"] == "Unresolved" or equipment["status"] == "In Progress":
                            malfunctionIds.append(equipment["malfunctionID"])
                            for item in equipmentsDict["equipments"]:
                                if item["eqid"] == equipment["eqid"]:
                                    equipmentName = item["eqname"]
                                    break
                            unresolvedReports.append([equipment["malfunctionID"], equipment["eqid"], equipmentName])
                if level == "High":
                    color = rFunctions.color('red', 'foreground')
                elif level == "Medium":
                    color = rFunctions.color('magenta', 'foreground')
                elif level == "Low":
                    color = rFunctions.color('yellow', 'foreground')
                print(f"Urgency Level: {color}{level}{rFunctions.color('reset', None)}\n" + rFunctions.tabulateGivenData(["Report ID", "Equipment ID", "Equipment Name"], unresolvedReports, tbfmt = "simple_grid") + "\n")
            malfunctionId = input("Enter Report ID to view malfunction report: ").upper()
            if malfunctionId not in malfunctionIds:
                raise ValueError(f"Invalid input ☹️ : Malfunction Report ID '{malfunctionId}' does not exists or has been resolved.")
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
    for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
        if equipment["malfunctionID"] == malfunctionId:
            for item in equipmentsDict["equipments"]:
                if item["eqid"] == equipment["eqid"]:
                    equipmentId = item["eqid"]
                    equipmentName = item["eqname"]
                    break
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
    print(f"""\033c{rFunctions.color('underline', None)}Malfunction Report for {equipmentId}:{rFunctions.color('reset', None)}\n
{rFunctions.tabulateGivenData(["Field", "Details"], malfunctionTable, tbfmt = "simple_grid", align = ("left", "left"))}\n""")
    time.sleep(2)
    resolve = input("Enter <YES> to proceed to resolve report: ").lower()
    if resolve == "yes":
        return True, malfunctionId
    else:
        return False, None

def resolveMalfunctionNoId():
    while True:
        while True:
            try:
                malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction")
                equipmentsDict = rFunctions.readFile("equipment")
                print("\033c" + rFunctions.color('bold', None) + "-"*40 + "\n" + "Display Unresolved Malfunction Report".center(40) + "\n" + "-"*40 + rFunctions.color('reset', None))
                urgencyLevel = []
                for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
                    urgencyLevel.append(equipment["urgency level"]) if equipment["urgency level"] not in urgencyLevel and equipment["status"] != "Resolved" else urgencyLevel
                malfunctionIds = []
                for level in urgencyLevel:
                    unresolvedReports = []
                    for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
                        if equipment["urgency level"] == level:
                            if equipment["status"] == "Unresolved" or equipment["status"] == "In Progress":
                                malfunctionIds.append(equipment["malfunctionID"])
                                for item in equipmentsDict["equipments"]:
                                    if item["eqid"] == equipment["eqid"]:
                                        equipmentName = item["eqname"]
                                        break
                                unresolvedReports.append([equipment["malfunctionID"], equipment["eqid"], equipmentName])
                    if level == "High":
                        color = rFunctions.color('red', 'foreground')
                    elif level == "Medium":
                        color = rFunctions.color('magenta', 'foreground')
                    elif level == "Low":
                        color = rFunctions.color('yellow', 'foreground')
                    print(f"Urgency Level: {color}{level}{rFunctions.color('reset', None)}\n" + rFunctions.tabulateGivenData(["Report ID", "Equipment ID", "Equipment Name"], unresolvedReports, tbfmt = "simple_grid") + "\n")
                if not rFunctions.askContinue():
                    return
                rFunctions.clearPreviousLine()
                malfunctionId = input("Enter Report ID to view malfunction report: ").upper()
                if malfunctionId not in malfunctionIds:
                    raise ValueError(f"Invalid input ☹️ : Malfunction Report ID '{malfunctionId}' does not exists or has been resolved.")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
        resolveMalfunction(malfunctionId)
        if not rFunctions.askContinue():
            break

def resolveMalfunction(malfunctionId: str):
    malfunctionEquipmentsDict = rFunctions.readFile("equipment malfunction")
    equipmentsDict = rFunctions.readFile("equipment")
    print(f"\033c{rFunctions.color('bold', None)}{"="*40}\n{"Malfunction Report".center(40)}\n{"="*40}{rFunctions.color('reset', None)}")
    for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
        if equipment["malfunctionID"] == malfunctionId:
            for item in equipmentsDict["equipments"]:
                if item["eqid"] == equipment["eqid"]:
                    equipmentId = item["eqid"]
                    equipmentName = item["eqname"]
                    break
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
            reportDate = equipment["report date"]
            bakersDict = rFunctions.readFile("baker")
            for baker in bakersDict["bakers"]:
                if baker["id"] == equipment["bakerID"]:
                    bakerId = baker["id"]
                    bakerName = baker["name"]
                    break
    malfunctionTable = [(key, value) for key, value in equipmentData.items()]
    print(f"""\033c{rFunctions.color('underline', None)}Malfunction Report for {equipmentId}:{rFunctions.color('reset', None)}\n
Reported by: {bakerId} {bakerName}
Report Date: {reportDate}
{rFunctions.tabulateGivenData(["Field", "Details"], malfunctionTable, tbfmt = "simple_grid", align = ("left", "left"))}\n""")
    rFunctions.clearPreviousLine()
    while True:
        try:
            status = input("Enter resolution status: ").title()
            if status not in ["Resolved", "In Progress"]:
                raise ValueError("Invalid input ☹️ : Resolution Status can either be 'Resolved' or 'In Progress'.")
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
    while True:
        try:
            if status == "Resolved":
                resolutionDate = datetime.now().date()
            else:
                resolutionDate = ""
                nextMaintenance = input("Enter Next Maintenance Date [YYYY-MM-DD]: ")
                nextMaintenanceDate = datetime.strptime(nextMaintenance, "%Y-%m-%d").date()
                _, _, valid = rFunctions.validMonthYear(nextMaintenanceDate.month, nextMaintenanceDate.year)
                dateCondition1 = nextMaintenanceDate.year < datetime.now().year
                dateCondition2 = nextMaintenanceDate.year == datetime.now().year and nextMaintenanceDate.month < datetime.now().month
                dateCondition3 = nextMaintenanceDate.year == datetime.now().year and nextMaintenanceDate.month == datetime.now().month and nextMaintenanceDate.day < datetime.now().day
                if not valid:
                    continue
                elif dateCondition1 or dateCondition2 or dateCondition3:
                    raise ValueError("Maintenance Date cannot be in the past.")
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}Invalid input ☹️ : {vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
    while True:
        try:
            comment = input("Enter resolution comment: ").replace(",", ", ").replace(",  ", ", ")
            if comment.strip() == "":
                raise ValueError("Invalid input ☹️ : Resolution comment cannot be left blank.")
            break
        except ValueError as vE:
            print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
            time.sleep(2)
            rFunctions.clearPreviousLine()
            rFunctions.clearPreviousLine()
    for equipment in malfunctionEquipmentsDict["equipment malfunctions"]:
        if equipment["malfunctionID"] == malfunctionId:
            equipment["status"] = status
            equipment["resolution date"] = resolutionDate
            equipment["resolution comments"] = comment
            if status == "Resolved":
                color = rFunctions.color('green', 'foreground')
            else:
                color = rFunctions.color('yellow', 'foreground')
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
    print(f"""\033c{rFunctions.color('underline', None)}Malfunction Report for {equipmentId}:{rFunctions.color('reset', None)}\n
Reported by: {bakerId} {bakerName}
Report Date: {reportDate}
{rFunctions.tabulateGivenData(["Field", "Details"], malfunctionTable, tbfmt = "simple_grid", align = ("left", "left"))}\n""")
    confirm = input("Enter <YES> to confirm: ").lower()
    rFunctions.clearPreviousLine()
    if confirm == "yes":
            for equipment in equipmentsDict["equipments"]:
                if equipment["eqid"] == equipmentId:
                    if status == "Resolved":
                        equipment["status"] = "Operational"
                        equipment["next_maintenance"] = ""
                    elif status == "In Progress":
                        equipment["status"] = "Under Maintenance"
                        equipment["next_maintenance"] = nextMaintenanceDate
                    equipment["last_maintenance"] = resolutionDate
            rFunctions.writeFile("equipment", equipmentsDict)
            rFunctions.writeFile("equipment malfunction", malfunctionEquipmentsDict)
            print(f"{rFunctions.color('green', 'foreground')}Equipment Malfunction Report for {equipmentId} is successfully reported 😄{rFunctions.color('reset', None)}")
    else:
        print(f"{rFunctions.color('red', 'foreground')}Equipment Malfunction Report for {equipmentId} is not reported ☹️{rFunctions.color('reset', None)}")
    time.sleep(2)
    rFunctions.clearPreviousLine()

# Functionality 06: Customer Feedback
def viewCustomerFeedback():
    while True:
        productsDict = rFunctions.readFile("product") #read products data
        os.system('cls') #clear terminal
        print(f"""{rFunctions.color('bold', None)}{"-"*40}
{"View Customer Feedback".center(40)}
{"-"*40}{rFunctions.color('reset', None)}
List of Products:""")
        #get categories of product
        categories = []
        for product in productsDict["products"]:
            categories.append(product["category"]) if product["category"] not in categories else categories
        #get product based on category
        for category in categories:
            products = []
            for product in productsDict["products"]:
                if product["category"] == category:
                    products.append([product["id"], product["name"]])
            #display category and all of its products
            print(f"{category}:\n{rFunctions.tabulateGivenData(["Product ID", "Name"], products, tbfmt = "simple_grid")}\n")
        if not rFunctions.askContinue():
            break
        rFunctions.clearPreviousLine()
        while True:
            productsDict = rFunctions.readFile("product") #read products data
            reviewsDict = rFunctions.readFile("review") #read product reviews data
            customersDict = rFunctions.readFile("customer") #read customer data
            try:
                productId = input("Enter Product ID: ").upper()
                if not rFunctions.checkUniqueData("product", "id", productId, productsDict):
                    raise ValueError(f"Invalid input ☹️ : Product ID {productId} does not exist.")
                #get review and ratings
                reviewList, totalRating = [], 0
                for reviews in reviewsDict["reviews"]:
                    for review in eval(reviews["products"]):
                        if review[0] == productId:
                            productName = review[1]
                            #get customer username
                            for customer in customersDict["customers"]:
                                if customer["id"] == reviews["userID"]:
                                    reviewList.append([customer["username"], review[3], review[2]])
                                    totalRating += int(review[2])
                #display all ratings and reviews of the product, with customer username
                print(f"""\033c{rFunctions.color('bold', None)}{"="*40}
{f"Ratings and Reviews on {productName}".center(40) }
{"="*40}{rFunctions.color('reset', None)}\n""")
                print(f"""{rFunctions.tabulateGivenData(["Customer Username", "Review", "Rating (1 - 5)"], reviewList, tbfmt = "fancy_grid")}
Overall Rating: {float(totalRating/len(reviewList)):.1f} ⭐\n""")
                break
            except ValueError as vE:
                print(f"{rFunctions.color('red', 'foreground')}{vE}{rFunctions.color('reset', None)}")
                time.sleep(2)
                rFunctions.clearPreviousLine()
                rFunctions.clearPreviousLine()
        if not rFunctions.askContinue():
            break
