import os
import random
import string
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Substitution Encryption of a File')
parser.add_argument('f1name', help='File to encrypt', type=str)
parser.add_argument('-o', dest='f2name', type=str, metavar='f2name', help='Fichero destino')
args=parser.parse_args()

#Monoalphabetic substitution encryption function
def randomSubstitution():
    f=open(args.f1name, 'r')
    abc=list(string.ascii_lowercase)
    l=list(string.ascii_lowercase)
    random.shuffle(l)
    key=''.join(l)
    texto=f.read()
    f.close()
    texto=texto.lower()
    numeric_encryption=[]
    for i in texto:
        for j in abc:
            if i==j:
                numeric_encryption.append(abc.index(j))
    encrypted_text=''
    for i in numeric_encryption:
        encrypted_text+=key[i]
    output=open(args.f2name, 'w')
    output.write(key)
    output.write('\n')
    output.write(encrypted_text)
    output.close()

#Main
def main():
    if(args.f2name==None):
        print('Destination file not provided.')
    else:
        if os.path.isfile(args.f1name):
            randomSubstitution()
        else:
            print('The provided file does not exist')

#Call to the main function
if __name__=='__main__':
    main()    