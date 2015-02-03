import wx
import copy
from gui import bitmapLoader
import gui.mainFrame
import gui.globalEvents as GE
import time
from gui.PFListPane import PFListPane

from wx.lib.buttons import GenBitmapButton

import gui.utils.colorUtils as colorUtils
import gui.utils.drawUtils as drawUtils
import gui.utils.animUtils as animUtils
import gui.utils.animEffects as animEffects

import gui.sfBrowserItem as SFItem
from gui.contextMenu import ContextMenu

import service
import gui.utils.fonts as fonts

class CharacterBrowser(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__ (self, parent,style = 0)

        self._lastWidth = 0
        self._activeStage = 1
        self._lastStage = 0
        self.browseHist = []
        self.lastStage = (0,0)
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        layout = wx.HORIZONTAL

        container = wx.BoxSizer(wx.VERTICAL if layout == wx.HORIZONTAL else wx.HORIZONTAL)



        mainSizer.Add(container, 1, wx.EXPAND)
        self.SetSizer(mainSizer)
        self.Layout()
        self.Show()

