#PROJECT-SHADOW-LOCK
class Credential:
    def __init__(self, website_name, username, password):
        self.website_name = website_name
        self.username = username
        self.password = password

    def __str__(self):
        return f"Website Name: {self.website_name} | Username: {self.username} | Password: {self.password}"


class PasswordManager:
    def __init__(self):
        self.vault = {}
        self.master_password = "krishna"
        self.is_unlocked = False

    def check_master_password(self, entered_password):
        if entered_password == self.master_password:
            self.is_unlocked = True
            print("Access Granted!")
            return True
        else:
            print("Access Denied! Wrong password.")
            return False

    def validate_password_strength(self, password):
        if len(password) < 8:
            return False
        
        has_number = False
        has_special = False
        special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        
        for char in password:
            if char.isdigit():
                has_number = True
            if char in special_chars:
                has_special = True
                
        if has_number == True and has_special == True:
            return True
        else:
            return False

    def add_credential(self, website_name, username, password):
        if website_name == "" or username == "" or password == "":
            print("Error: Fields cannot be empty.")
            return False

        if self.validate_password_strength(password) == False:
            print("Warning: Weak password! Password should have 8 chars, 1 number, and 1 symbol.")
            choice = input("Do you still want to save this password? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Credential not saved.")
                return False

        new_cred = Credential(website_name, username, password)
        self.vault[website_name] = new_cred
        print("Credentials saved successfully!")
        return True

    def retrieve_credential(self, website_name):
        if website_name in self.vault:
            cred = self.vault[website_name]
            reveal = input("Do you want to see the password? (yes/no): ").strip().lower()
            if reveal == "yes":
                print(f"Website: {cred.website_name}")
                print(f"Username: {cred.username}")
                print(f"Password: {cred.password}")
            else:
                print(f"Website: {cred.website_name}")
                print(f"Username: {cred.username}")
                print("Password: ********")
            return True
        else:
            print("Error: Website not found in your vault.")
            return False

    def export_to_csv(self):
        if len(self.vault) == 0:
            print("No records available to export.")
            return False

        try:
            file = open("shadow_lock_vault.csv", mode="w")
            file.write("Website,Username,Password\n")
            for key in self.vault:
                cred = self.vault[key]
                file.write(f"{cred.website_name},{cred.username},{cred.password}\n")
            file.close()
            print("Data successfully saved to shadow_lock_vault.csv")
            return True
        except:
            print("Error saving CSV file.")
            return False

    def save_to_json(self):
        if len(self.vault) == 0:
            print("No records found to save.")
            return False

        try:
            file = open("shadow_lock_vault.json", "w")
            file.write("{\n")
            
            keys = list(self.vault.keys())
            for i in range(len(keys)):
                k = keys[i]
                cred = self.vault[k]
                file.write(f'    "{k}": {{\n')
                file.write(f'        "website": "{cred.website_name}",\n')
                file.write(f'        "username": "{cred.username}",\n')
                file.write(f'        "password": "{cred.password}"\n')
                
                if i < len(keys) - 1:
                    file.write("    },\n")
                else:
                    file.write("    }\n")
                    
            file.write("}")
            file.close()
            print("Data successfully saved to shadow_lock_vault.json")
            return True
        except:
            print("Error saving JSON file.")
            return False


manager = PasswordManager()

while True:
    print("\n------------ SHADOWLOCK MENU -----------------")
    print("1. Unlock Vault")
    print("2. Add New Account Credentials")
    print("3. Retrieve Password for a Website")
    print("4. Export Vault to CSV")
    print("5. Save Vault to JSON")
    print("6. Exit")

    choice = input("Select an option (1-6): ").strip()

    if choice == "1":
        master_in = input("Enter the master password: ").strip()
        manager.check_master_password(master_in)

    elif choice == "2":
        if manager.is_unlocked == False:
            print("Access Blocked! Please unlock the vault first.")
            continue
        web = input("Enter Website Name: ").strip()
        user = input("Enter Username: ").strip()
        pass_str = input("Enter Password: ").strip()
        manager.add_credential(web, user, pass_str)

    elif choice == "3":
        if manager.is_unlocked == False:
            print("Access Blocked! Please unlock the vault first.")
            continue
        web = input("Enter website name to lookup: ").strip()
        manager.retrieve_credential(web)

    elif choice == "4":
        if manager.is_unlocked == False:
            print("Access Blocked! Please unlock the vault first.")
            continue
        manager.export_to_csv()

    elif choice == "5":
        if manager.is_unlocked == False:
            print("Access Blocked! Please unlock the vault first.")
            continue
        manager.save_to_json()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 6.")

