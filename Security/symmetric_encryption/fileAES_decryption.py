import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Function to decrypt a file with AES
def fileAESDecryption():
    i=input("Enter the key: ")
    try:
        key= bytes.fromhex(i)
    except (ValueError, KeyError):
        print("You entered a non-hexadecimal number")
        exit()

    try:
        with open("data.json") as json_data:
            b64=json.load(json_data)
            print(b64)
        nonce=b64decode(b64['nonce'])
        tag=b64decode(b64['tag'])
        ciphertext=b64decode(b64['ciphertext'])
        cipher=AES.new(key, AES.MODE_EAX, nonce)
        data=cipher.decrypt_and_verify(ciphertext, tag)
        print("The message was: ", data.decode())
    except (ValueError, KeyError):
        print("Incorrect decryption")

#Main
def main():
    fileAESDecryption()

#Call to the main function
if __name__=='__main__':
    main()
