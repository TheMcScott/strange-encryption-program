import cryption, kawuub

def decrypt():
    pattern = cryption.create_key(input("Paste key:\n"))
    message = input("Enter kawuub endings:\n")
    while not message:
        print("An error occurred")
        message = input("Enter kawuub endings:\n")
    message = kawuub.convert_from_kawuub(message)
    print(f"Decrypted message is {cryption.decrypt(pattern, message)}")
    
def encrypt():
    pattern = cryption.create_key(input("Create Key:\n"))
    message = input("Enter message to encrypt:\n")
    newmessage = cryption.shakyceasar(pattern, message)
    kawuub.kawuubify(newmessage, 10)

def kawuu():
    message = input("Enter message to kawuubify: ")
    kawuub.kawuubify(message, 10)
    
def dekawuu():
    message = input("Enter message to dekawuubify: ")
    message = kawuub.convert_from_kawuub(message)
    print(message)
    
while True:
    choice = input("Encrypt or Decrypt? ").lower()
    if choice in ["encrypt", "e"]:
        choice = input("Ceasar Kawuub or Kawuub? ").lower()
        if choice in ["c", "ck", "ceasar"]:
                try:
                    encrypt()
                except:
                    pass
        elif choice in ["k", "kawuub"]:
            kawuu()
        else:
            print("Choice not recognised. Check your spelling.")
    elif choice in ["decrypt", "d"]:
        choice = input("Decrypt Ceasar Kawuub or Kawuub? ").lower()
        if choice in ["c", "ck", "ceasar"]:
            decrypt()
        elif choice in ["k", "kawuub"]:
            dekawuu()
        else:
            print("Choice not recognised. Check your spelling.")
    else:
        print("Choice not recognised. Check your spelling.")
