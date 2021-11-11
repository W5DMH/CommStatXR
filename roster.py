import os
import sqlite3
from configparser import ConfigParser
import re
from time import strftime
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDateTime, Qt, QDate
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import datetime
import js8callAPIsupport
import folium
import sqlite3
import io


serverip = ""
serverport = ""
callsign = ""
grid = ""
selectedgroup = ""
acklist = ""

class Ui_FormRoster(object):
    def setupUi(self, FormRoster):
        self.MainWindow = FormRoster
        FormRoster.setObjectName("FormRoster")
        FormRoster.resize(700, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        FormRoster.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("USA-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormRoster.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(FormRoster)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(FormRoster)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(FormRoster)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 5, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(FormRoster)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(FormRoster)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(FormRoster)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(FormRoster)
        self.tableWidget.setObjectName("tableWidget")
        #self.tableWidget.setColumnCount(0)
        #self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 4, 2)
        self.pushButton_2 = QtWidgets.QPushButton(FormRoster)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 4, 1, 1, 1)

        self.tableWidget.clicked.connect(self.on_Click)

        self.gridLayout_2.setRowStretch(0, 0);
        self.gridLayout_2.setRowStretch(1, 1);
        self.gridLayout_2.setRowStretch(2, 1);
        self.gridLayout_2.setRowStretch(3, 1);
        self.gridLayout_2.setRowStretch(4, 1);
        self.gridLayout_2.setRowStretch(5, 2);
        self.getConfig()
        self.mapperWidget()
        self.loadcheckins()

        self.serveripad = serverip
        self.servport = int(serverport)
        self.api = js8callAPIsupport.js8CallUDPAPICalls((self.serveripad),
                                                        int(self.servport))
        self.pushButton_2.clicked.connect(self.MainWindow.close)
        self.pushButton.clicked.connect(self.transmit)


        self.retranslateUi(FormRoster)
        QtCore.QMetaObject.connectSlotsByName(FormRoster)

    def retranslateUi(self, FormRoster):
        _translate = QtCore.QCoreApplication.translate
        FormRoster.setWindowTitle(_translate("FormRoster", "CommStatX NET Roster"))
        self.pushButton.setText(_translate("FormRoster", "Transmit"))
        self.label_2.setText(_translate("FormRoster", "Callsigns Selected for Check in ACK"))
        self.label.setText(_translate("FormRoster", "Current Active Group : "+selectedgroup))
        self.pushButton_2.setText(_translate("FormRoster", "Cancel"))

    def getConfig(self):
        global serverip
        global serverport
        global grid
        global callsign
        global selectedgroup
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





    def mapperWidget(self):
        mapper = QWebEngineView()
        coordinate = (38.8199286, -90.4782551)
        m = folium.Map(
            tiles='Stamen Terrain',
            zoom_start=4,
            location=coordinate

        )

        try:
            sqliteConnection = sqlite3.connect('traffic.db3')
            cursor = sqliteConnection.cursor()
            today = QDate.currentDate()
            todaystring2 = (today.toString(Qt.ISODate))
            yesterday = today.addDays(-1).toString(Qt.ISODate)

            query = "SELECT gridlat, gridlong, callsign, date  FROM checkins_Data where groupname = ? and date like ? or date LIKE ?"
            cursor.execute(query, (selectedgroup, '%' + todaystring2 + '%', '%' + yesterday + '%'))


            #sqlite_select_query = 'SELECT gridlat, gridlong, callsign, date FROM checkins_Data where groupname=?'
            #cursor.execute(sqlite_select_query, (selectedgroup,))
            items = cursor.fetchall()

            for item in items:
                glat = item[0]
                glon = item[1]
                call = item[2]
                utc = item[3]

                pinstring = (" Last Heard :")
                html = '''<HTML> <BODY><p style="color:blue;font-size:14px;">%s<br>
                %s<br>
                %s
                </p></BODY></HTML>''' % (call, pinstring, utc)
                iframe = folium.IFrame(html,
                                       width=160,
                                       height=70)

                popup = folium.Popup(iframe,
                                     min_width=100, max_width=160)
                #folium.Marker(location=[glat, glon], popup=popup).add_to(m)
                folium.CircleMarker(radius=6,fill=True, fill_color="darkblue",
                 location=[glat, glon], popup=popup, icon=folium.Icon(color="red")).add_to(m)


            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
         #       print("The SQLite connection is closed")
        # return map

        # folium.Marker(location=[38.655800, -87.274721],popup='<h3 style="color:green;">Marker2</h3>').add_to(m)
        # save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        #self.gridLayout.addWidget()widget = QWebEngineView()
        mapper.setHtml(data.getvalue().decode())
        self.gridLayout_2.addWidget(mapper, 5, 0, 1, 2)
        #print("Mapping completed")
        self.loadcheckins()
        QtCore.QTimer.singleShot(30000, self.mapperWidget)

    def loadcheckins(self):

        today = QDate.currentDate()
        #today2utc = today.toUTC()
        todaystring = QDateTime.currentDateTime().toString(Qt.ISODate)
        todaystring2 = (today.toString(Qt.ISODate))

        yesterday = today.addDays(-1).toString(Qt.ISODate)
        #print(todaystring)
        print(yesterday)
        print(todaystring2)
        #_from = self.fromDateTE.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        #_to = self.toDateTE.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        #sql = "SELECT * from test WHERE dt BETWEEN datetime('{}') AND datetime('{}')".format(_from, _to)
        #print(f'Subtracting 22 days: ')

        #date1 = QDateTime.currentDateTime()
        #displayTxt = (now.toUTC().toString(Qt.ISODate))

        #self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        connection = sqlite3.connect('traffic.db3')
        query = "SELECT date, callsign, traffic FROM checkins_Data where groupname = ? and date like ? or date LIKE ?"

        result = connection.execute(query, (selectedgroup, '%'+todaystring2+'%', '%'+yesterday+'%'))
        #('%' + searchstr + '%', type))


        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        table = self.tableWidget
        table.setHorizontalHeaderLabels(
            str("Date Time UTC ;Callsign; traffic").split(
                ";"))
        header = table.horizontalHeader()
        #header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget = QtWidgets.QTableWidget()
        # self.addWidget(QTableWidget(table),0, 0, 1, 2)
        # self.tableWidget = QtWidgets.QTableWidget()
        #self.tableWidget.resizeColumnsToContents()
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.sortItems(0, QtCore.Qt.DescendingOrder)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        #print("Load Bulletins & Marquee Completed")
        #QtCore.QTimer.singleShot(30000, self.loadbulletins)




    def on_Click(self):
        global acklist
        # #selected cell value.
        index=(self.tableWidget.selectionModel().currentIndex())
        # print(index)
        #value=index.sibling(index.row(),index.column()).data()
        value2 = index.sibling(index.row(),1).data()
        acklist = acklist+ " * "+value2
        self.lineEdit.setText("Check ins from : "+acklist)

    def transmit(self):
        global selectedgroup
        global callsign

        comments1 = "Checked in  "+ acklist
        comments = re.sub("[^A-Za-z0-9*\-\s]+", " ", comments1)

        if len(comments) < 5 :
            msg = QMessageBox()
            msg.setWindowTitle("CommStatX error")
            msg.setText( "Text too short")
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            x = msg.exec_()  # this will show our messagebox

            return
        group = "@"+selectedgroup
        message = "" + group + " MSG ," + comments + ""
        #message = ""+group + " ," + comments + ""
        messageType = js8callAPIsupport.TYPE_TX_SEND
        messageString = message

        #res = QMessageBox.question(FormCheckin, "Question", "Are you sure?", QMessageBox.Yes | QMessageBox.No)
        msg = QMessageBox()
        msg.setWindowTitle("CommStatX TX")
        msg.setText("CommStatX will transmit : " + message)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        x = msg.exec_()



        self.sendMessage(messageType, messageString)

        self.closeapp()

    def closeapp(self):
        self.MainWindow.close()

    def sendMessage(self, messageType, messageText):
        self.api.sendMessage(messageType, messageText)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormRoster = QtWidgets.QWidget()
    ui = Ui_FormRoster()
    ui.setupUi(FormRoster)
    FormRoster.show()
    sys.exit(app.exec_())
