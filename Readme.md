# CommStatXR BETA 0.061 Released 11/20/21 @14:29Z
<h3 style="color: #4485b8;">CommStatXR BETA 0.061 add on software for JS8Call groups&nbsp;&nbsp;<img src="https://github.com/W5DMH/CommStatXR/blob/main/CommStatXBeta.png?raw=true" alt="CommStatXR 0.061" width="300" height="170" /></h3>

CommstatXR is a Python version of the CommStat software designed to run on Rasberry Pi Buster (Bullseye is not supported) operating systems. 
probably best to update python a bit before starting: <br>
<b>in a terminal type : python3 -m pip install --upgrade pip </b>
when the above command completes, make sure you are in the commstatx folder and then : <br>

Download the archive into home/pi, to unarchive the file: 
<b>type: tar -xvf commstatx.tar.gz </b><br>

and it will create the folder "commstatx", go into that folder and run install.py 
<b>type: python3 install.py </b><br>

After a successful install (this installs all of the necessary Python modules) 

<b>type: python3 commstatx.py</b>    

you should see a settings window that must be populated with a callsign, and a path to the 
JS8Call log directory (use JS8Call "LOG" menu item and "Open Log Directory" to get the path and
make sure there is in fact a DIRECTED.TXT file there ....the path should be something 
like /home/pi/.local/share/JS8Call    <b>do not enter the trailing slash or the file name.</b> 

After that is complete you should be able to run CommStatx by retyping:<br>
<b> type : python3 commstatx.py </b>
<br>
<BR>

 
<h3>Here is a link to the archive file:&nbsp;<a href="https://github.com/W5DMH/CommStatXR/raw/main/commstatx.tar.gz" target="_blank" rel="noopener">CommStatXR BETA 0.061 with Maps</a></h3>
<hr />

Get CommStat Support at: <br>
https://groups.io/g/CommStat
 <br>
 I must give credit to m0iax for his JS8CallAPISupport Script as that is what makes the transmitting possible.See the rest of his JS8Call Tools here : https://github.com/m0iax
<br>
