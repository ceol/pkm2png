import struct
from StringIO import StringIO
from PIL import Image, ImageDraw

def _pack(data):
    return struct.pack('<' + ('B' * len(data)), data)

def _unpack(data):
    return struct.unpack('<' + ('B' * len(data)), data)

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
    
    length = len(data)
    if length % 4 != 0:
        raise ValueError('the pkm data supplied is incomplete')
    # The first pixel is always the header, so we need to add one to the
    # terminator.
    terminator = (length / 4) + 1

    data = _unpack(data)

    # a list of 4-item tuples representing pixels
    pixels = []

    # Header format:
    # R value: game generation
    # G value: terminator pixel
    # B value: unused
    # A value: unused
    pixels.append((gen,terminator,0,0))

    for i in count(start=0, step=4):
        if (i + 4) == (terminator - 1):
            break
        pixels.append(data[i])
    
    width = 10
    height = 6
    size = (width,height)

    # the PNG should default all-white
    color = (0,0,0,0)

    imgobj = Image.new('RGBA', size, color)
    drawobj = ImageDraw.Draw(imgobj)

    xpos = 0
    ypos = 0

    for pixel in pixels:
        drawobj.point((xpos,ypos), fill=pixel)

        # advance xpos but make sure it stays between 0 and width
        xpos = (xpos + 1) % width
        # if it's starting a new row, advance ypos
        if xpos == 0:
            ypos += 1
    
    # PIL's Image module requires the data to be a file buffer in order
    # to save. It's a complicated library, but image manipulation is a
    # complicated topic!
    imgbuffer = StringIO()
    imgobj.save(imgbuffer, format='PNG')
    
    # grab that data back out of the buffer
    imgdata = imgbuffer.getvalue()
    
    imgbuffer.close()

    return imgdata

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
    # PIL's Image module requires the data to be a file buffer in order
    # to open.
    imgbuffer = StringIO()
    imgbuffer.write(data)

    imgobj = Image.open(imgbuffer)
    pixels = list(imgobj.getdata())

    imgbuffer.close()

    # The first pixel is header information, and the 'R' value of that
    # header is the file's game generation.
    generation = pixels[0][0]
    # The 'G' value is the last pixel containing PKM data.
    terminator = pixels[0][1]

    bytedata = ''
    for pixel in pixels[1:terminator]:
        bytedata += struct.pack('BBBB', *pixel)
    
    return (generation, bytedata)