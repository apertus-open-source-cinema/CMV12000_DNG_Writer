import struct, collections
import numpy as np
import sys
import shutil
from math import *
from DNGTags import *
from DNG import *

dngFile = 'img.dng'
rawFile = 'img.raw16'

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
