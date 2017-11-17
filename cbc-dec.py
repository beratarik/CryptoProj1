import sys
from reuseFunc import readInputs
import binascii as ba
from Crypto.Cipher import AES
from Crypto.Util import strxor
 
def main():
    kname, iname, oname, vname = readInputs(sys.argv[1:])
	
    kfile = open(kname, 'r')
    ifile = open(iname, 'r')
    ofile = open(oname, 'w')

	
    cipher = ifile.read()
    cipher = cipher.rstrip()
    print("cipher is " + str(cipher))
    
    key = kfile.read()
    key = key.rstrip()
    print("key is " + str(key))
     
    blocksize = 16
    l = []
    print("cipher size is " + str(len(cipher)))
    cipher = bytes(cipher,'utf-8')
    #cipher = cipher[2:]
    #cipher = cipher[::-1]
    print("cipher is "+str(cipher))
    print("with size "+str(len(cipher)))
    IV = cipher[:16]
    print("IV is " + str(IV))
    cipher = cipher[16:]

    print(len(cipher))
    for i in range(len(cipher)):
        if(i%blocksize == blocksize -1 and i != 0):
            #this is not correct
            print(cipher[i-blocksize+1:i+1])
            l.append(cipher[i-blocksize+1:i+1])
    print(i)
    
    for i in range(len(l)):
        print(i)
        print("hex is " + str(l[i]))
    message = ''
    for i in range(len(l)-1, 0, -1):
        print("i unhex is " + str((l[i])))
        l[i] = bytes(l[i], 'utf-8')
        ciph = decrypt(key,(l[i]))
        print("ciph is " + str((ciph)) +" li-1 is " + str((l[i-1])))
        #ciph = str(ciph)
        c = strxor.strxor(bytes(l[i-1],'utf-8'), (ciph))
        #c = c.decode('utf-8')
        print("c is " + str(c))
        message = str(c)+ message
    print(message)
def decrypt(key,cipher):
   # cipher = ba.unhexlify(cipher) 
    ciph = AES.AESCipher(key[:32], AES.MODE_ECB)
    cipher = ciph.decrypt(cipher)
    print(str(cipher))
    return cipher#.decode('utf-8')   
main()		
