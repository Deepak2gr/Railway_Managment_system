# RAILWAY MANAGEMENT SYSTEM (Updated with Update Feature)

# Importing Modules
import mysql.connector as sql
from random import randint

# Establishment of connection to MySQL Server
print("Enter the details of your MySQL Server:")
x = input("Hostname: ")
y = input("User: ")
z = input("Password: ")

con = sql.connect(host=x, user=y, password=z)
con.autocommit = True
cur = con.cursor()

# Database and Table Setup
cur.execute("CREATE DATABASE IF NOT EXISTS IRCTC;")
cur.execute("USE IRCTC;")

cur.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INT PRIMARY KEY,
    pass VARCHAR(16),
    name VARCHAR(100),
    sex CHAR(1),
    age VARCHAR(3),
    dob DATE,
    ph_no CHAR(10)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INT,
    PNR INT,
    train VARCHAR(25),
    doj DATE,
    tfr VARCHAR(100),
    tto VARCHAR(100)
);
""")


# ====================== LOGIN MENU ======================
def login_menu():
    print("\nWELCOME TO THE IRCTC PORTAL")
    print("1. Create New Account")
    print("2. Log In")
    print("3. Exit")

    opt = int(input("Enter your choice: "))
    if opt == 1:
        create_acc()
    elif opt == 2:
        login()
    else:
        e = input("Exit the portal? (Y/N): ")
        if e.upper() == "N":
            login_menu()


# ====================== ACCOUNT CREATION ======================
def create_acc():
    print("\nEnter the details to create your account:")
    i = randint(1000, 10000)
    print(f"Your generated ID is: {i}")
    p = input("Enter your password: ")
    n = input("Enter your name: ")
    sex = input("Enter your gender (M/F/O): ")
    age = input("Enter your age: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    ph = input("Enter your contact number: ")

    cur.execute("INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (i, p, n, sex.upper(), age, dob, ph))
    print("✅ Account created successfully! Now you may log in.")
    login()


# ====================== LOGIN ======================
def login():
    global a
    try:
        a = int(input("Enter your ID: "))
        b = input("Enter your password: ")
        cur.execute("SELECT name FROM accounts WHERE id = %s AND pass = %s", (a, b))
        j = cur.fetchone()
        if j:
            print(f"Welcome back, {j[0]}!")
            main_menu()
        else:
            raise Exception
    except:
        print("❌ Your account was not found!")
        print("You can: \n1. Try logging in again\n2. Create a new account")
        ch = input("Enter your choice: ")
        if ch == "1":
            login()
        elif ch == "2":
            create_acc()
        else:
            login_menu()


# ====================== MAIN MENU ======================
def main_menu():
    print("\nWhat would you like to do today?")
    print("1. Purchase a Ticket")
    print("2. Check Ticket Status")
    print("3. Request a Refund")
    print("4. Account Settings")
    print("5. Update Data")
    print("6. Logout")
    print("7. Exit")

    ch1 = int(input("Enter your choice: "))
    if ch1 == 1:
        buy_ticket()
    elif ch1 == 2:
        show_ticket()
    elif ch1 == 3:
        cancel_ticket()
    elif ch1 == 4:
        account()
    elif ch1 == 5:
        update_data()
    elif ch1 == 6:
        login_menu()
    else:
        exit_prompt()


# ====================== EXIT PROMPT ======================
def exit_prompt():
    x2 = input("Would you like to exit? (Y/N): ")
    if x2.upper() == "N":
        main_menu()


# ====================== BACK TO MAIN MENU ======================
def back_to_main_menu():
    x3 = input("\nReturn to the Main Menu? (Y/N): ")
    if x3.upper() == "Y":
        print("Returning to Main Menu...")
        main_menu()


# ====================== TICKET CREATION ======================
def buy_ticket():
    print("\nEnter details for your journey:")
    i = a
    pnr = randint(100000, 1000000)
    print(f"Your PNR is {pnr}")
    train = input("Enter the name of the train: ")
    doj = input("Enter the date of your journey (YYYY-MM-DD): ")
    fr = input("Enter the Departing Station: ")
    to = input("Enter the Destination Station: ")
    cur.execute("INSERT INTO tickets VALUES (%s, %s, %s, %s, %s, %s)", (i, pnr, train, doj, fr, to))
    print("✅ Ticket booked successfully!")
    back_to_main_menu()


# ====================== SHOW TICKET ======================
def show_ticket():
    try:
        pnr = int(input("Enter your PNR: "))
        cur.execute("SELECT * FROM tickets WHERE pnr = %s", (pnr,))
        j = cur.fetchone()
        if j and j[0] == a:
            print(f"\nTrain: {j[2]}\nDate of Journey: {j[3]}\nFrom: {j[4]}\nTo: {j[5]}")
        else:
            print("Unauthorized access or ticket not found!")
        back_to_main_menu()
    except:
        ticket_not_found()


# ====================== CANCEL TICKET ======================
def cancel_ticket():
    try:
        pnr = int(input("Enter the PNR number of the ticket: "))
        cur.execute("SELECT id, pnr, train FROM tickets WHERE pnr = %s", (pnr,))
        j = cur.fetchone()
        if j and j[0] == a:
            print(f"\nPNR: {j[1]}\nTrain: {j[2]}")
            x4 = input("Do you really want to cancel this ticket? (Y/N): ")
            if x4.upper() == "Y":
                cur.execute("DELETE FROM tickets WHERE pnr = %s", (pnr,))
                print("✅ Ticket cancelled successfully! Refund will be processed soon.")
        else:
            print("Unauthorized access or ticket not found!")
        back_to_main_menu()
    except:
        ticket_not_found()


# ====================== TICKET NOT FOUND ======================
def ticket_not_found():
    print("\nTicket not found!")
    print("1. Try entering your PNR number again")
    print("2. Purchase a ticket")
    print("3. Return to Main Menu")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        show_ticket()
    elif ch == 2:
        buy_ticket()
    elif ch == 3:
        main_menu()
    else:
        exit_prompt()


# ====================== ACCOUNT SETTINGS ======================
def account():
    print("\nDo you want to:")
    print("1. Show Account Details")
    print("2. Delete Account")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        cur.execute("SELECT * FROM accounts WHERE id = %s", (a,))
        j = cur.fetchone()
        print(f"\nID: {j[0]}\nName: {j[2]}\nGender: {j[3]}\nAge: {j[4]}\nDOB: {j[5]}\nPhone: {j[6]}")
        back_to_main_menu()
    elif ch == 2:
        x6 = input("Do you want to delete all your tickets too? (Y/N): ")
        if x6.upper() == "Y":
            cur.execute("DELETE FROM tickets WHERE id = %s", (a,))
            print("Refund will be processed for your deleted tickets.")
        cur.execute("DELETE FROM accounts WHERE id = %s", (a,))
        print("✅ Account Deleted Successfully!")
        login_menu()
    else:
        back_to_main_menu()


# ====================== UPDATE MENU ======================
def update_data():
    print("\nWhat would you like to update?")
    print("1. Update Account Details")
    print("2. Update Ticket Details")
    print("3. Back to Main Menu")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        update_account()
    elif ch == 2:
        update_ticket()
    else:
        main_menu()


# ====================== UPDATE ACCOUNT ======================
def update_account():
    print("\nWhat detail do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Phone Number")
    print("4. Password")
    print("5. Back")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_name = input("Enter new name: ")
        cur.execute("UPDATE accounts SET name = %s WHERE id = %s", (new_name, a))
        print("✅ Name updated successfully!")

    elif choice == 2:
        new_age = input("Enter new age: ")
        cur.execute("UPDATE accounts SET age = %s WHERE id = %s", (new_age, a))
        print("✅ Age updated successfully!")

    elif choice == 3:
        new_ph = input("Enter new phone number: ")
        cur.execute("UPDATE accounts SET ph_no = %s WHERE id = %s", (new_ph, a))
        print("✅ Phone number updated successfully!")

    elif choice == 4:
        new_pass = input("Enter new password: ")
        cur.execute("UPDATE accounts SET pass = %s WHERE id = %s", (new_pass, a))
        print("✅ Password updated successfully!")

    back_to_main_menu()


# ====================== UPDATE TICKET ======================
def update_ticket():
    try:
        pnr = int(input("Enter the PNR of the ticket to update: "))
        cur.execute("SELECT * FROM tickets WHERE pnr = %s AND id = %s", (pnr, a))
        j = cur.fetchone()
        if not j:
            print("❌ Ticket not found or unauthorized!")
            return back_to_main_menu()

        print("\nWhat do you want to update?")
        print("1. Train Name")
        print("2. Date of Journey")
        print("3. From Station")
        print("4. To Station")
        print("5. Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_train = input("Enter new train name: ")
            cur.execute("UPDATE tickets SET train = %s WHERE pnr = %s", (new_train, pnr))
            print("✅ Train name updated successfully!")

        elif choice == 2:
            new_doj = input("Enter new date of journey (YYYY-MM-DD): ")
            cur.execute("UPDATE tickets SET doj = %s WHERE pnr = %s", (new_doj, pnr))
            print("✅ Date updated successfully!")

        elif choice == 3:
            new_from = input("Enter new departing station: ")
            cur.execute("UPDATE tickets SET tfr = %s WHERE pnr = %s", (new_from, pnr))
            print("✅ Departing station updated successfully!")

        elif choice == 4:
            new_to = input("Enter new destination station: ")
            cur.execute("UPDATE tickets SET tto = %s WHERE pnr = %s", (new_to, pnr))
            print("✅ Destination updated successfully!")

        back_to_main_menu()
    except Exception as e:
        print("⚠️ Error:", e)
        ticket_not_found()


# ====================== PROGRAM START ======================
if __name__ == "__main__":
    login_menu()
