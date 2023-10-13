import os
from Crypto.Hash import SHA256
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Generate an SHA256 hash of a file')
parser.add_argument('fname', help='Input file', type=str)
args=parser.parse_args()

#Function hash SHA256 of a file
def hashFileSHA256():
    f=open(args.fname, 'rb')
    data=f.read()
    f.close()
    hash_object=SHA256.new(data)
    print('SHA256 Output:', hash_object.hexdigest())
    
#Main
def main():
    if os.path.isfile(args.fname):
        hashFileSHA256()
    else:
        print('The provided file does not exist.')

#Call the main function
if __name__=='__main__':
    main()    