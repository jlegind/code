#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jlegind
#
# Created:     25-10-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python


import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(400,200))

        self.Move((0,0))
        self.Centre()
        self.Show()

if __name__ == '__main__':

    app = wx.App(False)
    ed = Example(None, title='Dead center')

    app.MainLoop()