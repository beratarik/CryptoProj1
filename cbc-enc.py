import sys
import binascii as ba
from Crypto.Cipher import AES

def main():

    kname = sys.argv[1]
    iname = sys.argv[2]
    oname = sys.argv[3]
    if(len(sys.argv) == 5):
        ivname = sys.argv[4]
        ivfile = open(ivname, 'r')

    kfile = open(kname, 'r')
    ifile = open(iname, 'r')
    oname = open(oname, 'w')

    message = ifile.read()
    message = message[:-1]
    #message = message.encode('utf-8')
    print(message)
    pad(message)

def pad(message):
    
    padamount = 8 - len(message) % 8
    padbyte = chr(padamount)
    print((message + padbyte * padamount).encode('utf-8'))

main()
