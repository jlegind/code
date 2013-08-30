#-------------------------------------------------------------------------------
# Name:        module4
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
import os

APP_EXIT = 1

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('exit.png'))
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.Quitter, id=APP_EXIT)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((250, 200))
        self.SetTitle('Icons and shortcuts')
        self.Centre()
        self.Show(True)

    def Quitter(self, e):
        self.Close()


def main():

    print os.getcwd()
    ex = wx.App(False)
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()