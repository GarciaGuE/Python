import os
import string
import argparse

#Argument parser
parser=argparse.ArgumentParser(description='Frequency Analysis')
parser.add_argument('fname', help='File to analyze', type=str)
args=parser.parse_args()

#Function to calculate character frequencies in a file
def freq():
    f=open(args.fname, 'r')
    abc=list(string.ascii_lowercase)
    text=f.read()
    text=text.lower()
    f.close()
    long=len(text)
    for i in abc:
        count=0
        for j in text:
            if i==j:
                count+=1
        print('Frequency of', i+':', str(count*100/long)+'%')

#Main
def main():
    if os.path.isfile(args.fname):
        freq()
    else:
        print('The provided file does not exist.')

#Call to the main function
if __name__=='__main__':
    main()    