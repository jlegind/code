#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     08-03-2013
# Copyright:   (c) jlegind 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import string

letters = string.ascii_uppercase
low_letters = string.ascii_lowercase

def namerange():
    i = 0

    for j in letters:
        txt = j, letters[i], letters[i]
        txt2 = j, max(low_letters), max(low_letters)
        txt3 = [''.join(txt), ''.join(txt2)]
        yield txt3



def main():
    nr = namerange()

    for j in nr:
        if j[1] == 'Zzz':
            j[1] = 'zzz'

        print '\t'.join(j)

if __name__ == '__main__':
    main()
