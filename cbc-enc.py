import sys
import binascii as ba
from Crypto.Cipher import AES
from Crypto.Util import strxor
import random
from reuseFunc import readInputs
def main():
    kname, iname, oname, vname = readInputs(sys.argv[1:])
   

    blocksize = 8
    l = []
    isIV = 0
    if vname != '':
        vfile = open(vname, 'r')
        isIV = 1
    kfile = open(kname, 'r')
    ifile = open(iname, 'r')
    ofile = open(oname, 'w')

    message = ifile.read()
    message = message.rstrip()

    key = kfile.read()
    key = key.rstrip()

    ciphertext =''
    if isIV == 0:
        ran = random.randrange(10**80)
        myhex = "%64x" %ran
        myhex = myhex[:16]
    else:
        myhex = vfile.read()
        myhex = myhex.rstrip()
        myhex = myhex[:16]
    ciphertext += myhex
    myhex = bytes(myhex, 'utf-8')
    #print("myhex is " + str(myhex))

   
    #print("Unpadded message is " + message)
    padded = pad(message)

    #print("Padded message is " + padded.decode('utf-8'))
    #print("hex mesage " + str(ba.hexlify(padded)))
    for i in range(len(padded)):
        if(i%blocksize == blocksize-1 and i != 0):
            #print(padded[i-blocksize+1:i+1])
            l.append(padded[i-blocksize+1:i+1])
    
    #for i in range(len(l)):
        #print("hex is " + str((l[i])))
    
    #print("l is " + str(ba.hexlify(l[0]))) 
    #print()
    #print(ciphertext)
    c = strxor.strxor(myhex, ba.hexlify(l[0]))
    #print(c)
    #h = strxor.strxor(myhex, c)
    #print("h is " +str((h)))
    #c = xor(myhex, (l[0]))
    #print("C is " +str(ba.hexlify(c)))
    
    cipher = encrypt(key, c)
    print("cipher is " + str(cipher))
    ciphertext = createCipher(ciphertext, cipher)
    #print(ciphertext)
    for i in range(1,len(l)):
        #print("xor of " + str(ba.unhexlify(cipher)) + " and " + str(ba.hexlify(l[i])))
        c = strxor.strxor(ba.unhexlify(cipher),ba.hexlify(l[i]))
        #print("Xor res is " + str(c))
        cipher = encrypt(key, c)
        print("cipher is " + str(cipher))
        ciphertext = createCipher(ciphertext, cipher)

    #print(ciphertext)
    ofile.write(ciphertext)

def pad(message):
    
    padamount = 8 - len(message) % 8
    padbyte = chr(padamount)
    padded = (message + padbyte * padamount).encode('utf-8')
    return padded


def encrypt(key, message):
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    return ba.hexlify(bytearray(ciphertext)).decode('utf-8')

def createCipher(ciphertext, message):
    ciphertext += message;
    return ciphertext

main()
