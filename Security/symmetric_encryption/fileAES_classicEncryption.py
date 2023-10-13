import argparse
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

#Funcion de encriptado
def classicFile_AES_Encryption(in_file):
    with open(in_file, 'r') as infile:
        text=infile.read()
    data=text.encode("utf-8")
    key=get_random_bytes(16)
    cipher=AES.new(key, AES.MODE_CBC)
    ct_bytes=cipher.encrypt(pad(data, AES.block_size))
    iv=b64encode(cipher.iv).decode('utf-8')
    ct=b64encode(ct_bytes).decode('utf-8')
    result={}
    result["iv"]=iv
    result["ciphertext"]=ct
    print(result)
    print("key = {}".format(key.hex()))
    with open('data.json', 'w') as outfile:
        json.dump(result, outfile)

#Main
def main():
    #Procesamos los argumentos de la línea de comandos
    parser = argparse.ArgumentParser()
    parser.add_argument('in_file', help='El archivo a encriptar')
    args = parser.parse_args()

    # Encriptamos el archivo
    classicFile_AES_Encryption(args.in_file)

#Call to the main function
if __name__=='__main__':
    main()
