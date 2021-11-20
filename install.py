#!/usr/bin/env python3
import subprocess
import sys
import os 



def runsettings():
	subprocess.call("./settings.py", shell=True)


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#firstmodule = "pyqt5"
#secondmodule = "PyQtWebEngine"
thirdmodule = "feedparser"
forthmodule = "file-read-backwards"
fifthmodule = "folium"
#install(firstmodule)
#install(secondmodule)
install(thirdmodule)
install(forthmodule)
install(fifthmodule)
#os.chdir(os.path.dirname(__file__))
#print(os.getcwd())

#runsettings()



