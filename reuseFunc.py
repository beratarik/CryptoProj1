#this funciton will include the reused functs
import sys, getopt
import binascii as ba
from Crypto.Cipher import AES
def readInputs(argv):
	iname = ''
	oname = ''
	kname = ''
	vname = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -k <key> -v IV -i <inputfile> -o <outputfile>"'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			iname = arg
		elif opt in ("-o", "--ofile"):
			oname = arg
		elif opt in ("-k", "--kfile"):
			kname = arg
		elif opt in ("-v", "--vfile"):
			vname = arg
	print 'Input file is "', iname
	print 'Output file is "', oname	
	#count = 1
	#while(cot < len(sys.argv)):
	#	if(sys.argv[count] == '-i')
	#		iname = sys.argv[count+1]
	#	elif(sys.argv[count] == '-k'
	#		kname = sys.argv[count+1]
	#	elif(sys.argv[count] == '-o')
	#		oname = sys.argv[count+1]
	#	elif(sys.argv[count] == '-v')
	#		vname = sys.argv[count+1]
	#	count = count+2;
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
