#this funciton will include the reused functs
import sys, getopt
import binascii as ba
from Crypto.Cipher import AES


def readInputs(commandl):
	#call with
	print(commandl)
	iname = ''
	oname = ''
	kname = ''
	vname = ''
	try:
		opts, args = getopt.getopt(commandl,"hi:o:k:v:",["kfile=", "vfile=","ifile=","ofile="])
	except getopt.GetoptError:
		print ('test.py -k <keyfile> -v <IVfile> -i <inputfile> -o <outputfile>"')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -k <key> -v <IVfile> -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			iname = arg
		elif opt in ("-o", "--ofile"):
			oname = arg
		elif opt in ("-k", "--kfile"):
			kname = arg
		elif opt in ("-v", "--vfile"):
			vname = arg
	print ('Input file is "', iname)
	print ('key is "', kname)	
	print ('Output file is "', oname)	
	print ('IV file is "', vname)	
	
	return kname, iname, oname, vname

def impAESenc( key, inputString ):
	#inputstring should be 8 bytes
	
	cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
	ctext = cipher.encrypt(inputString)
	return binascii.hexlify(bytearray(ctext)).decode('utf-8')
	
def impAESdec(key, inputString):
	enc = binascii.unhexlify(enc)
	cipher = AES.AESCipher(key[:32], AES.MODE_ECB)
	enc = cipher.decrypt(enc)
	return enc.decod('utf-8')

def impXOR(xor_val, mess_block):
	c = int(xor_val, 16) ^ int(mess_block,16)
	print("xor of " + str(xor_val) + " and " + str(mess_block))
	print(c)
	print()
	print(hex(c))
	return c
