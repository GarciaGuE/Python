import os
import string
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Brute-Force Caesar Decryption of a File')
parser.add_argument('fname', help='File to decrypt', type=str)
args=parser.parse_args()

#Function to perform all possible Caesar cipher rotations
def bruteForceCaesar():
    f=open(args.fname, 'r')
    abc=list(string.ascii_lowercase)
    text=f.read()
    text=text.lower()
    f.close()
    for key in range(len(abc)):
        decrypted_text=''
        for i in text:
            if i in abc:
                index=abc.index(i)
                shift=index-key
                if shift<0:
                    shift=shift+len(abc)
                decrypted_text=decrypted_text+abc[shift]
            else:
                decrypted_text=decrypted_text+i
        print('Shift', str(key)+':', decrypted_text)   

#Main
def main():
    if os.path.isfile(args.fname):
        bruteForceCaesar()
    else:
        print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main() 