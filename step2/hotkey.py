# -*- coding: utf-8 -*-
"""
1. Check hotkeys (ex: "Nodes/Image/Write", "W")
2. Get HotKeyButton instance corresponding 'KEY' instance
3. Store Key information to HotKeyButton instance.
4. When the Button is clicked, print it to TextBrowser
5. Color HotKeyButton when 'Viewer', 'Nodes', 'Nuke' checkbox is checked.
"""

from PySide import QtCore, QtGui
import ui_hotkey
reload(ui_hotkey)

class HotKeyViewer(QtGui.QDialog):
    def __init__(self, parent=None):
        super(HotKeyViewer, self).__init__(parent)
        self.ui = ui_hotkey.Ui_Form()
        self.ui.setupUi(self)
        
        # get all HotKeyButton instance from ui_hotkey file        
        self.allHotKey = [ins for ins in self.ui.__dict__.values() if isinstance(ins, ui_hotkey.HotKeyButton)]
        
        # make dictionary {'K':HotKeyButton object, 'O':HotKeyButton,...}
        self.keyDic = {}
        for button in self.allHotKey:
            self.keyDic[button.text()] = button
        
        self.parse_hotkey()

    def parse_hotkey(self):
        menuBuffer = [''] * 10
        for line in nuke.hotkeys().split('\n'):
            step = (len(line) - len(line.lstrip())-1)/4
            menuBuffer[step] = line.split('\t')[0].lstrip()
            keyInfo = line.split('\t')[-1]
            print repr(line), 'level :', step
            print menuBuffer[:step+1], keyInfo
            print ""

            
def show_hotkey():
    hotkey_dialog = HotKeyViewer(QtGui.QApplication.activeWindow())
    hotkey_dialog.show()

show_hotkey()
