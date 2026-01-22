import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password: str, stored_hash: str) -> bool:
    return hash_password(input_password) == stored_hash


if __name__ == "__main__":
    password = input("Enter a password: ")
    hashed = hash_password(password)

    print("\nHashed password:")
    print(hashed)

    check = input("\nRe-enter password to verify: ")
    if verify_password(check, hashed):
        print("Password verified successfully.")
    else:
        print("Password verification failed.")
