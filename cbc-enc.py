import sys
import binascii as ba
from Crypto.Cipher import AES
from Crypto import Random

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

    rndfile = Random.new()
    IV = rndfile.read(8)
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
        print("hex is " + str(ba.hexlify(l[i])))

    c = xor(IV, ba.hexlify(l[0]))
    cipher = encrypt(c, l[0])
    print(c)
    print(cipher)

def pad(message):
    
    padamount = 8 - len(message) % 8
    padbyte = chr(padamount)
    padded = (message + padbyte * padamount).encode('utf-8')
    return padded

def xor(xor_val, mess_block):
    print("xor of " + str(xor_val) + " and " + str(mess_block))
    #encrypt = [ord(chr(a)) ^ ord(chr(b)) for (a,b) in zip(xor_val, mess_block)]
    encrypt = int(xor_val, 16) ^ int(mess_block, 16)
    #for i in range(len(encrypt)):
    #    c += str(encrypt[i])
    #c = ''.join(str(encrypt))
    return hex(encrypt)[2:]

def encrypt(key, message):
    cipher = AES.AESCipher(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(message)
    return ba.hexlify(bytearray(ciphertext)).decode('utf-8')

def createCipher(message):
    ciphertext += message;
    return ciphertext

main()
