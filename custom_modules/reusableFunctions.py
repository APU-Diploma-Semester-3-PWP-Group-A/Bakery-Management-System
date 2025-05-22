#Reusable function
from sys import stdout
from time import sleep
from tabulate import tabulate
from datetime import datetime

#01 ask to continue program
def askContinue():
    while True:
        askContinue = input("Enter 1 to <CONTINUE> or 0 to <EXIT>: ")
        try:
            if not askContinue.isdigit():
                raise ValueError("Invalid Input :(" + "\n" + "Please Try Again...")
            if int(askContinue) == 1:
                return True
            elif int(askContinue) == 0:
                return False
            else:
                raise ValueError("Invalid Input :(" + "\n" + "Please Try Again...")
        except ValueError as vE:
            print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
            sleep(2)
            clearPreviousLine()
            clearPreviousLine()
            clearPreviousLine()

def clearPreviousLine():
    # Move the cursor up one line
    stdout.write("\033[F")
    # Clear the current line
    stdout.write("\033[K")
    stdout.flush()

def validMonthYear(month, year):
    try:
        valid = True
        if isinstance(month, int) or month.isdigit():
            month = int(month)
            if month < 1 or month > 12:
                raise ValueError("Invalid Input ☹️ : invalid month entered")
            if isinstance(year, int) or year.isdigit():
                year = int(year)
                if year <= 0:
                    raise ValueError("Invalid Input ☹️ : invalid year entered")
            else:
                raise ValueError("Invalid Input ☹️ : invalid year entered")
            month = datetime(year, month, 1).strftime('%B').capitalize()
        else:
            if month.lower() not in ["january", "february", "march", "april", "may",
                                    "june", "july", "august", "september", "october", "november", "december"]:
                raise ValueError("Invalid Input ☹️ : invalid month entered")
            month = month.capitalize()
        return str(month), str(year), valid
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
        sleep(2)
        clearPreviousLine()
        valid = False
        return None, None, valid

def extractNumber(string: str):
    return float("".join(char for char in string if char.isdigit() or char == "."))

def extractChar(string: str):
    return str("").join(char for char in string if char.isalpha())


def assignId(role: str, dataDict: dict):
    ids = []
    if role in ["customer", "cashier", "baker", "product", "product record"]:
        for user in dataDict[f"{role}s"]:
            ids.append(user["id"])
    elif role == "cart":
        cartIds = []
        ordersDict = readFile("order")
        for cart in ordersDict["orders"]:
            cartIds.append(cart["cartID"])
        for cart in dataDict["carts"]:
            cartIds.append(cart["cartID"])
    elif role == "equipment":
        for user in dataDict[f"{role}s"]:
            ids.append(user["eqid"])
    elif role == "order":
        for order in dataDict["orders"]:
            ids.append(order["orderID"])
    elif role == "equipment report":
        for equipment in dataDict[f"{role}s"]:
            ids.append(equipment["reportID"])
    elif role == "equipment malfunction":
        for equipment in dataDict[f"{role}s"]:
            ids.append(equipment["malfunctionID"])
    if role == "customer":
        idInitials = "UID"
    elif role == "cashier":
        idInitials = "EMPC"
    elif role == "baker":
        idInitials = "EMPB"
    elif role == "product":
        idInitials = "RC"
    elif role == "cart":
        idInitials = "CAID"
    elif role == "order":
        idInitials = "OID"
    elif role == "equipment":
        idInitials = "E"
    elif role == "equipment report":
        idInitials = "R"
    elif role == "equipment malfunction":
        idInitials = "M"
    elif role == "product record":
        idInitials = "B"
    if role != "cart":
        newIdNum = f"{idInitials}{str(len(ids) + 1).zfill(3)}"
    elif role == "cart":
        newIdNum = f"{idInitials}{str(len(cartIds) + 1).zfill(3)}"
    return newIdNum


def checkUniqueData(role: str, type: str, data: str,dataDict: dict):
    try:
        validRole = ["cashier", "baker", "customer", "product", "cart", "cogs", "loan", "operating", "payroll",
                    "taxe", "order", "equipment", "product record", "equipment report", "equipment malfunction"]
        validType = ["id", "username", "email", "orderID", "eqid", "batch_num", "malfunctionID", "reportID"]
        if role not in validRole:
            raise ValueError(f"Invalid variable type for 'role': valid variables are {', '.join(validRole)}")
        elif type not in validType:
            raise ValueError(f"Invalid variable type for 'type': valid variables are {', '.join(validType)}")
        if data in [value[type] for value in dataDict[f"{role}s"]]:
            return True
        else:
            return False
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")

def checkLogin(role: str, username: str, password: str, dataDict: dict):
    try:
        validRole = ["cashier", "baker", "customer"]
        if role not in validRole:
            raise Exception(f"Invalid variable type for 'role': valid variables are {', '.join(validRole)}")
        verifiedUsername = False
        verifiedPassword = False
        for user in dataDict[f"{role}s"]:
            if username == user["username"]:
                verifiedUsername = True
                if password == user["password"]:
                    verifiedPassword = True
        return verifiedUsername, verifiedPassword
    except Exception as E:
        print(f"{color('red', 'foreground')}{E}{color('reset', None)}")

def validData(username: str = '', password: str = '', gender: str = '', phoneNumber: str = '', email: str = ''):
    if username != "":
        if not username[0].isalnum() or not username[len(username) - 1].isalnum():
            return f"Username cannot start or end with special characters.", False
        else:
            return None, True
    elif password != "":
        if len(password) < 8:
            return "Password must contain at least 8 characters.", False
        elif password.isalpha() or password.isnumeric():
            return "Password must contain both letters and numbers.", False
        elif "".join(char for char in password if char.isalpha()).isupper() or "".join(char for char in password if char.isalpha()).islower():
            return "Password must contain both uppercase and lowercase letters.", False
        else:
            return None, True
    elif gender != "":
        if gender.lower() not in ["male", "female"]:
            return "Gender can only be Male or Female.", False
        else:
            return None, True
    elif phoneNumber != "":
        lenPhoneCode = len(phoneNumber[:phoneNumber.find("-")])
        lenSubscriberNum = len(phoneNumber[phoneNumber.find("-") + 1:])
        areaCode = phoneNumber[(phoneNumber.find("-") - 1)]
        charAlpha = False
        for char in phoneNumber:
            charAlpha = True if char.isalpha() else charAlpha
        if charAlpha:
            return "Phone Number consist of only digits.", False
        elif not phoneNumber.startswith("0"):
            return "Phone Number must be in this format '01X-XXX XXXX' or '011-XXXX XXXX' or '03-XXXX XXXX' or 08X-XXX XXX' or '0X-XXX XXXX'.", False
        elif lenPhoneCode < 2 or lenPhoneCode > 3:
            return "Phone Area Code in Malaysia have 1 - 2 digits.", False
        elif lenPhoneCode == 2 and phoneNumber[(phoneNumber.find("-") - 1)] not in ["3", "4", "5", "6", "7"]:
            return "Invalid Phone Number Area Code.", False
        elif lenPhoneCode == 3 and phoneNumber[(phoneNumber.find("-") - 2)] != "1" and phoneNumber[(phoneNumber.find("-") - 2): (phoneNumber.find("-"))] not in ["82", "88"]:
            return "Invalid Phone Number Area Code.", False
        elif lenPhoneCode == 3 and phoneNumber[(phoneNumber.find("-") - 2)] != "1" and phoneNumber[(phoneNumber.find("-") - 2)] != "8":
            return "Phone Number must be in this format '01X-XXX XXXX' or '011-XXXX XXXX' or '03-XXXX XXXX' or 08X-XXX XXX' or '0X-XXX XXXX'.", False
        elif areaCode == "0":
            return "Phone Area Code in Malaysia does not hav 0.", False
        elif lenSubscriberNum < 7 or lenSubscriberNum > 8:
            return "Phone Subscriber Number in Malaysia only have 7 - 8 digits.", False
        else:
            return None, True
    elif email != "":
        if not email[0].isalnum():
            return "Email cannot start with special characters.", False
        elif not email.endswith(".com"):
            return "Email must end with '.com'.", False
        elif "@" not in email:
            return "Email must include '@'.", False
        elif email.find("@") == (email.find(".com") - 1):
            return "Email is missing a domain.", False
        else:
            return None, True
    elif username == '' and password == '' and gender == '' and phoneNumber == '' and email == '':
        return "No data is provided.", False


def getFilePath(role: str):
    try:
        validRole = ["cashier", "baker", "customer", "product",
                    "cart", "order", "projected income", "cogs",
                    "loan", "operating", "payroll", "taxe", "inventorie",
                    "tax rate", "review", "equipment", "product record", "equipment report", "equipment malfunction"]
        if role not in validRole:
            raise ValueError(f"Invalid variable type for 'role': valid variables are {', '.join(validRole)}")
        if role == "customer":
            return "Database\\customer\\customerDetails.csv"
        elif role == "cashier":
            return "Database\\userDetails\\cashierDetails.csv"
        elif role == "baker":
            return "Database\\userDetails\\bakerDetails.csv"
        elif role == "product":
            return "Database\\productDetails\\bakerProducts.csv"
        elif role == "cart":
            return "Database\\customer\\customerCart.csv"
        elif role == "order":
            return "Database\\customer\\customerOrder.csv"
        elif role == "projected income":
            return "Database\\financialDetails\\projectedIncome.csv"
        elif role == "cogs":
            return "Database\\financialDetails\\expensesDetails\\cogsExpenses.csv"
        elif role == "loan":
            return "Database\\financialDetails\\expensesDetails\\miscellaneousLoan.csv"
        elif role == "operating":
            return "Database\\financialDetails\\expensesDetails\\operatingExpenses.csv"
        elif role == "payroll":
            return "Database\\financialDetails\\expensesDetails\\payrollExpenses.csv"
        elif role == "taxe":
            return "Database\\financialDetails\\expensesDetails\\taxes.csv"
        elif role == "inventorie":
            return "Database\\productDetails\\inventory.csv"
        elif role == "tax rate":
            return "Database\\financialDetails\\expensesDetails\\taxRates.csv"
        elif role == "review":
            return "Database\\customer\\productReview.csv"
        elif role == "equipment":
            return "Database\\equipment\\equipment.csv"
        elif role == "equipment report":
            return "Database\\equipment\\equipmentReport.csv"
        elif role == "equipment malfunction":
            return "Database\\equipment\\equipmentMalfunction.csv"
        elif role == "product record":
            return "Database\\productDetails\\productRecord.csv"
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")

def readFile(role: str):
    try:
        validRole = ["cashier", "baker", "customer", "product",
                    "cart", "order", "projected income", "cogs",
                    "loan", "operating", "payroll", "taxe", "inventorie",
                    "tax rate", "review", "equipment", "product record",
                    "product quantitie", "equipment report", "equipment malfunction"]
        if role not in validRole:
            raise ValueError(f"Invalid variable type for 'role': valid variables are {', '.join(validRole)}")
        filePath = getFilePath(role)
        listOfDict = []
        keys = []
        with open(filePath, mode = 'r', encoding = 'utf-8', newline = '') as file:
            for i, line in enumerate(file):
                if i == 0:
                    keys = line.split(",")
                    if "\r" or "\n" in keys[len(keys) - 1]:
                        keys[len(keys) - 1] = keys[len(keys) - 1].replace("\r", "")
                        keys[len(keys) - 1] = keys[len(keys) - 1].replace("\n", "")
                else:
                    if len(line.split(",")) > 1:
                        data = line.split(",")
                        listOfTuples = []
                        if "\r" or "\n" in data[len(data) - 1]:
                            data[len(data) - 1] = data[len(data) - 1].replace("\r", "")
                            data[len(data) - 1] = data[len(data) - 1].replace("\n", "")
                        for key in keys:
                            if key in ["address", "description", "ingredients", "instructions", "allergen info", "products", "flavour", "product_specification", "comments", "issue", "resolution comments"]:
                                data[keys.index(key)] = data[keys.index(key)].replace("-", ", ")
                        for num in range(len(keys)):
                            listOfTuples.append((keys[num], data[num]))
                        dictionary = dict(listOfTuples)
                        listOfDict.append(dictionary)
        dataDict = {f"{role}s": listOfDict}
        return dataDict
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")

def writeFile(role: str, dataDict: dict):
    try:
        validRole = ["cashier", "baker", "customer", "product",
                    "cart", "order", "projected income", "cogs",
                    "loan", "operating", "payroll", "taxe", "inventorie",
                    "tax rate", "review", "equipment", "product record",
                    "product quantitie", "equipment report", "equipment malfunction"]
        if role not in validRole:
            raise ValueError(f"Invalid variable type for 'role': valid variables are {', '.join(validRole)}")
        keys = [key for key, _ in dataDict[f"{role}s"][0].items()]
        filePath = getFilePath(role)
        with open(filePath, mode = 'w', encoding = 'utf-8', newline = '') as file:
            file.write(','.join(map(str, keys)) + "\n")
            for data in dataDict[f"{role}s"]:
                values = []
                for key, value in data.items():
                    if key in ["address", "promotion", "description", "ingredients", "instructions", "allergen info", "products", "flavour", "product_specification", "comments", "issue", "resolution comments"]:
                        value = value.replace(", ", "-")
                    values.append(value)
                file.write(','.join(map(str, values)) + "\n")
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")

def appendFile(role: str, dataDict: dict, dataAppend: dict):
    try:
        validRole = ["cashier", "baker", "customer", "product",
                    "cart", "order", "projected income", "cogs",
                    "loan", "operating", "payroll", "taxe", "inventorie",
                    "tax rate", "review", "equipment", "product record",
                    "product quantitie", "equipment report", "equipment malfunction"]
        if role not in validRole:
            raise Exception(f"Invalid variable type for 'role': valid variables are {', '.join(validRole)}")
        filePath = getFilePath(role)
        with open(filePath, mode = 'a', encoding = 'utf-8', newline = '') as file:
            values = []
            for key, value in dataAppend.items():
                if key in ["address", "promotion", "description", "ingredients", "instructions", "allergen info", "products", "flavour", "product_specification", "comments", "issue", "resolution comments"]:
                    value = value.replace(", ", "-")
                values.append(value)
            file.write(",".join(map(str, values)) + "\n")
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")

def tabulateGivenData(header: list, data: list, tbfmt: str, align: tuple = ()):
    return tabulate(data, headers = header, tablefmt = tbfmt, colalign = align)

def tabulateCsvData(role: str, dataDisplay: list, tbfmt: str, align: tuple = (), headerName: list = ''):
    try:
        validRole = ["cashier", "baker", "customer", "product",
                    "cart", "order", "projected income", "cogs",
                    "loan", "operating", "payroll", "taxe", "inventorie",
                    "tax rate", "review", "equipment", "product record",
                    "product quantitie", "equipment report", "equipment malfunction"]
        if role not in validRole:
            raise ValueError(f"Invalid variable type for 'role': valid variables are {', '.join(validRole)}")
        listOfList = []
        dataDict = readFile(role)
        for data in dataDict[f"{role}s"]:
            dataRow = []
            for header in dataDisplay:
                for key, value in data.items():
                    if key == header:
                        dataRow.append(value)
            listOfList.append(dataRow)
        if headerName != '' and len(headerName) == len(dataDisplay):
            dataDisplay = headerName
        return tabulate(listOfList, dataDisplay, tablefmt = tbfmt, colalign = align)
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")

def color(colors: str, type):
    try:
        if colors.lower() == "reset" and type == None:
            return "\033[0m"
        elif colors.lower() == "bold" and type == None:
            return "\033[1m"
        elif colors.lower() == "underline" and type == None:
            return "\033[4m"
        elif colors.lower() == "red" and type == "foreground":
            return "\033[31m"
        elif colors.lower() == "green" and type == "foreground":
            return "\033[32m"
        elif colors.lower() == "yellow" and type == "foreground":
            return "\033[33m"
        elif colors.lower() == "blue" and type == "foreground":
            return "\033[34m"
        elif colors.lower() == "magenta" and type == "foreground":
            return "\033[35m"
        elif colors.lower() == "cyan" and type == "foreground":
            return "\033[36m"
        else:
            raise ValueError("Invalid input :( : invalid argument 'color' or 'type' passed.")
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
