#this funciton will include the reused functs
import sys
import binascii as ba
from Crypto.Cipher import AES
def readInputs():
	
	count = 0
	while(count < len(sys.argv)):
		if(sys.argv[count] == "-i")
			iname = sys.argv[count+1]
		elif(sys.argv[count] == "-k"
			kname = sys.argv[count+1]
		elif(sys.argv[count] == "-o")
			oname = sys.argv[count+1]
		elif(sys.argv[count] == "-v")
			vname = sys.argv[count+1]
		count = count+2;
	return kname, iname, oname, vname

def impAESenc(key, inputString)
	#inputstring should be 8 bytes
	
	cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
	ctext = cipher.encrypt(inputString)
	return binascii.hexlify(bytearray(ctext)).decode('utf-8')
	
def impAESdec(key, inputString)
	enc = binascii.unhexlify(enc)
	cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
	enc = cipher.decrypt(enc)
	return enc.decod('utf-8')
