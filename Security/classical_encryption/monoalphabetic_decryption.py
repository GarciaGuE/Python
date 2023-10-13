import os
import string
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Substitution Decryption of a File')
parser.add_argument('f1name', help='File to decrypt', type=str)
parser.add_argument('-o', dest='f2name', type=str, metavar='f2name', help='Destination file')
args=parser.parse_args()

#Monoalphabetic substitution decryption function
def decryptSubstitution():
    with open(args.f1name, 'r') as f:
        lines=f.readlines()
        f.close()
    key=lines[0]
    abc=list(string.ascii_lowercase)
    text=lines[1]
    text=text.lower()
    numeric_decryption=[]
    for i in text:
        for j in key:
            if i==j:
                numeric_decryption.append(key.index(j))
    decrypted_text=''
    for i in numeric_decryption:
        decrypted_text+=abc[i]
    output=open(args.f2name, 'w')
    output.write(key)
    output.write(decrypted_text)
    output.close()

#Main
def main():
    if(args.f2name==None):
        print('Destination file not provided.')
    else:
        if os.path.isfile(args.f1name):
            decryptSubstitution()
        else:
            print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main()    