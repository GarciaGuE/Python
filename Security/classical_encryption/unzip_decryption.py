import os
import string
import argparse
import zipfile
from os import remove

#Argument parser
parser=argparse.ArgumentParser(description='Decryption of a compressed file using Caesar Cipher ROT3')
parser.add_argument('f1name', help='Zip file to decompress and decrypt', type=str)
parser.add_argument('-o', dest='f2name', type=str, metavar='f2name', help='Destination file')
args=parser.parse_args()

#Decompression function
def unzp():
    zip=args.f1name
    with zipfile.ZipFile(zip) as myzip:
        name=myzip.namelist()
        myzip.extractall()
    return name[0]

#Caesar Decryption function with a shift of 3
def caesarDecryptionROT3(file):
    f=open(file, 'r')
    abc=list(string.ascii_lowercase)
    text=f.read()
    f.close()
    text=text.lower()
    numeric_decryption=[]
    for i in text:
        count=0
        for j in abc:
            if j==i:
                result=(count-3)%26
                numeric_decryption.append(result)
            else:
                count+=1
    decrypted_text=''
    for i in numeric_decryption:
        for j in abc:
            if abc.index(j)==i:
                decrypted_text+=j
    output=open(args.f2name, 'w')
    output.write(decrypted_text)
    output.close()
    remove(file)   

#Main
def main():
    if(args.f2name==None):
        print('Destination file not provided.')
    else:
        fichero=unzp()
        if os.path.isfile(fichero):
            caesarDecryptionROT3(fichero)
        else:
            print('The provided file does not exist.')

#Call to the main function
if __name__ == '__main__':
    main()    