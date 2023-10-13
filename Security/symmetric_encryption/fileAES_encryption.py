import argparse
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Function to encrypt a file with AES
def fileAESEncryption(in_file):
    with open(in_file, 'r') as infile:
        text=infile.read()
    data=text.encode("utf-8")
    key=get_random_bytes(16)
    cipher=AES.new(key, AES.MODE_EAX)
    ciphertext, tag=cipher.encrypt_and_digest(data)
    nc=b64encode(cipher.nonce).decode('utf-8')
    tg=b64encode(tag).decode('utf-8')
    ct=b64encode(ciphertext).decode('utf-8')
    result={}
    result["nonce"]=nc
    result["tag"]=tg
    result["ciphertext"]=ct
    print(result)
    print("key = {}".format(key.hex()))
    with open('data.json', 'w') as outfile:
        json.dump(result, outfile)

#Main
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('in_file', help='The file to encrypt')
    args=parser.parse_args()

    #Encrypt the file
    fileAESEncryption(args.in_file)

#Call to the main function
if __name__=='__main__':
    main()
