# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hotkey.ui'
#
# Created: Tue Aug 16 19:40:13 2016
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!
try:
    from PyQt4 import QtCore, QtGui
except:
    from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1134, 536)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.keyGroup = QtGui.QGroupBox(self.tab)
        self.keyGroup.setMinimumSize(QtCore.QSize(650, 300))
        self.keyGroup.setObjectName(_fromUtf8("keyGroup"))
        self.pushButton_88 = HotKeyButton(self.keyGroup)
        self.pushButton_88.setGeometry(QtCore.QRect(445, 350, 50, 40))
        self.pushButton_88.setObjectName(_fromUtf8("pushButton_88"))
        self.pushButton_35 = HotKeyButton(self.keyGroup)
        self.pushButton_35.setGeometry(QtCore.QRect(320, 130, 40, 40))
        self.pushButton_35.setObjectName(_fromUtf8("pushButton_35"))
        self.pushButton_72 = HotKeyButton(self.keyGroup)
        self.pushButton_72.setGeometry(QtCore.QRect(420, 250, 40, 40))
        self.pushButton_72.setObjectName(_fromUtf8("pushButton_72"))
        self.pushButton_45 = HotKeyButton(self.keyGroup)
        self.pushButton_45.setGeometry(QtCore.QRect(170, 170, 40, 40))
        self.pushButton_45.setObjectName(_fromUtf8("pushButton_45"))
        self.pushButton_28 = HotKeyButton(self.keyGroup)
        self.pushButton_28.setGeometry(QtCore.QRect(20, 130, 60, 40))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.pushButton_73 = HotKeyButton(self.keyGroup)
        self.pushButton_73.setGeometry(QtCore.QRect(460, 250, 40, 40))
        self.pushButton_73.setCheckable(True)
        self.pushButton_73.setObjectName(_fromUtf8("pushButton_73"))
        self.pushButton_80 = HotKeyButton(self.keyGroup)
        self.pushButton_80.setGeometry(QtCore.QRect(500, 350, 40, 40))
        self.pushButton_80.setObjectName(_fromUtf8("pushButton_80"))
        self.pushButton_51 = HotKeyButton(self.keyGroup)
        self.pushButton_51.setGeometry(QtCore.QRect(410, 170, 40, 40))
        self.pushButton_51.setObjectName(_fromUtf8("pushButton_51"))
        self.pushButton_40 = HotKeyButton(self.keyGroup)
        self.pushButton_40.setGeometry(QtCore.QRect(520, 130, 40, 40))
        self.pushButton_40.setObjectName(_fromUtf8("pushButton_40"))
        self.pushButton_85 = HotKeyButton(self.keyGroup)
        self.pushButton_85.setGeometry(QtCore.QRect(445, 310, 50, 40))
        self.pushButton_85.setObjectName(_fromUtf8("pushButton_85"))
        self.pushButton_27 = HotKeyButton(self.keyGroup)
        self.pushButton_27.setGeometry(QtCore.QRect(540, 90, 80, 40))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.pushButton_57 = HotKeyButton(self.keyGroup)
        self.pushButton_57.setGeometry(QtCore.QRect(150, 210, 40, 40))
        self.pushButton_57.setObjectName(_fromUtf8("pushButton_57"))
        self.pushButton_37 = HotKeyButton(self.keyGroup)
        self.pushButton_37.setGeometry(QtCore.QRect(400, 130, 40, 40))
        self.pushButton_37.setObjectName(_fromUtf8("pushButton_37"))
        self.pushButton_84 = HotKeyButton(self.keyGroup)
        self.pushButton_84.setGeometry(QtCore.QRect(395, 310, 50, 40))
        self.pushButton_84.setObjectName(_fromUtf8("pushButton_84"))
        self.pushButton_18 = HotKeyButton(self.keyGroup)
        self.pushButton_18.setGeometry(QtCore.QRect(180, 90, 40, 40))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_36 = HotKeyButton(self.keyGroup)
        self.pushButton_36.setGeometry(QtCore.QRect(360, 130, 40, 40))
        self.pushButton_36.setObjectName(_fromUtf8("pushButton_36"))
        self.pushButton_3 = HotKeyButton(self.keyGroup)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 30, 40, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_46 = HotKeyButton(self.keyGroup)
        self.pushButton_46.setGeometry(QtCore.QRect(210, 170, 40, 40))
        self.pushButton_46.setObjectName(_fromUtf8("pushButton_46"))
        self.pushButton_2 = HotKeyButton(self.keyGroup)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 30, 40, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_41 = HotKeyButton(self.keyGroup)
        self.pushButton_41.setGeometry(QtCore.QRect(560, 130, 60, 40))
        self.pushButton_41.setObjectName(_fromUtf8("pushButton_41"))
        self.pushButton_29 = HotKeyButton(self.keyGroup)
        self.pushButton_29.setGeometry(QtCore.QRect(80, 130, 40, 40))
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.pushButton_67 = HotKeyButton(self.keyGroup)
        self.pushButton_67.setGeometry(QtCore.QRect(20, 250, 50, 40))
        self.pushButton_67.setCheckable(True)
        self.pushButton_67.setObjectName(_fromUtf8("pushButton_67"))
        self.pushButton_13 = HotKeyButton(self.keyGroup)
        self.pushButton_13.setGeometry(QtCore.QRect(580, 30, 40, 40))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_8 = HotKeyButton(self.keyGroup)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 30, 40, 40))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_74 = HotKeyButton(self.keyGroup)
        self.pushButton_74.setGeometry(QtCore.QRect(500, 250, 40, 40))
        self.pushButton_74.setObjectName(_fromUtf8("pushButton_74"))
        self.pushButton_52 = HotKeyButton(self.keyGroup)
        self.pushButton_52.setGeometry(QtCore.QRect(450, 170, 40, 40))
        self.pushButton_52.setObjectName(_fromUtf8("pushButton_52"))
        self.pushButton_86 = HotKeyButton(self.keyGroup)
        self.pushButton_86.setGeometry(QtCore.QRect(345, 350, 50, 40))
        self.pushButton_86.setObjectName(_fromUtf8("pushButton_86"))
        self.pushButton_64 = HotKeyButton(self.keyGroup)
        self.pushButton_64.setGeometry(QtCore.QRect(430, 210, 40, 40))
        self.pushButton_64.setObjectName(_fromUtf8("pushButton_64"))
        self.pushButton_58 = HotKeyButton(self.keyGroup)
        self.pushButton_58.setGeometry(QtCore.QRect(190, 210, 40, 40))
        self.pushButton_58.setObjectName(_fromUtf8("pushButton_58"))
        self.pushButton_5 = HotKeyButton(self.keyGroup)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 30, 40, 40))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_19 = HotKeyButton(self.keyGroup)
        self.pushButton_19.setGeometry(QtCore.QRect(220, 90, 40, 40))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.pushButton_63 = HotKeyButton(self.keyGroup)
        self.pushButton_63.setGeometry(QtCore.QRect(390, 210, 40, 40))
        self.pushButton_63.setObjectName(_fromUtf8("pushButton_63"))
        self.pushButton_15 = HotKeyButton(self.keyGroup)
        self.pushButton_15.setGeometry(QtCore.QRect(60, 90, 40, 40))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.pushButton_47 = HotKeyButton(self.keyGroup)
        self.pushButton_47.setGeometry(QtCore.QRect(250, 170, 40, 40))
        self.pushButton_47.setObjectName(_fromUtf8("pushButton_47"))
        self.pushButton_42 = HotKeyButton(self.keyGroup)
        self.pushButton_42.setGeometry(QtCore.QRect(20, 170, 70, 40))
        self.pushButton_42.setObjectName(_fromUtf8("pushButton_42"))
        self.pushButton_9 = HotKeyButton(self.keyGroup)
        self.pushButton_9.setGeometry(QtCore.QRect(390, 30, 40, 40))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_23 = HotKeyButton(self.keyGroup)
        self.pushButton_23.setGeometry(QtCore.QRect(380, 90, 40, 40))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.pushButton_83 = HotKeyButton(self.keyGroup)
        self.pushButton_83.setGeometry(QtCore.QRect(345, 310, 50, 40))
        self.pushButton_83.setObjectName(_fromUtf8("pushButton_83"))
        self.pushButton_75 = HotKeyButton(self.keyGroup)
        self.pushButton_75.setGeometry(QtCore.QRect(540, 250, 40, 40))
        self.pushButton_75.setObjectName(_fromUtf8("pushButton_75"))
        self.pushButton_53 = HotKeyButton(self.keyGroup)
        self.pushButton_53.setGeometry(QtCore.QRect(490, 170, 40, 40))
        self.pushButton_53.setObjectName(_fromUtf8("pushButton_53"))
        self.pushButton_32 = HotKeyButton(self.keyGroup)
        self.pushButton_32.setGeometry(QtCore.QRect(200, 130, 40, 40))
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.pushButton_7 = HotKeyButton(self.keyGroup)
        self.pushButton_7.setGeometry(QtCore.QRect(310, 30, 40, 40))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_59 = HotKeyButton(self.keyGroup)
        self.pushButton_59.setGeometry(QtCore.QRect(230, 210, 40, 40))
        self.pushButton_59.setObjectName(_fromUtf8("pushButton_59"))
        self.pushButton_14 = HotKeyButton(self.keyGroup)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 90, 40, 40))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.pushButton_69 = HotKeyButton(self.keyGroup)
        self.pushButton_69.setGeometry(QtCore.QRect(120, 250, 50, 40))
        self.pushButton_69.setCheckable(True)
        self.pushButton_69.setObjectName(_fromUtf8("pushButton_69"))
        self.pushButton_20 = HotKeyButton(self.keyGroup)
        self.pushButton_20.setGeometry(QtCore.QRect(260, 90, 40, 40))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.pushButton_48 = HotKeyButton(self.keyGroup)
        self.pushButton_48.setGeometry(QtCore.QRect(290, 170, 40, 40))
        self.pushButton_48.setObjectName(_fromUtf8("pushButton_48"))
        self.pushButton_79 = HotKeyButton(self.keyGroup)
        self.pushButton_79.setGeometry(QtCore.QRect(540, 310, 40, 40))
        self.pushButton_79.setObjectName(_fromUtf8("pushButton_79"))
        self.pushButton_10 = HotKeyButton(self.keyGroup)
        self.pushButton_10.setGeometry(QtCore.QRect(460, 30, 40, 40))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_24 = HotKeyButton(self.keyGroup)
        self.pushButton_24.setGeometry(QtCore.QRect(420, 90, 40, 40))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.pushButton_31 = HotKeyButton(self.keyGroup)
        self.pushButton_31.setGeometry(QtCore.QRect(160, 130, 40, 40))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.pushButton_76 = HotKeyButton(self.keyGroup)
        self.pushButton_76.setGeometry(QtCore.QRect(580, 250, 40, 40))
        self.pushButton_76.setCheckable(True)
        self.pushButton_76.setObjectName(_fromUtf8("pushButton_76"))
        self.pushButton_54 = HotKeyButton(self.keyGroup)
        self.pushButton_54.setGeometry(QtCore.QRect(530, 170, 91, 40))
        self.pushButton_54.setObjectName(_fromUtf8("pushButton_54"))
        self.pushButton_33 = HotKeyButton(self.keyGroup)
        self.pushButton_33.setGeometry(QtCore.QRect(240, 130, 40, 40))
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.pushButton_60 = HotKeyButton(self.keyGroup)
        self.pushButton_60.setGeometry(QtCore.QRect(270, 210, 40, 40))
        self.pushButton_60.setObjectName(_fromUtf8("pushButton_60"))
        self.pushButton_70 = HotKeyButton(self.keyGroup)
        self.pushButton_70.setGeometry(QtCore.QRect(170, 250, 50, 40))
        self.pushButton_70.setObjectName(_fromUtf8("pushButton_70"))
        self.pushButton_66 = HotKeyButton(self.keyGroup)
        self.pushButton_66.setGeometry(QtCore.QRect(510, 210, 110, 40))
        self.pushButton_66.setCheckable(True)
        self.pushButton_66.setObjectName(_fromUtf8("pushButton_66"))
        self.pushButton_43 = HotKeyButton(self.keyGroup)
        self.pushButton_43.setGeometry(QtCore.QRect(90, 170, 40, 40))
        self.pushButton_43.setObjectName(_fromUtf8("pushButton_43"))
        self.pushButton_82 = HotKeyButton(self.keyGroup)
        self.pushButton_82.setGeometry(QtCore.QRect(580, 350, 40, 40))
        self.pushButton_82.setObjectName(_fromUtf8("pushButton_82"))
        self.pushButton_21 = HotKeyButton(self.keyGroup)
        self.pushButton_21.setGeometry(QtCore.QRect(300, 90, 40, 40))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.pushButton_68 = HotKeyButton(self.keyGroup)
        self.pushButton_68.setGeometry(QtCore.QRect(70, 250, 50, 40))
        self.pushButton_68.setObjectName(_fromUtf8("pushButton_68"))
        self.pushButton_49 = HotKeyButton(self.keyGroup)
        self.pushButton_49.setGeometry(QtCore.QRect(330, 170, 40, 40))
        self.pushButton_49.setObjectName(_fromUtf8("pushButton_49"))
        self.pushButton_38 = HotKeyButton(self.keyGroup)
        self.pushButton_38.setGeometry(QtCore.QRect(440, 130, 40, 40))
        self.pushButton_38.setObjectName(_fromUtf8("pushButton_38"))
        self.pushButton_81 = HotKeyButton(self.keyGroup)
        self.pushButton_81.setGeometry(QtCore.QRect(540, 350, 40, 40))
        self.pushButton_81.setObjectName(_fromUtf8("pushButton_81"))
        self.pushButton_65 = HotKeyButton(self.keyGroup)
        self.pushButton_65.setGeometry(QtCore.QRect(470, 210, 40, 40))
        self.pushButton_65.setObjectName(_fromUtf8("pushButton_65"))
        self.pushButton_11 = HotKeyButton(self.keyGroup)
        self.pushButton_11.setGeometry(QtCore.QRect(500, 30, 40, 40))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_25 = HotKeyButton(self.keyGroup)
        self.pushButton_25.setGeometry(QtCore.QRect(460, 90, 40, 40))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.pushButton_17 = HotKeyButton(self.keyGroup)
        self.pushButton_17.setGeometry(QtCore.QRect(140, 90, 40, 40))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.pushButton_55 = HotKeyButton(self.keyGroup)
        self.pushButton_55.setGeometry(QtCore.QRect(20, 210, 90, 40))
        self.pushButton_55.setCheckable(True)
        self.pushButton_55.setObjectName(_fromUtf8("pushButton_55"))
        self.pushButton_30 = HotKeyButton(self.keyGroup)
        self.pushButton_30.setGeometry(QtCore.QRect(120, 130, 40, 40))
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.pushButton_6 = HotKeyButton(self.keyGroup)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 30, 40, 40))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_34 = HotKeyButton(self.keyGroup)
        self.pushButton_34.setGeometry(QtCore.QRect(280, 130, 40, 40))
        self.pushButton_34.setObjectName(_fromUtf8("pushButton_34"))
        self.pushButton_61 = HotKeyButton(self.keyGroup)
        self.pushButton_61.setGeometry(QtCore.QRect(310, 210, 40, 40))
        self.pushButton_61.setObjectName(_fromUtf8("pushButton_61"))
        self.pushButton_4 = HotKeyButton(self.keyGroup)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 30, 40, 40))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_71 = HotKeyButton(self.keyGroup)
        self.pushButton_71.setGeometry(QtCore.QRect(220, 250, 201, 40))
        self.pushButton_71.setObjectName(_fromUtf8("pushButton_71"))
        self.pushButton_44 = HotKeyButton(self.keyGroup)
        self.pushButton_44.setGeometry(QtCore.QRect(130, 170, 40, 40))
        self.pushButton_44.setObjectName(_fromUtf8("pushButton_44"))
        self.pushButton_16 = HotKeyButton(self.keyGroup)
        self.pushButton_16.setGeometry(QtCore.QRect(100, 90, 40, 40))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_22 = HotKeyButton(self.keyGroup)
        self.pushButton_22.setGeometry(QtCore.QRect(340, 90, 40, 40))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.pushButton_87 = HotKeyButton(self.keyGroup)
        self.pushButton_87.setGeometry(QtCore.QRect(395, 350, 50, 40))
        self.pushButton_87.setObjectName(_fromUtf8("pushButton_87"))
        self.pushButton = HotKeyButton(self.keyGroup)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 40, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_50 = HotKeyButton(self.keyGroup)
        self.pushButton_50.setGeometry(QtCore.QRect(370, 170, 40, 40))
        self.pushButton_50.setObjectName(_fromUtf8("pushButton_50"))
        self.pushButton_39 = HotKeyButton(self.keyGroup)
        self.pushButton_39.setGeometry(QtCore.QRect(480, 130, 40, 40))
        self.pushButton_39.setObjectName(_fromUtf8("pushButton_39"))
        self.pushButton_12 = HotKeyButton(self.keyGroup)
        self.pushButton_12.setGeometry(QtCore.QRect(540, 30, 40, 40))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_26 = HotKeyButton(self.keyGroup)
        self.pushButton_26.setGeometry(QtCore.QRect(500, 90, 40, 40))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.pushButton_62 = HotKeyButton(self.keyGroup)
        self.pushButton_62.setGeometry(QtCore.QRect(350, 210, 40, 40))
        self.pushButton_62.setObjectName(_fromUtf8("pushButton_62"))
        self.pushButton_56 = HotKeyButton(self.keyGroup)
        self.pushButton_56.setGeometry(QtCore.QRect(110, 210, 40, 40))
        self.pushButton_56.setObjectName(_fromUtf8("pushButton_56"))
        self.gridLayout_3.addWidget(self.keyGroup, 1, 0, 1, 3)
        self.viewerFocusGroup = QtGui.QGroupBox(self.tab)
        self.viewerFocusGroup.setMaximumSize(QtCore.QSize(16777215, 50))
        self.viewerFocusGroup.setObjectName(_fromUtf8("viewerFocusGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.viewerFocusGroup)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.viewerCheckBox = QtGui.QCheckBox(self.viewerFocusGroup)
        self.viewerCheckBox.setObjectName(_fromUtf8("viewerCheckBox"))
        self.gridLayout_4.addWidget(self.viewerCheckBox, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.viewerFocusGroup, 0, 2, 1, 1)
        self.mainFocusGroup = QtGui.QGroupBox(self.tab)
        self.mainFocusGroup.setMaximumSize(QtCore.QSize(16777215, 50))
        self.mainFocusGroup.setObjectName(_fromUtf8("mainFocusGroup"))
        self.gridLayout_2 = QtGui.QGridLayout(self.mainFocusGroup)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.nukeCheckBox = QtGui.QCheckBox(self.mainFocusGroup)
        self.nukeCheckBox.setObjectName(_fromUtf8("nukeCheckBox"))
        self.gridLayout_2.addWidget(self.nukeCheckBox, 0, 0, 1, 1)
        self.nodesCheckBox = QtGui.QCheckBox(self.mainFocusGroup)
        self.nodesCheckBox.setObjectName(_fromUtf8("nodesCheckBox"))
        self.gridLayout_2.addWidget(self.nodesCheckBox, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.mainFocusGroup, 0, 0, 1, 2)
        self.hotkeyTextEdit = QtGui.QTextEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hotkeyTextEdit.sizePolicy().hasHeightForWidth())
        self.hotkeyTextEdit.setSizePolicy(sizePolicy)
        self.hotkeyTextEdit.setObjectName(_fromUtf8("hotkeyTextEdit"))
        self.gridLayout_3.addWidget(self.hotkeyTextEdit, 0, 3, 2, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.keyGroup.setTitle(_translate("Form", "Keyboard", None))
        self.pushButton_88.setText(_translate("Form", "PgDown", None))
        self.pushButton_35.setText(_translate("Form", "U", None))
        self.pushButton_72.setText(_translate("Form", "kr/en", None))
        self.pushButton_45.setText(_translate("Form", "D", None))
        self.pushButton_28.setText(_translate("Form", "Tab", None))
        self.pushButton_73.setText(_translate("Form", "Alt", None))
        self.pushButton_80.setText(_translate("Form", "←", None))
        self.pushButton_51.setText(_translate("Form", "L", None))
        self.pushButton_40.setText(_translate("Form", "]", None))
        self.pushButton_85.setText(_translate("Form", "PgUp", None))
        self.pushButton_27.setText(_translate("Form", "Backspace", None))
        self.pushButton_57.setText(_translate("Form", "X", None))
        self.pushButton_37.setText(_translate("Form", "O", None))
        self.pushButton_84.setText(_translate("Form", "Home", None))
        self.pushButton_18.setText(_translate("Form", "4", None))
        self.pushButton_36.setText(_translate("Form", "I", None))
        self.pushButton_3.setText(_translate("Form", "F2", None))
        self.pushButton_46.setText(_translate("Form", "F", None))
        self.pushButton_2.setText(_translate("Form", "F1", None))
        self.pushButton_41.setText(_translate("Form", "\\", None))
        self.pushButton_29.setText(_translate("Form", "Q", None))
        self.pushButton_67.setText(_translate("Form", "Ctrl", None))
        self.pushButton_13.setText(_translate("Form", "F12", None))
        self.pushButton_8.setText(_translate("Form", "F7", None))
        self.pushButton_74.setText(_translate("Form", "Win", None))
        self.pushButton_52.setText(_translate("Form", ";", None))
        self.pushButton_86.setText(_translate("Form", "Del", None))
        self.pushButton_64.setText(_translate("Form", ".", None))
        self.pushButton_58.setText(_translate("Form", "C", None))
        self.pushButton_5.setText(_translate("Form", "F4", None))
        self.pushButton_19.setText(_translate("Form", "5", None))
        self.pushButton_63.setText(_translate("Form", ",", None))
        self.pushButton_15.setText(_translate("Form", "1", None))
        self.pushButton_47.setText(_translate("Form", "G", None))
        self.pushButton_42.setText(_translate("Form", "Caps\n"
"Lock", None))
        self.pushButton_9.setText(_translate("Form", "F8", None))
        self.pushButton_23.setText(_translate("Form", "9", None))
        self.pushButton_83.setText(_translate("Form", "Insert", None))
        self.pushButton_75.setText(_translate("Form", "Win", None))
        self.pushButton_53.setText(_translate("Form", "\'", None))
        self.pushButton_32.setText(_translate("Form", "R", None))
        self.pushButton_7.setText(_translate("Form", "F6", None))
        self.pushButton_59.setText(_translate("Form", "V", None))
        self.pushButton_14.setText(_translate("Form", "`", None))
        self.pushButton_69.setText(_translate("Form", "Alt", None))
        self.pushButton_20.setText(_translate("Form", "6", None))
        self.pushButton_48.setText(_translate("Form", "H", None))
        self.pushButton_79.setText(_translate("Form", "↑", None))
        self.pushButton_10.setText(_translate("Form", "F9", None))
        self.pushButton_24.setText(_translate("Form", "0", None))
        self.pushButton_31.setText(_translate("Form", "E", None))
        self.pushButton_76.setText(_translate("Form", "Ctrl", None))
        self.pushButton_54.setText(_translate("Form", "Return", None))
        self.pushButton_33.setText(_translate("Form", "T", None))
        self.pushButton_60.setText(_translate("Form", "B", None))
        self.pushButton_70.setText(_translate("Form", "Meta", None))
        self.pushButton_66.setText(_translate("Form", "Shift", None))
        self.pushButton_43.setText(_translate("Form", "A", None))
        self.pushButton_82.setText(_translate("Form", "→", None))
        self.pushButton_21.setText(_translate("Form", "7", None))
        self.pushButton_68.setText(_translate("Form", "Win", None))
        self.pushButton_49.setText(_translate("Form", "J", None))
        self.pushButton_38.setText(_translate("Form", "P", None))
        self.pushButton_81.setText(_translate("Form", "↓", None))
        self.pushButton_65.setText(_translate("Form", "/", None))
        self.pushButton_11.setText(_translate("Form", "F10", None))
        self.pushButton_25.setText(_translate("Form", "-", None))
        self.pushButton_17.setText(_translate("Form", "3", None))
        self.pushButton_55.setText(_translate("Form", "Shift", None))
        self.pushButton_30.setText(_translate("Form", "W", None))
        self.pushButton_6.setText(_translate("Form", "F5", None))
        self.pushButton_34.setText(_translate("Form", "Y", None))
        self.pushButton_61.setText(_translate("Form", "N", None))
        self.pushButton_4.setText(_translate("Form", "F3", None))
        self.pushButton_71.setText(_translate("Form", "Space", None))
        self.pushButton_44.setText(_translate("Form", "S", None))
        self.pushButton_16.setText(_translate("Form", "2", None))
        self.pushButton_22.setText(_translate("Form", "8", None))
        self.pushButton_87.setText(_translate("Form", "End", None))
        self.pushButton.setText(_translate("Form", "Esc", None))
        self.pushButton_50.setText(_translate("Form", "K", None))
        self.pushButton_39.setText(_translate("Form", "[", None))
        self.pushButton_12.setText(_translate("Form", "F11", None))
        self.pushButton_26.setText(_translate("Form", "=", None))
        self.pushButton_62.setText(_translate("Form", "M", None))
        self.pushButton_56.setText(_translate("Form", "Z", None))
        self.viewerFocusGroup.setTitle(_translate("Form", "Viewer Focus", None))
        self.viewerCheckBox.setText(_translate("Form", "Viewer", None))
        self.mainFocusGroup.setTitle(_translate("Form", "Main Focus", None))
        self.nukeCheckBox.setText(_translate("Form", "Nuke", None))
        self.nodesCheckBox.setText(_translate("Form", "Nodes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Hot Key List", None))

class HotKeyButton(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(HotKeyButton, self).__init__(parent)
        
        self.menuDic = {'Viewer':[],
                        'Nodes':[],
                        'Nuke':[]
                        }
                      
    def addKeyInfo(self, root, node, key):
        self.menuDic[root].append([node, key])           

    def getKeyInfo(self, root=None):
        if root:
            return self.menuDic[root]
        else:
            menus = []
            for menu in self.menuDic:
                menus += self.menuDic[menu]
            return menus           
          
        
