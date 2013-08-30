#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jlegind
#
# Created:     15-10-2012
# Copyright:   (c) jlegind 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hi GBIF") # A Frame is a top-level window.
frame.Show(True)     # Show the frame.
app.MainLoop()