import os
import string
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Caesar Encryption of a File')
parser.add_argument('kROT', help='Shift', type=int, choices=range(1,26))
parser.add_argument('f1name', help='File to encrypt', type=str)
parser.add_argument('-o', dest='f2name', type=str, metavar='f2name', help='Destination file')
args=parser.parse_args()

#Caesar Encryption function with user-defined shift
def caesarEncryption():
    f=open(args.f1name, 'r')
    abc=list(string.ascii_lowercase)
    text=f.read()
    f.close()
    text=text.lower()
    numeric_encryption=[]
    shift=int(args.kROT)
    for i in text:
        count=0
        for j in abc:
            if j==i:
                resultado=(count+shift)%26
                numeric_encryption.append(resultado)
            else:
                count+=1
    encrypted_text=''
    for i in numeric_encryption:
        for j in abc:
            if abc.index(j)==i:
                encrypted_text+=j
    output=open(args.f2name, 'w')
    output.write(encrypted_text)
    output.close()

#Main
def main():
    if(args.f2name==None):
        print('Destination file not provided.')
    else:
        if os.path.isfile(args.f1name):
            caesarEncryption()
        else:
            print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main()     
 