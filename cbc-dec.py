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
    cciph = cipher.encode('utf-8')
    for i in range(len(cciph)):
        if(i%blocksize == blocksize -1 and i != 0):
            l.append(cciph[i-blocksize+1:i+1])
    
    for i in range(len(l)):
        print("hex is " + str(ba.hexlify(l[i])))
    
    z = len(l)-1
    while z >0:
        i = z    
        decd = impAESdec(key, ba.hexlify(l[i]))
        m = impXOR(decd, ba.hexlify(l[i-1]))
        #put m in ofile
main()		
