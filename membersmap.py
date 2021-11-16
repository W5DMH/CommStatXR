from requests import get
import json
import folium
import os
import webbrowser
import html
import sqlite3
import io
from configparser import ConfigParser


serverip = ""
serverport = ""
callsign = ""
grid = ""
selectedgroup = ""




def getConfig():
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
            #print(labeltext)
            #self.label.setText("net tezt here")
            #self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
            #self.label.setText( labeltext)
            
getConfig()



def mapper():
    coordinate = (38.8199286, -90.4782551)
    m = folium.Map(zoom_start=4,location=coordinate)
    #map_ws = folium.Map(location=[0,0],zoom_start=2)

    try:
        sqliteConnection = sqlite3.connect('traffic.db3')
        cursor = sqliteConnection.cursor()

        #query = "SELECT datetime, idnum, callsign, message FROM bulletins_Data where groupid = ?"
        # result = connection.execute(query, (selectedgroup,))

        sqlite_select_query = 'SELECT gridlat, gridlong, callsign, date FROM members_Data where groupname1=? OR groupname2=?'
        cursor.execute(sqlite_select_query, (selectedgroup,selectedgroup,))
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
        #mapper.setHtml(data.getvalue().decode())



    CWD = os.getcwd()
    m.save('membersmap.html')
    webbrowser.open_new('file://'+CWD+'/'+'membersmap.html')
    
mapper()
