#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      jlegind
#
# Created:     26-10-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        toolbar = self.CreateToolBar()
        qtool = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('exit.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSize((250, 200))
        self.SetTitle('Simple toolbar')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()