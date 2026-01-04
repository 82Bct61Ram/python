
def check_pass(password):
    score = 0

    if len(password) >= 8:
        score +=1

    # Check for uppercase letter
    for ch in password:
        if ord(ch) >= 65 and ord(ch) <= 90:
            score = score + 1
            break

    # Check for lowercase letter
    for ch in password:
        if ord(ch)>=97 and ord(ch)<=122:
            score = score + 1
            break

    # Check for digit
    for ch in password:
        if ord(ch)>=48 and ord(ch)<=57:
            score = score + 1
            break
    # check for special characters
    for ch in password:
        if ord(ch) >= 33 and ord(ch) <= 47 or  ord(ch) >= 58 and ord(ch) <= 64 or ord(ch) >= 91 and ord(ch) <= 96:
            score+=1
            break

    return score


def login_system():
    username = "Ram"
    password = "IamPython#0"

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == username and password == password:
        print("Login Successful ✅")
    else:
        print("Invalid username or password ❌")


while True:
    print("1. Check Password Strength")
    print("2. Login System")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        pwd = input("Enter password: ")
        strength = check_pass(pwd)

        if strength == 5:
            print("Password Strength: STRONG (5/5)")
        elif strength == 4:
            print("Password Strength: GOOD (4/5)")
        elif strength == 3:
            print("Password Strength:moderate (3/5)")
        elif strength == 2:
            print("Password Strength: WEAK (2/5)")    
        else:
            print("Password Strength: VERY WEAK (1/4)")

    elif choice == "2":
        login_system()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
