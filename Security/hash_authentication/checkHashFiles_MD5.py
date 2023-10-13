import os
from Crypto.Hash import MD5
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Check if two files have the same MD5 hash value')
parser.add_argument('f1name', help='File 1', type=str)
parser.add_argument('f2name', help='File 2', type=str)
args=parser.parse_args()

#Function to compare the MD5 hash of two files
def checkHashFilesMD5():
    f=open(args.f1name, 'rb')
    data1=f.read()
    f.close()
    f=open(args.f2name, 'rb')
    data2=f.read()
    f.close()
    hash_object1=MD5.new(data1)
    hash_object2=MD5.new(data2)
    hash1=hash_object1.hexdigest()
    hash2=hash_object2.hexdigest()
    if hash1==hash2:
        print('The files have the same MD5 hash value.')
    else:
        print('The files do not have the same MD5 hash value.')
        print('Hash of', args.f1name+':', hash1)
        print('Hash of', args.f2name+':', hash2)
    
#Main
def main():
    if os.path.isfile(args.f1name):
        checkHashFilesMD5()
    else:
        print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main()    