import os
from Crypto.Hash import HMAC, SHA256
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Generate an HMAC hash of a file')
parser.add_argument("fname", help="Input file", type=str)
args=parser.parse_args()

#Function HMAC of a file
def fileHMAC():
    f=open(args.fname, 'rb')
    data=f.read()
    f.close()
    hash_object=HMAC.new(data, digestmod=SHA256)
    print("HMAC Output:", hash_object.hexdigest())
    
#Main
def main():
    if os.path.isfile(args.fname):
        fileHMAC()
    else:
        print('The provided file does not exist.')

#Call the main function
if __name__=='__main__':
    main()    