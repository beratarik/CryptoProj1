import sys, argparse
from reuseFunc import readInputs
from reuseFunc import impXOR
from reuseFunc import impAESdec
import binascii as ba
from Crypto.Cipher import AES

 
def main():
    kname, iname, oname, vname = readInputs(sys.argv[1:])
	
    kfile = open(kname, 'r')
    ifile = open(iname, 'r')
    ofile = open(oname, 'w')

	
    cipher = ifile.read()
    cipher = cipher[:-1]
    
    key = kfile.read()
    key = key[:-1]
    
    print("read in k " +str(kname) +" and v "+str(vname)+ " and i " + str(iname)+" and o "  + str(oname))	
    
    blocksize = 8
    l = []
    
    for i in range(len(cipher)):
        l.append(cipher[i-blocksize+1:i+1])
    
    for i in range(len(l)):
        print("hex is " + str(ba.hexlify(l[i])))
    
    decd = impAESdec(key, ba.hexlify(l[i]))

main()		
