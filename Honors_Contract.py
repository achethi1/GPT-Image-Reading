#!/usr/bin/env python3

import binascii
import hashlib
import sys
import struct
import socket

def printAddresses(address):
    print("Table Start address:", address)
    part=0
    while part<128:
        newA=((address + 0x20) + (part* 0x80))
        newB=((address + 0x28) + (part* 0x80))
        newC=((address + 0x30) + (part* 0x80))
        startA = gpt[newA:newB].hex()
        endA =  gpt[newB : newC].hex()
        
        # Converting from big to little
        finalStartA= (int.from_bytes(bytes.fromhex(startA), 'big').to_bytes((int.from_bytes(bytes.fromhex(startA), 'big').bit_length() + 7) // 8, 'little')).hex()
        finalEndA=(int.from_bytes(bytes.fromhex(endA), 'big').to_bytes((int.from_bytes(bytes.fromhex(endA), 'big').bit_length() + 7) // 8, 'little')).hex()

        while len(finalStartA) < 16:
            finalStartA = finalStartA + '0'
        print("Partition Start address:", finalStartA)   
        while len(finalEndA) < 16:
            finalEndA = finalEndA + '0'
        print("Partition End address:", finalEndA)
        part=part+1

gpt=bytearray()
binary_file=open(sys.argv[1],'rb')
gpt=binary_file.read()
first = gpt[0x248:0x250].hex()
address= int(int.from_bytes(bytes.fromhex(first), 'big').to_bytes(((int.from_bytes(bytes.fromhex(first), 'big')).bit_length() + 7) // 8, 'little').hex()) * 512
printAddresses(address)