from cryptography.fernet import Fernet
import sys

def load_key():
    """Load the previously generated key"""
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    """Encrypt file"""

    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python encrytp_file.py <filename>")
        sys.exit(1)

    key = load_key()
    encrypt_file(sys.argv[1], key)
    print(f"Decryption of {sys.argv[1]} complete")
