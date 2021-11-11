#!/usr/bin/env python3
from configparser import ConfigParser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox
import os.path
from os.path import exists
selgrp = ""


class Ui_FormSettings(object):
    def setupUi(self, FormSettings):
        self.MainWindow = FormSettings
        FormSettings.setObjectName("FormSettings")
        FormSettings.resize(678, 360)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("USA-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormSettings.setWindowIcon(icon)
        self.lineEdit = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(FormSettings)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FormSettings)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 50, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(FormSettings)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FormSettings)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 110, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 140, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(FormSettings)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 80, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(FormSettings)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 240, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(FormSettings)
        self.pushButton.setGeometry(QtCore.QRect(444, 290, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.setInfo)
        self.pushButton_2 = QtWidgets.QPushButton(FormSettings)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 290, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.MainWindow.close)
        self.radioButton = QtWidgets.QRadioButton(FormSettings)
        self.radioButton.setGeometry(QtCore.QRect(530, 60, 89, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(FormSettings)
        self.radioButton_2.setGeometry(QtCore.QRect(530, 80, 89, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_7 = QtWidgets.QLabel(FormSettings)
        self.label_7.setGeometry(QtCore.QRect(510, 40, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 170, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(FormSettings)
        self.label_8.setGeometry(QtCore.QRect(30, 170, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(FormSettings)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(FormSettings)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 200, 113, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.retranslateUi(FormSettings)
        QtCore.QMetaObject.connectSlotsByName(FormSettings)

        self.MainWindow.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowStaysOnTopHint
        )


    def retranslateUi(self, FormSettings):
        _translate = QtCore.QCoreApplication.translate
        FormSettings.setWindowTitle(_translate("FormSettings", "Settings"))
        self.label.setText(_translate("FormSettings", "Enter Legal Callsign :"))
        self.label_2.setText(_translate("FormSettings", "Enter Callsign Suffix :"))
        self.label_3.setText(_translate("FormSettings", "Enter Group 2 :"))
        self.label_4.setText(_translate("FormSettings", "Enter Group 1 :"))
        self.label_5.setText(_translate("FormSettings", "Enter 4 Digit Grid :"))
        self.label_6.setText(_translate("FormSettings", "Enter Path to JS8Call Directed.TXT"))
        self.pushButton.setText(_translate("FormSettings", "Save Settings"))
        self.pushButton_2.setText(_translate("FormSettings", "Cancel"))
        self.radioButton.setText(_translate("FormSettings", "Group1"))
        self.radioButton_2.setText(_translate("FormSettings", "Group2"))
        self.label_7.setText(_translate("FormSettings", "Active Group"))
        self.lineEdit_7.setText(_translate("FormSettings", "127.0.0.1"))
        self.label_8.setText(_translate("FormSettings", "Server :"))
        self.label_9.setText(_translate("FormSettings", "UDP Port :"))
        self.lineEdit_8.setText(_translate("FormSettings", "2242"))

        self.lineEdit.textChanged.connect(self.callval)
        self.lineEdit_2.textChanged.connect(self.suffval)
        self.lineEdit_3.textChanged.connect(self.grp1val)
        self.lineEdit_4.textChanged.connect(self.grp2val)
        self.lineEdit_5.textChanged.connect(self.gridval)

        call = self.lineEdit
        call.setMaxLength(6)
        suff = self.lineEdit_2
        suff.setMaxLength(2)
        grp1 = self.lineEdit_3
        grp1.setMaxLength(7)
        grp2 = self.lineEdit_4
        grp2.setMaxLength(7)
        grd = self.lineEdit_5
        grd.setMaxLength(4)
        self.getConfig()



    def on_close(self):
        self.MainWindow.close()

    def getConfig(self):
        if os.path.exists("config.ini"):
            config_object = ConfigParser()
            config_object.read("config.ini")
            userinfo = config_object["USERINFO"]
            # print("callsign is {}".format(userinfo["callsign"]))
            print("callsignsuffix is {}".format(userinfo["callsignsuffix"]))
            print("group1 is {}".format(userinfo["group1"]))
            print("group2 is {}".format(userinfo["group2"]))
            print("grid is {}".format(userinfo["grid"]))
            systeminfo = config_object["DIRECTEDCONFIG"]
            print("file path  is {}".format(systeminfo["path"]))
            callsign = format(userinfo["callsign"])
            callsignSuffix = format(userinfo["callsignsuffix"])
            group1 = format(userinfo["group1"])
            group2 = format(userinfo["group2"])
            grid = format(userinfo["grid"])
            path = format(systeminfo["path"])
            server = format(systeminfo["server"])
            port = format(systeminfo["port"])
            selectedgroup = format(userinfo["selectedgroup"])
            if (selectedgroup == group2):
                self.radioButton_2.setChecked(True)
            else:
                self.radioButton.setChecked(True)
            self.lineEdit.setText(str(callsign))
            self.lineEdit_2.setText(str(callsignSuffix))
            self.lineEdit_3.setText(str(group1))
            self.lineEdit_4.setText(str(group2))
            self.lineEdit_5.setText(str(grid))
            self.lineEdit_6.setText(str(path))
            self.lineEdit_7.setText(str(server))
            self.lineEdit_8.setText(str(port))

    def setInfo(self):
        # printing the form information
        print("legal Callsign : {0}".format(self.lineEdit.text()))
        print("Callsign Suffix : {0}".format(self.lineEdit_2.text()))
        print("Group 1 : {0} ".format(self.lineEdit_3.text()))
        print("Group 2 : {0}".format(self.lineEdit_4.text()))
        print("GRID: {0}".format(self.lineEdit_5.text()))
        print("PATH : {0} ".format(self.lineEdit_6.text()))
        callsign = self.lineEdit.text()
        callsignSuffix = self.lineEdit_2.text()
        group1 = self.lineEdit_3.text()
        group2 = self.lineEdit_4.text()
        grid = self.lineEdit_5.text()
        path = self.lineEdit_6.text()
        server = self.lineEdit_7.text()
        port = self.lineEdit_8.text()
        global selgrp
        if (self.radioButton.isChecked() == True):
            selgrp = group1
            print(selgrp)

        if (self.radioButton_2.isChecked() == True):
            if len(group2) < 4:
                msg = QMessageBox()
                msg.setWindowTitle("CommStatX error")
                msg.setText(" Group 2 Minimum 4 characters required!")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()  # this will show our messagebox
                selgrp = group1
                return
            selgrp = group2
            print(selgrp)

        if len(callsign) < 4:
            msg = QMessageBox()
            msg.setWindowTitle("CommStatX error")
            msg.setText("Minimum 4 characters required!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            x = msg.exec_()  # this will show our messagebox
            return
        if len(group1) < 4:
            msg = QMessageBox()
            msg.setWindowTitle("CommStatX error")
            msg.setText("Minimum 4 characters required for Group 1!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            x = msg.exec_()  # this will show our messagebox
            return
        if len(group2) > 0 and len(group2) < 4:
            msg = QMessageBox()
            msg.setWindowTitle("CommStatX error")
            msg.setText("Minimum 4 characters required for Group 2!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            x = msg.exec_()  # this will show our messagebox
            return
        if len(grid) < 4:
            msg = QMessageBox()
            msg.setWindowTitle("CommStatX error")
            msg.setText("4 characters required for Grid!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            x = msg.exec_()  # this will show our messagebox
            return
        if len(path) < 8:
            msg = QMessageBox()
            msg.setWindowTitle("CommStatX error")
            msg.setText("Path must be populated with JS8Call DIRECTED.TXT Path!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            x = msg.exec_()  # this will show our messagebox
            return

        path_to_file = path + "/DIRECTED.TXT"
        if not os.path.exists(path_to_file):
            msg = QMessageBox()
            msg.setWindowTitle("CommStatX error")
            msg.setText("JS8Call DIRECTED.TXT not found!")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            x = msg.exec_()  # this will show our messagebox
            return

        # Get the configparser object
        config_object = ConfigParser()

        # Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
        config_object["USERINFO"] = {
            "callsign": callsign,
            "callsignsuffix": callsignSuffix,
            "group1": group1,
            "group2": group2,
            "grid": grid,
            "selectedgroup": selgrp
        }

        config_object["DIRECTEDCONFIG"] = {
            "path": path,
            "server": server,
            "port": port

        }

        # Write the above sections to config.ini file
        with open('config.ini', 'w') as conf:
            config_object.write(conf)
        self.on_close()

    def callval(self):
        le_callsign = self.lineEdit
        # !! ReGex implementation !!
        # For more details about ReGex search on google: regex rules or something similar
        reg_ex = QRegExp("[a-z-A-Z0-9_]+")  # @"[^A-Za-z0-9\s]+"
        le_callsign_validator = QRegExpValidator(reg_ex, le_callsign)
        le_callsign.setValidator(le_callsign_validator)
        # !! ReGex implementation End !!

    def suffval(self):
        le_callsign = self.lineEdit_2
        # !! ReGex implementation !!
        # For more details about ReGex search on google: regex rules or something similar
        reg_ex = QRegExp("[a-z-A-Z0-9_]+")  # @"[^A-Za-z0-9\s]+"
        le_callsign_validator = QRegExpValidator(reg_ex, le_callsign)
        le_callsign.setValidator(le_callsign_validator)
        # !! ReGex implementation End !!

    def grp1val(self):
        le_callsign = self.lineEdit_3
        # !! ReGex implementation !!
        # For more details about ReGex search on google: regex rules or something similar
        reg_ex = QRegExp("[a-z-A-Z0-9_]+")  # @"[^A-Za-z0-9\s]+"
        le_callsign_validator = QRegExpValidator(reg_ex, le_callsign)
        le_callsign.setValidator(le_callsign_validator)
        # !! ReGex implementation End !!

    def grp2val(self):
        le_callsign = self.lineEdit_4
        # !! ReGex implementation !!
        # For more details about ReGex search on google: regex rules or something similar
        reg_ex = QRegExp("[a-z-A-Z0-9_]+")  # @"[^A-Za-z0-9\s]+"
        le_callsign_validator = QRegExpValidator(reg_ex, le_callsign)
        le_callsign.setValidator(le_callsign_validator)
        # !! ReGex implementation End !

    def gridval(self):
        le_callsign = self.lineEdit_5
        # !! ReGex implementation !!
        # For more details about ReGex search on google: regex rules or something similar
        reg_ex = QRegExp("[a-z-A-Z0-9_]+")  # @"[^A-Za-z0-9\s]+"
        le_callsign_validator = QRegExpValidator(reg_ex, le_callsign)
        le_callsign.setValidator(le_callsign_validator)
        # !! ReGex implementation End !!



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormSettings = QtWidgets.QWidget()
    ui = Ui_FormSettings()
    ui.setupUi(FormSettings)
    FormSettings.show()
    sys.exit(app.exec_())
