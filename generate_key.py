from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it to the file
    """

    key = Fernet.generate_key()
    with open("secret.key", "wb") as keyFile:
        keyFile.write(key)

if __name__ == "__main__" :
    generate_key()
    print("Key Generated and saved to secret.key")
