#!/usr/bin/python
# -*- coding: utf-8 -*-

import binascii
import sys
import os
import glob

def field_convert(int_h):
    h = float(int_h) / 79.9 + 3019.
    return h

    
def main():
    path = './'
    try:
        i_skip = int (input("How many points to skip between saving? S = "))
    except:
        i_skip = 1
        
    if i_skip <= 0 : i_skip = 1
    print ("Finally S = " + str(i_skip))

    for f_in in glob.glob( os.path.join(path, '*.epr') ):
        print ("current file is: " + f_in)
        try:
            f = open(f_in, 'rb')
            f_out = f_in + '.txt'
            d = open(f_out, 'w')
            d.write('field,G intensity,a.u.\n')

            i = 0
            for i in range(65520):
                a = f.read(1)
                b = f.read(1)
                h_field = field_convert(int(binascii.b2a_hex(b''.join([b,a])),16))
                a = f.read(1)
                b = f.read(1)
                intens = int(binascii.b2a_hex(b''.join([b,a])),16)
                if intens > 4096: break
                if i % i_skip == 0:
                    out_line = '{0:8.6}\t{1:6}\n'.format(h_field, intens)
                    d.write(out_line)
                #i += 1
     
        except Exception:
            print("Error while reading file") 
        finally:
            try:
                f.close()
                d.close()
            except:
                pass
        
    input("Press Enter to exit")

if __name__ == '__main__':
    main()

