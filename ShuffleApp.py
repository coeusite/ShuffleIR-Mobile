#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade not found on Thu Oct 29 19:31:31 2015 from "/home/devin/Documents/ShuffleIR-Mobile/ShuffleFrame.wxg"
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from frameShuffleNew import frameShuffleNew

class ShuffleIR(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = frameShuffleNew(None, wx.ID_ANY, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        return 1

# end of class ShuffleIR

if __name__ == "__main__":
    gettext.install("ShuffleApp") # replace with the appropriate catalog name

    ShuffleApp = ShuffleIR(0)
    ShuffleApp.MainLoop()