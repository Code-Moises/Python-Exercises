import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters #huge string -> !asdwad1235AWDAD...
chars = list(chars) # now divided into a list " ", "!", ...
key = chars.copy()

# now let's shuffle our key list
random.shuffle(key)

#ENCRYPTION
def ecryption(chars, key):
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Original message: {plain_text}\nEncrypted message: {cipher_text}")


#DECRYPTION
def decryption(chars, key):
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted message: {cipher_text}\nDecrypted message: {plain_text}")

def main():
    ecryption(chars, key)
    decryption(chars, key)

if __name__ == "__main__":
    main()