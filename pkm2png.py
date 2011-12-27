from struct import pack, unpack
from StringIO import StringIO
from PIL import Image, ImageDraw

def _pack(data):
    return pack('<' + ('B' * len(data)), data)

def _unpack(data):
    return unpack('<' + ('B' * len(data)), data)

def pkm2png(gen, data):
    """Convert a PKM file to a PNG image.

    The file data is unpacked as individual bytes in a tuple. An empty image
    is then created and the unpacked tuple is looped over with every four
    bytes being placed in a four-item tuple and appended to a list.

    An empty PNG is created with the game generation located as the 'R'
    value of the first pixel. This set of four bytes functions as the
    header, carrying any extra data.

    The list of tuples is then looped over, using each tuple as the fill
    value for a pixel (RGBA being four 8-bit numbers).

    Keyword arguments:
    gen (int) -- the file's game generation
    data (string) -- the file data as a bytestring
    """
    # PIL's Image module requires the data to be a string buffer in order
    # to save.
    pass

def png2pkm(data):
    """Convert a PNG image to a PKM file.

    The PIL.Image module contains a useful method `getdata()` which returns
    a sequence object containing each pixel of the image as a tuple of pixel
    values (in our case, the RGBA values). What this function does is calls
    that method, flattens the returned object into a list, loops over
    the list, and appends each pixel value to the end of an empty PKM file.

    Keyword arguments:
    data (string) -- the file data as a bytestring
    """
    # PIL's Image module requires the data to be a string buffer in order
    # to open.
    pass