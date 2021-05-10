
def encryptor(message, encryptionValue):
    encryptedMessage = ""
    for i in message:
        asciiValue = ord(i)
        if asciiValue == 32:
            encryptedCharector = chr(asciiValue)
            encryptedMessage += encryptedCharector
        else:
            asciiValue += abs(encryptionValue)
            encryptedCharector = chr(asciiValue)
            encryptedMessage += encryptedCharector
    return encryptedMessage

def decryptor(message, encryptionValue):
    decryptedMessage = ""
    for i in message:
        asciiValue = ord(i)
        if asciiValue == 32:
            decryptedCharector = chr(asciiValue)
            decryptedMessage += decryptedCharector
        else:
            asciiValue -= abs(encryptionValue)
            decryptedCharector = chr(asciiValue)
        decryptedMessage += decryptedCharector
    return decryptedMessage

if __name__== '__main__':
    text = input("What do you want to encrypt? ")
    encryptedValue = 50
    encryted = encryptor(text, encryptedValue)
    print(encryted)
    print(decryptor(encryted,encryptedValue))
