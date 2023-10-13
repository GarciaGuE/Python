import os
from Crypto.Hash import MD5
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Compare a given MD5 hash and the hash generated from a file')
parser.add_argument('fname', help='Input file', type=str)
parser.add_argument('hash', help='Hash to compare', type=str)
args=parser.parse_args()

#Function to compare the MD5 hash of a file and a given one
def checkHashMD5():
    f=open(args.fname, 'rb')
    data=f.read()
    f.close()
    hash_object1=MD5.new(data)
    hashf=hash_object1.hexdigest()
    if hashf==args.hash:
        print('The provided file and the MD5 hash value match.')
    else:
        print('The provided file and the MD5 hash value do not match.')
        print('Hash of', args.fname+':', hashf)
        print('Compared hash:', args.hash)
    
#Main
def main():
    if os.path.isfile(args.fname):
        checkHashMD5()
    else:
        print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main()