#!/usr/bin/env python3

import bcrypt
import getpass
import os
import pandas as pd
from tabulate import tabulate

# hash file
hash_file = "hashpw.txt"

def hash_password(password):
    """Hash a password with bcrypt."""
    salt = bcrypt.gensalt()  # Generate a new salt
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def verify_password(password, hashed_password):
    """Verify a password against a hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)

def initialize_password():
    """Initialize the password by setting it."""
    password = getpass.getpass("Set your new password: ")
    hashed_password = hash_password(password)
    
    # Store the hashed password in a hash file
    with open(hash_file, "wb") as file:
        file.write(hashed_password)
    print("Password initialized successfully.\n")

def change_password():
    """Change the existing password."""
    with open(hash_file, "rb") as file:
        content = file.read()

    hashed_password = content
    current_password = getpass.getpass("Enter current password: ")

    if verify_password(current_password, hashed_password):
        new_password = getpass.getpass("Enter new password: ")
        confirm_new_password = getpass.getpass("Confirm new password: ")
        if new_password != confirm_new_password:
            print("new password and confirmation not match !!")
            return

        new_hashed_password = hash_password(new_password)
        # Update the hash file to update new hash password
        with open(hash_file, "wb") as file:
            file.write(new_hashed_password)
        print("Password changed successfully.")
    else:
        print("Current password is incorrect !!")

def check_password():
    """Check the password for access to the program."""
    with open(hash_file, "rb") as file:
        content = file.read()

    hashed_password = content
    entered_password = getpass.getpass("Enter password to continue: ")
    if verify_password(entered_password, hashed_password):
        print("Access granted.\n")
        return True
    else:
        print("Access denied.\n")
        return False

def main_program():
    """Main program functionality."""
    print("******************** /////  WELCOME TO ECHO PASSWORD MANAGER  ///// ********************")
    print("")
    print("!!!!!!!!!!!!!!   WARNING   !!!!!!!!!!!!!!")
    print("!!!!!!!! OPEN ON SECURE AREA ONLY !!!!!!!\n")

    Continue_button = input("Your in safe area? Want to continue?(Y/N) ").upper()
    if Continue_button != "Y":
        print("program exiting...")
        return

    laptop_pw = {"USER": ["Name-1", "Name-2", "Name-3", "Name-4", "Name-5", "Name-6", "Name-7"],
             "LAPTOP MODEL/BRAND": ["ASUS", "HP", "ASUS/LINUX", "ASUS/WINDOWS", "HP/WINDOWS", "ASUS", "HP"],
             "PASSWORD": ["None", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX"]}

    Government_ATM_pw = {"TYPES": ["SSS", "PAG-IBIG", "PHIL-HEALTH", "ATM"],
                "PASSWORD": ["N/A", "N/A", "N/A", "XXXXXXXX"],
                "USER ID": ["XXXXXXXX", "N/A", "N/A", "N/A"],
                "ACCOUNT NUMBER": ["XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX"]}
    
    Wifi_pw = {"TYPE/USERNAME": ["pldtadmin", "admin", "PLDTHOME", "PLDTHOME5G", "Telephone No."],
             "PASSWORD": ["XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX"]}
    
    Personal_pw = {"TYPES": ["Facebook", "Facebook", "Facebook", "Gmail", "Gmail", "Gmail", "Gmail", "Gmail"],
                "USERNAME": ["XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX",
                             "XXXXXXXX", "XXXXXXXX", "XXXXXXXX",
                             "XXXXXXXX"],
                "PASSWORD": ["XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX", "XXXXXXXX",
                             "XXXXXXXX", "XXXXXXXX", "XXXXXXXX"]}

    Programming_Tools_pw = {"TYPES": ["git", "github"],
             "USERNAME/email": ["XXXXXXXX", "XXXXXXXX"],
             "PASSWORD": ["None", "XXXXXXXX"]}

    Other = {"TYPES": ["XXXXXXXX", "XXXXXXXX"],
             "OWNER": ["Dad", "Mom"],
             "USERNAME/email": ["XXXXXXXX", "XXXXXXXX"],
             "PASSWORD": ["XXXXXXXX", "XXXXXXXX"]}

    
    df_laptop = pd.DataFrame(laptop_pw)
    df_gov_atm = pd.DataFrame(Government_ATM_pw)
    df_wifi = pd.DataFrame(Wifi_pw)
    df_personal = pd.DataFrame(Personal_pw)
    df_tools = pd.DataFrame(Programming_Tools_pw)
    df_other = pd.DataFrame(Other)

    print("\n=====>> LAPTOP PASSWORD")
    print(tabulate(df_laptop, headers='keys', tablefmt='grid'))
    print("\n=====>> GOV and ATM PASSWORD")
    print(tabulate(df_gov_atm, headers='keys', tablefmt='grid'))
    print("\n=====>> WIFI PASSWORD")
    print(tabulate(df_wifi, headers='keys', tablefmt='grid'))
    print("\n=====>> PERSONAL PASSWORD")
    print(tabulate(df_personal, headers='keys', tablefmt='grid'))
    print("\n=====>> PROGRAMMING TOOLS PASSWORD")
    print(tabulate(df_tools, headers='keys', tablefmt='grid'))
    print("\n=====>> OTHER PASSWORD")
    print(tabulate(df_other, headers='keys', tablefmt='grid'))
    print("")
    print("")

def main():
    """Main function to control program flow."""
    if not os.path.exists(hash_file) or os.path.getsize(hash_file) == 0:
        print("\nNo password set. Initialize a password first.")
        initialize_password()

    print("*********** FOR ALLOWED PERSONNEL ONLY ***********\n")
    print("1. Continue the program")
    print("2. Change password\n")
    
    choice = input("Select 1 or 2: ")
    
    if choice == "1":
        if check_password():
            main_program()
            return

        return

    if choice == "2":
        change_password()
        return

    else:
        print("not a valid choice")
        print("program exiting...")

if __name__ == "__main__":
    main()
