# -*- coding: utf-8 -*-
import os
import psutil
from configparser import ConfigParser
# Form implementation generated from reading ui file 'datareset.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt

path = ""


class Ui_FormReset(object):
    def setupUi(self, FormReset):
        self.MainWindow = FormReset
        FormReset.setObjectName("FormReset")
        FormReset.resize(682, 273)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormReset.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("USA-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormReset.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(FormReset)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(FormReset)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(FormReset)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(FormReset)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        self.pushButton.clicked.connect(self.reset_all)
        self.pushButton_2.clicked.connect(self.MainWindow.close)

        self.getConfig()

        self.retranslateUi(FormReset)
        QtCore.QMetaObject.connectSlotsByName(FormReset)

    def retranslateUi(self, FormReset):
        _translate = QtCore.QCoreApplication.translate
        FormReset.setWindowTitle(_translate("FormReset", "CommStatX Data Reset"))
        self.pushButton.setText(_translate("FormReset", "Execute"))
        self.pushButton_2.setText(_translate("FormReset", "Cancel"))
        self.label.setText(_translate("FormReset", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Data reset, essetially this is the nuclear option to wipe out<br> all of your CommStatX tables and rebuild your database. <br>This will also delete your JS8Call DIRECTED.TXT file, but it <br>will make a backup copy for you called DIRECTEDBACKUP.TXT . </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All other data and tables will be removed and recreated as empty tables. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


    def getConfig(self):
        global serverip
        global serverport
        global grid
        global callsign
        global selectedgroup
        global path
        if os.path.exists("config.ini"):
            config_object = ConfigParser()
            config_object.read("config.ini")
            userinfo = config_object["USERINFO"]
            systeminfo = config_object["DIRECTEDCONFIG"]
            callsign = format(userinfo["callsign"])
            callsignSuffix = format(userinfo["callsignsuffix"])
            group1 = format(userinfo["group1"])
            group2 = format(userinfo["group2"])
            grid = format(userinfo["grid"])
            path = format(systeminfo["path"])
            serverip = format(systeminfo["server"])
            serverport = format(systeminfo["port"])
            selectedgroup = format(userinfo["selectedgroup"])
            labeltext = ("Currently Active Group : " + selectedgroup)
            print(labeltext)
            self.label.setText("net tezt here")
            #self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
            self.label.setText( labeltext)

    def reset_all(self):
        print("resetting all")
        conn = sqlite3.connect("traffic.db3")
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS StatRep_Data")
        cur.execute("DROP TABLE IF EXISTS  checkins_Data")
        cur.execute("DROP TABLE IF EXISTS  members_Data")
        cur.execute("DROP TABLE IF EXISTS  heard_Data")
        cur.execute("DROP TABLE IF EXISTS  bulletins_Data")
        cur.execute("DROP TABLE IF EXISTS  marquees_Data")

        cur.execute("CREATE TABLE IF NOT EXISTS bulletins_Data (Id integer primary key autoincrement, datetime TEXT, groupid TEXT, idnum TEXT UNIQUE, callsign TEXT, message TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS checkins_Data (id INTEGER PRIMARY KEY autoincrement, date TEXT, time TEXT, callsign TEXT UNIQUE, groupname TEXT, traffic TEXT, gridlat DOUBLE, gridlong Double)")
        cur.execute("CREATE TABLE IF NOT EXISTS StatRep_Data(id INTEGER PRIMARY KEY autoincrement, datetime TEXT, date TEXT, T1 TEXT, freq DOUBLE, callsign TEXT, groupname TEXT, grid TEXT, SRid TEXT NOT NULL UNIQUE, prec TEXT,status TEXT, commpwr TEXT, pubwtr TEXT, med TEXT, ota TEXT, trav TEXT, net TEXT, fuel TEXT, food TEXT, crime TEXT, civil TEXT, political TEXT, comments TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS heard_Data(id INTEGER PRIMARY KEY, date TEXT NOT NULL, callsign TEXT UNIQUE NOT NULL, gridlat DOUBLE NOT NULL, gridlong DOUBLE NOT NULL)")
        cur.execute("CREATE TABLE IF NOT EXISTS members_Data(id INTEGER PRIMARY KEY, date TEXT, callsign TEXT UNIQUE, groupname1 TEXT,groupname2 TEXT, gridlat DOUBLE, gridlong Double )")
        cur.execute("CREATE TABLE IF NOT EXISTS marquees_Data(id INTEGER PRIMARY KEY, idnum TEXT UNIQUE NOT NULL, callsign TEXT, groupname TEXT, date TEXT, color TEXT, message TEXT)")

        mtstr1 = "2021-11-02 19:04:12"
        mtstr2 = "0000"
        mtstr7 = "1"
        mtstr8 = "NO MESSAGE YET"
        grpname = "AMRRON"
        callsign = "W5DMH"
        #cur.execute("INSERT OR REPLACE INTO marquees_Data (date, idnum, groupname, color, message) VALUES ('" + mtstr1 + "','" + mtstr2 + "','" + mtstr7 + "','" + grpname + "','" + mtstr8 + "')")
        #cur.execute("INSERT OR REPLACE INTO marquees_Data (date, idnum, callsign, groupname, color, message) VALUES (mtstr1,mtstr2,mtstr7,grpname,mtstr8 + "')")

        cur.execute("INSERT OR REPLACE INTO marquees_Data (date, idnum, callsign, groupname, color, message) VALUES(?, ?, ?, ?, ?, ?  )",(mtstr1, mtstr2, callsign, grpname, mtstr7, mtstr8))
        conn.commit()

        timestr = time.strftime("%Y%m%d-%H%M%S")
        os.rename(path+"\DIRECTED.TXT", path+"\DIRECTEDBACKUP"+timestr+".TXT")
        f = open(path+"\DIRECTED.TXT", "a")
        #f.write("Now the file has more content!")
        f.close()
        self.killcommstatx()


    def killcommstatx(self):
        PROCNAME = "CommStatX.exe"
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormReset = QtWidgets.QWidget()
    ui = Ui_FormReset()
    ui.setupUi(FormReset)
    FormReset.show()
    sys.exit(app.exec_())
