import struct, collections
import numpy as np
import sys
import shutil
from math import *
from DNGTags import *
from DNG import *

def addTag(dict, ifd, tagName):
    dict[DNG_TAGS_STR_ID[tagName]] = ifd.getTag(tagName)
def delTag(ifd, tagName):
    del ifd.tags[DNG_TAGS_STR_ID[tagName]]
    
organization = "Apertus"
cameraModel = "Axiom Alpha"
emptyDNG = 'empty.dng'
outputDNG = 'img.dng'
rawFile = sys.stdin

dng = DNG(emptyDNG)
dng.openDNG()
dng.readHeader()
dng.readIFDs()
dng.readSubIFD('SubIFDs')

makeTag = dng.ifd.getTag('Make')
makeTag.value = organization
makeTag.count = len(makeTag.value)
modelTag = dng.ifd.getTag('Model')
modelTag.value = organization + " " + cameraModel
modelTag.count = len(modelTag.value)
origRawFileNameTag = dng.ifd.getTag('OriginalRawFileName')
origRawFileNameTag.value = emptyDNG
origRawFileNameTag.count = len(origRawFileNameTag.value)

camCalTag = dng.ifd.getTag('CameraCalibrationSignature')
camCalTag.value = organization
camCalTag.count = len(camCalTag.value)
profCalTag = dng.ifd.getTag('ProfileCalibrationSignature')
profCalTag.value = organization
profCalTag.count = len(profCalTag.value)

# Replace Image
width = 4096
height = 3072
numPixels = width*height
#rf = open(rawFile, mode='rb')
rf = rawFile
rawData = struct.unpack("H"*numPixels,rf.read(2*numPixels))

rawFlatImage = np.zeros(numPixels,dtype=np.uint16)
rawFlatImage[:] = rawData[:] 
rawImage = np.reshape(rawFlatImage,(height,width))
rawImage = rawImage >> 4

rawIFD = dng.ifd.subIFDs[0]
rawIFD.image = rawImage
rawIFD.imageWidth = width
rawIFD.imageHeight = height
rawIFD.getTag('ImageWidth').value[0] = width
rawIFD.getTag('ImageLength').value[0] = height
rawIFD.getTag('StripByteCounts').value[0] = width*height*2
rawIFD.getTag('RowsPerStrip').value[0] = height
rawIFD.getTag('ActiveArea').value[0] = 0
rawIFD.getTag('ActiveArea').value[1] = 0
rawIFD.getTag('ActiveArea').value[2] = height
rawIFD.getTag('ActiveArea').value[3] = width
rawIFD.getTag('DefaultCropSize').value[0].num = width
rawIFD.getTag('DefaultCropSize').value[1].num = height
rawIFD.getTag('DefaultCropOrigin').value[0].num = 0
rawIFD.getTag('DefaultCropOrigin').value[1].num = 0

dng.writeDNG(outputDNG)

