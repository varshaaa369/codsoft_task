import random
import string

def generate_password(length):
    # Define the character sets: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the given length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    # Get the desired password length from the user
    length = int(input("Enter the desired length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
