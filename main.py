# import custom_modules.reusableFunctions as rFunctions
from custom_modules.reusableFunctions import readFile, color, appendFile, assignId, validData, checkLogin, checkUniqueData, clearPreviousLine, askContinue
from os import system
from time import sleep
from manager import managerPage
from cashier import cashierPage
from baker import bakerPage
from customer import customerHomePage

#02 Exit Program
def endProgram():
    system('cls')
    print("Thank You for Visiting 😄" + "\n" + " Exiting program...")
    exit()

#(B) Login: Worker Login
def staffLogin(roleNum: int, role: str):
    incorrect = 0
    while True:
        cashiersDict = readFile("cashier")
        bakersDict = readFile("baker")
        system('cls')
        try:
            if (roleNum in range(1,4)):
                print(f"{color('bold', None)}" + "="*40 + "\n" + f"{role.capitalize()} Login Page".center(40) + "\n" + "="*40 + f"{color('reset', None)}")
                username = input("Enter username: ")
                password = input("Enter password: ")
                validLogin = False
                if roleNum == 1:
                    if username == "manager_05" and password == "Mng_UCDF2309":
                        return managerPage(username)
                    elif username !=  "manager_M05":
                        raise ValueError("Invalid username ☹️")
                    else:
                        raise ValueError("Invalid password ☹️")
                if roleNum in [2, 3]:
                    if roleNum == 2:
                        checkUsername, checkPassword = checkLogin(role, username, password, cashiersDict)
                    elif roleNum == 3:
                        checkUsername, checkPassword = checkLogin(role, username, password, bakersDict)
                    if checkUsername and checkPassword:
                        validLogin = True
                    elif not checkUsername:
                        raise ValueError("Invalid username ☹️")
                    else:
                        raise ValueError("Invalid password ☹️")
                    if validLogin == True and roleNum == 2:
                        return cashierPage(username)
                    elif validLogin == True and roleNum == 3:
                        return bakerPage(username)
            else:
                raise ValueError(f"Error: Role number {roleNum} is out of range: roleNum -> 1, 2, 3")
        except ValueError as vE:
            incorrect += 1
            print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
            sleep(2)
            if incorrect == 3:
                clearPreviousLine()
                print()
                if not askContinue():
                    break

#(C) Customer Login: Sign in
def customerLoginPage():
    incorrect = 0
    while True:
        customersDict = readFile("customer")
        system('cls')
        print(f"{color('bold', None)}" + "="*40 + "\n" + "Customer Login Page".center(40) + "\n" + "="*40 + f"{color('reset', None)}")
        print("1. Sign In\n2. Sign Up\n3. Back\n" + "-"*40)
        login = input("Enter selection: ").lower()
        if login.isdigit():
            login = int(login)
        try:
            if login in [1, "sign in", "1. sign in"]:
                invalidLogin = 0
                while True:
                    try:
                        system('cls')
                        print(f"{color('bold', None)}" + "="*40 + "\n" + "Customer Login Page".center(40) + "\n" + "="*40 + f"{color('reset', None)}")
                        username = input("Enter username: ")
                        password = input("Enter password: ")
                        checkUsername, checkPassword = checkLogin("customer", username, password, customersDict)
                        if checkUsername and checkPassword:
                            sleep(1)
                            print(f"{color('green', 'foreground')}Login successfully 😄{color('reset', None)}")
                            sleep(1)
                            return customerHomePage(username)
                        elif not checkUsername:
                            raise ValueError("Invalid username ☹️")
                        else:
                            raise ValueError("Invalid password ☹️")
                    except ValueError as vE:
                        invalidLogin += 1
                        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
                        sleep(2)
                        if invalidLogin == 3:
                            clearPreviousLine()
                            print()
                            if not askContinue():
                                break
            elif login in [2, "sign up", "2. sign up"]:
                registerAccount()
            elif login in [3, "back", "3. back"]:
                break
            else:
                raise ValueError("Invalid input ☹️")
        except ValueError as vE:
            incorrect += 1
            print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
            sleep(2)

#(C) Customer Login: Sign Up
def registerAccount():
    while True:
        customersDict = readFile("customer")
        system('cls')
        print(f"{color('bold', None)}" + "="*40 + "\n" + "Customer Registration Page".center(40) + "\n" + "="*40 + f"{color('reset', None)}")
        try:
            idNum = assignId("customer", customersDict)
            name = input("Enter name: ").title()
            username = input("Enter username: ")
            if checkUniqueData("customer", "username", username, customersDict):
                raise ValueError(f"Username '{username}' is used ☹️\n" + "Please Try Again...")
            errorMsg, validUsername = validData(username = username)
            if not validUsername:
                raise ValueError(f"{errorMsg} ☹️")
            password = input("\nEnter password: ")
            errorMsg, validPassword = validData(password = password)
            if not validPassword:
                raise ValueError(f"{errorMsg} ☹️")
            age = int(input("\nEnter age: "))
            if age <= 0:
                raise ValueError(f"Age cannot be zero or negative ☹️")
            gender = input("\nEnter gender: ").capitalize()
            errorMsg, validGender = validData(gender = gender)
            if not validGender:
                raise ValueError(f"{errorMsg} ☹️")
            phoneNum = input("\nEnter phone number (01X-XXX XXXX): ")
            errorMsg, validPhoneNum = validData(phoneNumber = phoneNum)
            if not validPhoneNum:
                raise ValueError(f"{errorMsg} ☹️")
            email = input("\nEnter email: ")
            errorMsg, validEmail = validData(email = email)
            if not validEmail:
                raise ValueError(f"{errorMsg} ☹️")
            address = input("\nEnter address: ")
            newCustomer = {"id": idNum, "name": name, "username": username, "password": password, "age": age, "gender": gender, "phone number": phoneNum, "email": email, "address": address}
            appendFile("customer", customersDict, newCustomer)
            customersDict = readFile("customer")
            print(f"{color('green', 'foreground')}{username} is registered successfully 😄{color('reset', None)}")
            sleep(2)
            break
        except ValueError as vE:
            print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
            sleep(2)
            clearPreviousLine()
            print()
            if not askContinue():
                break

#(A) Start of program
#01 Start: Select role
while True:
    system('cls')
    print(f"{color('bold', None)}" + "="*40 + "\n" + "Select Role".center(40) + "\n" + "="*40 + f"{color('reset', None)}" + "\n1. 💼 Manager" + "\n" + "2. 📠 Cashier" + "\n" + "3. 🥐 Baker" + "\n" + "4. 🍴 Customer" + "\n" + "5. 🔚 Exit Program" + "\n" + "-"*40)
    role = input("Enter selection: ").lower()
    try:
        if role.isdigit():
            role = int(role)
        if role in [1, "manager", "1. manager"]:
            staffLogin(1, "manager")
        elif role in [2, "cashier", "2. cashier"]:
            staffLogin(2, "cashier")
        elif role in [3, "baker", "3. baker"]:
            staffLogin(3, "baker")
        elif role in [4, "customer", "4. customer"]:
            customerLoginPage()
        elif role in [5, "exit program", "5. exit program"]:
            endProgram()
        else:
            raise ValueError("Invalid input ☹️")
    except ValueError as vE:
        print(f"{color('red', 'foreground')}{vE}{color('reset', None)}")
        if askContinue():
            pass
        else:
            endProgram()