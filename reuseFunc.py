#this funciton will include the reused functs
import sys
import binascii as ba
from Crypto.Cipher import AES
def readInputs(iname, kname, oname,vname):
	
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
