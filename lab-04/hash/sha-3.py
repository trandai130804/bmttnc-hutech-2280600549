from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Enter the string to hash: ").encode('utf-8')
    hashed_text = sha3(text)
    
    print("Hashed text:", text.decode('utf-8'))
    print("SHA-3 Hash", hashed_text.hex())
    
if __name__ == "__main__":
    main()