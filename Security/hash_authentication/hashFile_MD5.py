import os
from Crypto.Hash import MD5
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Generate an MD5 hash of a file')
parser.add_argument('fname', help='Input file', type=str)
args=parser.parse_args()

#Function hash MD5 of a file
def hashFileMD5():
    f=open(args.fname, 'rb')
    data=f.read()
    f.close()
    hash_object=MD5.new(data)
    print('MD5 Output:', hash_object.hexdigest())
    
#Main
def main():
    if os.path.isfile(args.fname):
        hashFileMD5()
    else:
        print('The provided file does not exist.')

#Call the main function
if __name__=='__main__':
    main()    