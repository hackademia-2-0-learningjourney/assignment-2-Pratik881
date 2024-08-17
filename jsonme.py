import json

# Function to load the user data from the JSON file
def load_user_data():
    with open("me.json", "r") as file:
        return json.load(file)

# Function to save the user data to the JSON file
def save_user_data(users):
    with open("me.json", "w") as file:
        json.dump(users, file, indent=5)

# Function for user sign-up
def sign_up():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    phone_number = input("Enter your phone number: ")
    
    users = load_user_data()
    
    if username in users:
        print("Username already exists.")
    else:
        users[username] = {"password": password, "phone_number": phone_number}
        save_user_data(users)
        print("User sign-up successful!")

# Function for user sign-in
def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    users = load_user_data()
    
    if username in users and users[username]["password"] == password:
        print("Sign-in successful!")
    else:
        print("Incorrect credentials.")
        
# Main program flow
print("1. Sign up")
print("2. Sign in")
choice = input("Enter your choice (1/2): ")

if choice == "1":
    sign_up()
elif choice == "2":
    sign_in()
else:
    print("Invalid choice.")
