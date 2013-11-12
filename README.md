CMV12000_DNG_Writer
===================
Example usage:
cat self_10ms.raw16 | python CMV12000toDNG.py

Note it expects a 16 bit image from the CMV12000, not an 8 bit

DNG.py - This is the main class. To use it, create an instance of DNG with a file passed in, and then either manually load specific parts of the file (header, first icd, subifds, images, etc.), or call readFullDNG that loads everything for you. The support for loading tiles needs to be finished, including for auto-determining whether the image is using tiles verse stripsand write code to figure out whether to read the image in tiles or strips. Current support is for strips.

DNGTags.py includes  classes for an IFD, and Tags. It also includes definitions of a mix of DNG/TIFF 6.0/TIFF/EP tags. The tags are not labeled with which which spec they come from. More tags may be added as needed. Technically Numpy isn't required to read/write the DNGs, but it is presently being used to enable more advanced image processing. If you don't want to use Numpy you could easily store the image in a different structure.

stripDNG.py - This was written to try and figure out which minimal set of tags were required to make a file readable by photoshop and lightroom. It seems to want a camera profile in there. Most other tags seemed unnecessary for a minimal DNG. Right now it creates an "Empty" DNG with a 1x1 image and minimal tags. The specs listed some required tags that photoshop didn't care about.

readCMV12000.py - This just reads in the raw image from the CMV12000 and displays a few pixel values to screen to show it could read it.

CMV12000toDNG.py - This reads in the "Empty" dng file, re-writes the organization, and cameraModel, reads in a CMV12000 image and writes it to a DNG. Right now it accepts the input CMV12000 image on std in. Herbert was wanting to have the program accept from std in and write to std out. The problem at the moment is to write the file I do a bunch of seeks. Down the road it would be possible to do it without seeks, but that will require computing offsets to the data in advance. For now the file is written out to "img.DNG", which can easily be changed. 