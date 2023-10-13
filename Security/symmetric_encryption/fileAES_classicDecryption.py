import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def classicFile_AES_Decryption():
    i=input("Enter the key: ")
    try:
        key=bytes.fromhex(i)
    except (ValueError, KeyError):
        print("You entered a non-hexadecimal number")
        exit()
        
    try:
        with open("data.json") as json_data:
            b64=json.load(json_data)
            print(b64)
        iv=b64decode(b64['iv'])
        ct=b64decode(b64['ciphertext'])
        cipher=AES.new(key, AES.MODE_CBC, iv)
        pt=unpad(cipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")

#Main
def main():
    classicFile_AES_Decryption()

#Call to the main function
if __name__=='__main__':
    main()
