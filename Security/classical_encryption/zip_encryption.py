import os
import string
import argparse
import zipfile
from os import remove

#Argument parser
parser=argparse.ArgumentParser(description='Caesar Encryption ROT3 of a file and compression')
parser.add_argument('f1name', help='File to encrypt and compress', type=str)
parser.add_argument('-o', dest='f2name', type=str, metavar='f2name', help='Destination zip file')
args=parser.parse_args()

#Compression function
def zp(file):
    zipname=args.f2name
    with zipfile.ZipFile(zipname, 'w') as myzip:
        myzip.write(file)
    remove(file)

#Caesar Encryption function with a shift of 3
def caesarEncryptionROT3():
    f=open(args.f1name, 'r')
    abc=list(string.ascii_lowercase)
    text=f.read()
    f.close()
    text=text.lower()
    numeric_encryption=[]
    for i in text:
        count=0
        for j in abc:
            if j==i:
                result=(count+3)%26
                numeric_encryption.append(result)
            else:
                count+=1
    encrypted_text=''
    for i in numeric_encryption:
        for j in abc:
            if abc.index(j)==i:
                encrypted_text+=j
    zip_folder=args.f2name.rsplit('.', 1)[0]+'.enc'
    salida=open(zip_folder, 'w')
    salida.write(encrypted_text)
    salida.close()
    return zip_folder

#Main
def main():
    if(args.f2name==None):
        print('Destination file not provided.')
    else:
        if os.path.isfile(args.f1name):
            zp(caesarEncryptionROT3())
        else:
            print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main()        