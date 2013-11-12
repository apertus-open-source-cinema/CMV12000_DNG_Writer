import struct, collections
import numpy as np
from math import *
from DNGTags import *
from DNG import *

def addTag(dict, ifd, tagName):
    dict[DNG_TAGS_STR_ID[tagName]] = ifd.getTag(tagName)
def delTag(ifd, tagName):
    del ifd.tags[DNG_TAGS_STR_ID[tagName]]
emptyDNG = 'IMG_1736.dng'
outputDNG = 'empty2.dng'
dng = DNG(emptyDNG)
dng.openDNG()
dng.readHeader()
dng.readIFDs()
#dng.printIDFs()
print len(dng.ifd.tags)
# Tag 254: 1 if offset is thumbnail, else 0
dng.readSubIFD('SubIFDs')
#dng.ifd.printSubIFDs()
#print len(dng.ifd.subIFDs[0].tags)

print dng.ifd.subIFDs[0].image[0:32,0:32]
dng.ifd.subIFDs.remove(dng.ifd.subIFDs[1])
requiredTags = {}
#addTag(requiredTags, dng.ifd, 'NewSubfileType')
#addTag(requiredTags, dng.ifd, 'ImageWidth')
#addTag(requiredTags, dng.ifd, 'ImageLength')
#addTag(requiredTags, dng.ifd, 'BitsPerSample')
#addTag(requiredTags, dng.ifd, 'PhotometricInterpretation')
#addTag(requiredTags, dng.ifd, 'Make')
#addTag(requiredTags, dng.ifd, 'Model')
#addTag(requiredTags, dng.ifd, 'StripOffsets')
#addTag(requiredTags, dng.ifd, 'Orientation')
#addTag(requiredTags, dng.ifd, 'SamplesPerPixel')
#addTag(requiredTags, dng.ifd, 'RowsPerStrip')
#addTag(requiredTags, dng.ifd, 'StripByteCounts')
##addTag(requiredTags, dng.ifd, 'Software')
#addTag(requiredTags, dng.ifd, 'DateTime')
#addTag(requiredTags, dng.ifd, 'SubIFDs')
#addTag(requiredTags, dng.ifd, 'DNGVersion')
#addTag(requiredTags, dng.ifd, 'DNGBackwardVersion')
#addTag(requiredTags, dng.ifd, 'UniqueCameraModel')
#dng.ifd.tags.clear()
#dng.ifd.tags.update(requiredTags)
#rawIFD = dng.ifd.subIFDs[0]
#dng.ifd = rawIFD

delTag(dng.ifd,'NewSubfileType')
delTag(dng.ifd,'ImageWidth')
delTag(dng.ifd,'ImageLength')
delTag(dng.ifd,'BitsPerSample')
delTag(dng.ifd,'Compression')
delTag(dng.ifd,'Software')
delTag(dng.ifd,'PhotometricInterpretation')
delTag(dng.ifd,'StripOffsets')
delTag(dng.ifd,'Orientation')
delTag(dng.ifd,'SamplesPerPixel')
delTag(dng.ifd,'RowsPerStrip')
delTag(dng.ifd,'StripByteCounts')
delTag(dng.ifd,'PlanarConfiguration')


#delTag(dng.ifd,'ColorMatrix1')
#delTag(dng.ifd,'ColorMatrix2')
#delTag(dng.ifd,'CalibrationIlluminant1')
#delTag(dng.ifd,'CalibrationIlluminant2')
#delTag(dng.ifd,'CameraCalibrationSignature')
#delTag(dng.ifd,'ProfileCalibrationSignature')
#delTag(dng.ifd,'ProfileName')
#delTag(dng.ifd,'ProfileToneCurve')
#delTag(dng.ifd,'ProfileEmbedPolicy')
#delTag(dng.ifd,'ProfileCopyright')

#delTag(dng.ifd,'ForwardMatrix1')
#delTag(dng.ifd,'ForwardMatrix2')
#delTag(dng.ifd,'ProfileLookTableDims')
#delTag(dng.ifd,'ProfileLookTableData')
#delTag(dng.ifd,'CameraCalibration1')
#delTag(dng.ifd,'CameraCalibration2')


delTag(dng.ifd,'LinearResponseLimit')
delTag(dng.ifd,'ShadowScale')
delTag(dng.ifd,'AnalogBalance')

delTag(dng.ifd,'PreviewApplicationName')
delTag(dng.ifd,'PreviewApplicationVersion')
delTag(dng.ifd,'PreviewSettingsDigest')
delTag(dng.ifd,'PreviewColorSpace')
delTag(dng.ifd,'PreviewDateTime')
delTag(dng.ifd,'NoiseProfile')
delTag(dng.ifd,'DNGPrivateData')
delTag(dng.ifd,'RawDataUniqueID')
#delTag(dng.ifd,'OriginalRawFileName')

delTag(dng.ifd,'AsShotNeutral')
delTag(dng.ifd,'BaselineExposure')
delTag(dng.ifd,'BaselineNoise')
delTag(dng.ifd,'BaselineSharpness')
delTag(dng.ifd,'LensInfo')

#delTag(dng.ifd,'Unknown3')
delTag(dng.ifd,'Unknown2')
delTag(dng.ifd,'Unknown1')

makeTag = dng.ifd.getTag('Make')
makeTag.value = "Apertus"
makeTag.count = len(makeTag.value)
modelTag = dng.ifd.getTag('Model')
modelTag.value = "Apertus Axiom Alpha"
modelTag.count = len(modelTag.value)
origRawFileNameTag = dng.ifd.getTag('OriginalRawFileName')
origRawFileNameTag.value = emptyDNG
origRawFileNameTag.count = len(origRawFileNameTag.value)

camCalTag = dng.ifd.getTag('CameraCalibrationSignature')
camCalTag.value = "Apertus"
camCalTag.count = len(camCalTag.value)
profCalTag = dng.ifd.getTag('ProfileCalibrationSignature')
profCalTag.value = "Apertus"
profCalTag.count = len(profCalTag.value)

# Create empty image
width = 1
height = 1
numPixels = width*height
rawFlatImage = np.zeros(numPixels,dtype=np.uint16)
rawImage = np.reshape(rawFlatImage,(height,width))

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
# Replace Image
'''
width = 4096
height = 3072
numPixels = width*height
rawFile = 'self_10ms.raw16'
rf = open(rawFile, mode='rb')
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
'''

dng.writeDNG(outputDNG)


#import scipy
#image = np.zeros((dng.imageHeight,dng.imageWidth),dtype=np.uint8)
#image[:,:] = (dng.image[:,:]+0.0)/4000*255
#scipy.misc.imsave('testOut.png', dng.image)
