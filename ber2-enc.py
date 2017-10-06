import sys
import binascii as ba
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import strxor
import random
def main():

    kname = sys.argv[1]
    iname = sys.argv[2]
    oname = sys.argv[3]

    blocksize = 8
    l = []

    if(len(sys.argv) == 5):
        ivname = sys.argv[4]
        ivfile = open(ivname, 'r')

    kfile = open(kname, 'r')
    ifile = open(iname, 'r')
    oname = open(oname, 'w')

    message = ifile.read()
    message = message[:-1]
    #message = message.encode('utf-8')

    key = kfile.read()
    key = key[:-1]

    rndfile = Random.new()
    IV = rndfile.read(8)
    ran = random.randrange(10**80)
    myhex = "%64x" %ran
    myhex = myhex[:16]
    myhex = bytes(myhex, 'utf-8')
    print("myhex is " + str(myhex))
    print("IV is " + str(IV))
    IV = ba.hexlify(IV)
    print("IV is  " + str(IV))
    #print("Unpadded message is " + message)
    padded = pad(message)

    #print("Padded message is " + padded.decode('utf-8'))
    #print("hex mesage " + str(ba.hexlify(padded)))
    for i in range(len(padded)):
        if(i%blocksize == blocksize-1 and i != 0):
            l.append(padded[i-blocksize+1:i+1])
    
    for i in range(len(l)):
        print("hex is " + str((l[i])))
    ciphertext = ''
    print("l is " + str(ba.hexlify(l[0]))) 
    c = strxor.strxor(myhex, ba.hexlify(l[0]))
    h = strxor.strxor(myhex, c)
    print("h is " +str((h)))
    #c = xor(myhex, (l[0]))
    print("C is " +str(ba.hexlify(c)))
    
    cipher = encrypt(key, c)
    ciphertext = createCipher(ciphertext, cipher)
    print(ciphertext)
    for i in range(1,len(l)):
        print("xor of " + str(ba.unhexlify(cipher)) + " and " + str(ba.hexlify(l[i])))
        c = strxor.strxor(ba.unhexlify(cipher),ba.hexlify(l[i]))
        print("Xor res is " + str(c))
        cipher = encrypt(key, c)
        ciphertext = createCipher(ciphertext, cipher)

    print(ciphertext)

def pad(message):
    
    padamount = 8 - len(message) % 8
    padbyte = chr(padamount)
    padded = (message + padbyte * padamount).encode('utf-8')
    return padded

def xor(xor_val,mess_block):
    print("xor of " + str(xor_val) + " and " + str(mess_block))
    #return ba.hexlify(bytes(a^b) for a, b in zip(ba.unhexlify(xor_val), ba.unhexlify(mess_block)))
    #encrypt = int(xor_val, 16) ^ int(mess_block, 16)
    #for i in range(len(encrypt)):
    #    c += str(encrypt[i])
    #c = ''.join(str(encrypt))
    #return hex(encrypt)[2:]
    #encrypted = [ chr(a ^ b) for (a,b) in zip(xor_val, mess_block) ]
    #print(encrypted)
    #str1 = ''.join(encrypted)
    #str1 = str1.encode('utf-8')
    #print(str1)
    b = xor_val
    if type(xor_val) is str:
        b = bytes(xor_val,encoding='utf8')
    iData = int.from_bytes(mess_block, sys.byteorder)
    iKey = int.from_bytes(b, sys.byteorder)
    xored = iData ^ iKey
    xored - xored.to_bytes(len(mess_block), sys.byteorder)
    return xored
    #return str1
def encrypt(key, message):
    cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    return ba.hexlify(bytearray(ciphertext)).decode('utf-8')

def createCipher(ciphertext, message):
    ciphertext += message;
    return ciphertext

main()
