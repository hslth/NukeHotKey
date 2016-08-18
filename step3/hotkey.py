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
        # exception handle
        # ←↑↓→ character should match Left, Up, Down, Right        
        keyException = {'Left':u'←',
                        'Up':u'↑',
                        'Down':u'↓',
                        'Right':u'→',
                        '{':'[',
                        '}':']',
                        '?':'/',
                        '|':'\\',
                        'Enter':'Return'
                    }
                    # some menu have both Enter or Return as key name
        
        for line in nuke.hotkeys().split('\n'):
            step = (len(line) - len(line.lstrip())-1)/4
            menuBuffer[step] = line.split('\t')[0].lstrip()
            # some item doen't have '\t' so check if \t is in line
            if '\t' in line:
                keySeq = line.split('\t')[-1]
                keyInfo = keySeq.split('+')[-1]
                if keyInfo:
                    # lets store the hotkey info to HotKeyButton instance.
                    # get HotKeyButton based on keyInfo
                    #
                    # most single key asigned hotkey -> self.keyDic[keyInfo[-1]]
                    # some keys like Backspace, Del ... check length then self.keyDic[keyInfo]
                    # this will give you the HotKeyButton                   
                    try:
                        if keyInfo in keyException.keys():
                            hkb = self.keyDic[keyException[keyInfo]]
                        elif len(keyInfo) > 1:
                            hkb = self.keyDic[keyInfo]
                        
                        else:
                            hkb = self.keyDic[keyInfo[-1]] 

                    except:
                        print "key assign error"
                        print repr(line), 'level :', step
                        print menuBuffer[:step+1], repr(keyInfo)
                    finally:
                        hkb.addKeyInfo(menuBuffer[0], '/'.join(menuBuffer[:step+1]), keySeq)
            
def show_hotkey():
    hotkey_dialog = HotKeyViewer(QtGui.QApplication.activeWindow())
    hotkey_dialog.show()

show_hotkey()
