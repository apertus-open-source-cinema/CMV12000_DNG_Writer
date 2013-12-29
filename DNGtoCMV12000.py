import struct, collections
import numpy as np
import sys, getopt
import shutil
from math import *
from DNGTags import *
from DNG import *

def printUsage():
	print 'DNGtoCMV12000.py -i <inputDNG> -o <outputRaw>'

def main(argv):
	dngFile = ''
	rawFile = ''
	try:
   		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		printUsage()
   		sys.exit(2)
	for opt, arg in opts:
      		if opt == '-h':
			printUsage()
         		sys.exit()
      		elif opt in ("-i", "--ifile"):
         		dngFile = arg
      		elif opt in ("-o", "--ofile"):
         		rawFile = arg
	if dngFile == '' or rawFile == '':
		printUsage()
		sys.exit() 

	dng = DNG(dngFile)
	dng.openDNG()
	dng.readHeader()
	dng.readIFDs()
	dng.readSubIFD('SubIFDs')

	wf = open(rawFile, mode='wb')
	rawIFD = dng.ifd.subIFDs[0]
	rawImage = rawIFD.image << 4
	rowsPerStrip = rawIFD.tags[DNG_TAGS_STR_ID['RowsPerStrip']].value[0]
	numStrips = rawIFD.imageHeight/rowsPerStrip
	for stripNum in range(0,numStrips):
		for rowNum in range(0,rowsPerStrip):
			rowData = rawImage[stripNum*rowsPerStrip+rowNum,:]
			wf.write(struct.pack('H'*len(rowData),*rowData))
	regData = dng.ifd.getTag('DNGPrivateData').value
	wf.write(struct.pack('B'*len(regData),*regData))
	wf.close();

if __name__ == "__main__":
   main(sys.argv[1:])
