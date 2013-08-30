#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     29-05-2013
# Copyright:   (c) jlegind 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

def main():

    file=codecs.open('E:/Goth/occurrence.txt', mode="r", encoding="utf-8-sig")
    print file.readline()
    print file.readline()

    file.close()

if __name__ == '__main__':
    main()
