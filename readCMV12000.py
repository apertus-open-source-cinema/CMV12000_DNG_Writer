import struct, collections
import numpy as np

width = 4096
height = 3072
numPixels = width*height
rawFile = 'colors_400ms.raw16'
rf = open(rawFile, mode='rb')

print "Reading raw data..."
rawData = struct.unpack("H"*numPixels,rf.read(2*numPixels))
print rawData[0] >> 4
#for i in range(0,10):
#    (byte,) = struct.unpack("H",rf.read(2))
#    print byte >> 4

print "Unpacking data..."
rawFlatImage = np.zeros(numPixels,dtype=np.uint16)
rawFlatImage[:] = rawData[:] 
rawImage = np.reshape(rawFlatImage,(height,width))
rawImage = rawImage >> 4
print rawImage[0,0:32]

print "Done"