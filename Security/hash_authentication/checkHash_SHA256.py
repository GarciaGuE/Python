import os
import sys
from Crypto.Hash import SHA256
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Compare a given SHA256 hash and the hash generated from a file')
parser.add_argument('fname', help='Input file', type=str)
parser.add_argument('hash', help='Hash to compare', type=str)
args=parser.parse_args()

#Funcion para comparar el hash SHA256 de un fichero y uno dado
def checkHashSHA256():
    f=open(args.fname, 'rb')
    data=f.read()
    f.close()
    hash_object1=SHA256.new(data)
    hashf=hash_object1.hexdigest()
    if hashf==args.hash:
        print('The provided file and the SHA256 hash value match.')
    else:
        print('The provided file and the SHA256 hash value do not match.')
        print('Hash of', args.fname+':', hashf)
        print('Compared hash:', args.hash)
    
#Main
def main():
    if os.path.isfile(args.fname):
        checkHashSHA256()
    else:
        print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main()    