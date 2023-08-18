import random
import string
import argparse

def generate_secure_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    secure_password = ''.join(random.choice(all_characters) for _ in range(length))
    return secure_password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("length", type=int, default=12, nargs='?', help="Length of the password")
    args = parser.parse_args()
    
    secure_password = generate_secure_password(args.length)
    print("Generated Secure Password:", secure_password)

if __name__ == "__main__":
    main()