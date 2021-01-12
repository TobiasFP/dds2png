from wand import image
from lib.ddsparser import read_dds_signature, read_chunk
import struct
import zlib

def main():
    # f = open('input/002_50730.DDS', 'rb')
    f = open('input/hej.png', 'rb')
    read_dds_signature(f)



if __name__ == "__main__":
    # execute only if run as a script
    main()