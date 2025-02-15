import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Silly", "Witty", "Mighty", "Lucky", "Swift"]
nouns = ["Tiger", "Dragon", "Eagle", "Shark", "Wizard", "Knight", "Falcon", "Panther"]

# Function to generate a random username
def generate_username(add_numbers=False, add_special_chars=False, length=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if add_numbers:
        username += str(random.randint(10, 99))  # Adding a random two-digit number

    if add_special_chars:
        username += random.choice("!@#$%^&*")

    if length:
        username = username[:length]  # Trim or keep username within specified length

    return username

# Function to save usernames to a file
def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "a") as file:
        for name in usernames:
            file.write(name + "\n")
    print(f"Usernames saved to {filename}")

# Interactive user input 
def main():
    print("Welcome to the Random Username Generator!")

    try:
        num_usernames = int(input("How many usernames would you like to generate? "))
        add_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
        add_special_chars = input("Include special characters? (y/n): ").strip().lower() == "y"
        length = input("Max length of username (press Enter to skip): ").strip()
        length = int(length) if length.isdigit() else None

        usernames = [generate_username(add_numbers, add_special_chars, length) for _ in range(num_usernames)]

        print("\nGenerated Usernames:")
        for name in usernames:
            print(name)

        save_option = input("Save usernames to a file? (y/n): ").strip().lower()
        if save_option == "y":
            save_usernames(usernames)

    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
