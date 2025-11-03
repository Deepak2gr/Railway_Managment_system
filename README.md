# 🚆 IRCTC Portal System (MySQL + Python)

This project is a console-based **IRCTC Ticket Booking and Management System** built using **Python** and **MySQL**.  
It allows users to create accounts, book train tickets, check status, request refunds, and manage their profiles — all through a structured, menu-driven interface.

---

## 🧩 Features

### 👤 Account Management
- Create new user accounts with validation (Name, Age, DOB, Phone)
- Log in using User ID and Password
- Update personal details (Name, Age, Phone, Password)
- View or delete account information

### 🚉 Ticket Operations
- Book tickets with automatic **PNR generation**
- View ticket details using PNR
- Cancel (refund) tickets with confirmation
- Display booked journey information clearly

### ⚙️ System & Database
- Connects to MySQL for secure data storage
- Auto-creates required tables on first run
- Ensures data integrity using `commit()` and rollback mechanisms
- Includes error handling for invalid inputs and connections

---

## 🗂️ Database Structure

### `account` Table
| Column | Type | Description |
|--------|------|-------------|
| id | INT | Unique User ID |
| password | VARCHAR(255) | User password |
| name | VARCHAR(100) | Full name |
| gender | CHAR(1) | M/F/O |
| age | INT | Age of user |
| dob | DATE | Date of Birth |
| phone | VARCHAR(15) | Contact number |

### `ticket` Table
| Column | Type | Description |
|--------|------|-------------|
| pnr | INT | Unique PNR Number |
| user_id | INT | Reference to Account ID |
| train_name | VARCHAR(100) | Name of the train |
| journey_date | DATE | Travel date |
| source | VARCHAR(100) | Departure station |
| destination | VARCHAR(100) | Destination station |

---

## 🧠 Flow Overview

The system follows a **menu-driven flow**:

1. Connect to MySQL  
2. Main Menu  
   - Create Account  
   - Log In  
   - Exit  
3. Logged-in Menu  
   - Purchase Ticket  
   - Check Ticket Status  
   - Request Refund  
   - Account Settings  
   - Update Data  
   - Logout / Exit  

📊 A complete process flow is available in the **Flowchart** section below.

---

## 🗺️ Flowchart

<img width="1024" height="1536" alt="flowcharrail" src="https://github.com/user-attachments/assets/e1578532-2ef3-4a13-93da-fb6d927f152c" />


This flowchart visually represents the system’s step-by-step logic, including database interactions and user decision paths.

---

## 🧰 Technologies Used
- **Python 3.x**
- **MySQL Connector**
- **MySQL Server**
- **Figma** (for flowchart design)
💡 Future Improvements

GUI-based version using Tkinter or PyQt

Password encryption (bcrypt)

Admin dashboard for user/ticket management

SMS/email ticket confirmation integration

👨‍💻 Author

Deepak Kumar
📍 Delhi, India
🔗 LinkedIn
 | GitHub

Navigate to the folder:

cd IRCTC-Portal-System


Install dependencies:

pip install mysql-connector-python 
---

Would you like me to include the **IRCTC_Flowchart.png** file reference (so GitHub automatically shows it in the README preview)?  
If yes, I’ll adjust the link to display it directly in your repository after you upload the file.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Deepak2gr/Railway_Managment_system

                   [START]
                      |
             +--------v--------+
             | Connect to DB   |
             | (host,user,pass)|
             +--------+--------+
                      |
             +--------v--------+
             | Init DB & Tables|
             +--------+--------+
                      |
                   [MAIN MENU]
          (1) Create Account   (2) Log In   (3) Exit
               |                  |           |
    +----------+----+       +-----+-----+     |
    |               |       |           |     |
[Create Account]  <-------- [Login]     |     |
    |                       |Valid?     |     |
    |-- Generate ID         |   / \     |     |
    |-- Take details        |  No  Yes   |     |
    |-- INSERT account      |   |   |    |     |
    |-- Success msg         |   v   v    |     |
    +-----------------------+  Back to   |     |
                                Main     |     |
                                       [EXIT]
                                        

If logged in -> show LOGGED-IN MENU:
[LOGGED-IN MENU]
 1. Purchase Ticket
 2. Check Ticket Status
 3. Request Refund
 4. Account Settings
 5. Update Data
 6. Logout
 7. Exit

Purchase Ticket:
  +-- Generate PNR
  +-- Get train name, date, source, dest
  +-- INSERT ticket
  +-- Show PNR & success -> Back to Logged Menu

Check Ticket:
  +-- Input PNR
  +-- If found -> show details -> Back
  +-- If not found -> show 'Not found' -> Back

Request Refund:
  +-- Input PNR
  +-- If not found -> show 'Not found' -> Back
  +-- If found -> show details -> Confirm? (Y/N)
       Y -> DELETE ticket -> Show cancelled -> Back
       N -> Abort -> Back

Account Settings:
  +-- Option: Show Account Details -> display -> Back
  +-- Option: Delete Account -> Confirm? (Y/N)
       Y -> DELETE tickets for user -> DELETE account -> Exit
       N -> Abort -> Back

Update Data:
  +-- Choose field (Name/Age/Phone/Password)
  +-- Input new value -> UPDATE account -> Commit -> Back

Logout -> return to MAIN MENU
Exit -> Close DB and END
