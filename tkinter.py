#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     25-09-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from Tkinter import *
from ttk import *


def main():
    root = Tk()
    Button(root, text="Hello World").grid()
    root.mainloop()


if __name__ == '__main__':
    main()
