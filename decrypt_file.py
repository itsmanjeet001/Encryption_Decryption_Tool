from cryptography.fernet import Fernet
import sys

def load_key():
    """Loading the previously generated key"""
    return open("secret.key", "rb").read()

def decrypt_file(filename, key):
    """Decrypting the ecnrypted file"""
    fernet = Fernet(key)
   
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)
   
    with open(filename[:-13] + "Decrypted.txt", "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python decrypt_file.py <filename>")

    key = load_key()
    decrypt_file(sys.argv[1], key)
    print(f"Decryption of {sys.argv[1]} complete.")
