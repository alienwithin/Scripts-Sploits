#!/usr/bin/env python
__author__ = "Munir Njiru"
__email__ = "munir@alien-within.com"
__status__ = "Production"
#python giveWebHead.py -t https://example.com -w dirs.txt -i False -m GET
##########################################
#       Give Web Head v1.0
#         by Alienwithin
###########################################
#https://example.com/foundDir1
#https://example.com/foundDir2
#Results are written to a CSV file ie. found URLs and status code. 
#Bad Results are also written to file in the case above the files would be : 
#- example.com.csv => contains valid urls
#- example.com_ignored.csv => contains urls that failed the test and status code is the reason.
#HEAD is faster than GET ; if a server supports it then use that
##
import requests
import csv
from optparse import OptionParser
import tldextract
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
global gwHRequester
def gwhEngine(target, wordlist, method, redirects=False):
    error_codes_non_redir=[200,403]
    error_codes_redir= [200,301,302,403]
    with open(wordlist) as dirPerLine:
		for dir in dirPerLine:
			cleanDirName=str(dir.rstrip('\n'))
			fullURL=tldextract.extract(target)
			getHostname=fullURL.domain	
			resultFile=open(str(getHostname)+'.csv', 'a')
			badResults=open(str(getHostname)+'_ignored.csv', 'a')
			csvWritingObject = csv.writer(resultFile)
			BadResultObject=csv.writer(badResults)
			if method=="HEAD" and redirects=="False":
				gwhRequester=requests.head(target+cleanDirName,verify=False)
				gwhStatus=gwhRequester.status_code
				if gwhStatus in error_codes_non_redir:
					csvWritingObject.writerow( (target+cleanDirName, gwhStatus) )
					resultFile.close()
					print target+cleanDirName+" => "+ str(gwhStatus)		
			elif method=="HEAD" and redirects=="True":
				gwhRequester=requests.head(target+cleanDirName,verify=False)
				gwhStatus=gwhRequester.status_code
				if gwhStatus in error_codes_redir: 
					csvWritingObject.writerow( (target+cleanDirName, gwhStatus) )
					resultFile.close()
					print target+cleanDirName+" => "+ str(gwhStatus)	
			if method=="GET" and redirects=="True":
				gwhRequester=requests.get(target+cleanDirName,verify=False)
				gwhStatus=gwhRequester.status_code
				if gwhStatus in error_codes_non_redir: 
					csvWritingObject.writerow( (target+cleanDirName, gwhStatus) )
					resultFile.close()
					print target+cleanDirName+" => "+ str(gwhStatus)	
			elif method=="GET" and redirects=="False":
				gwhRequester=requests.get(target+cleanDirName,verify=False)
				gwhStatus=gwhRequester.status_code
				if gwhStatus in error_codes_redir: 
					csvWritingObject.writerow( (target+cleanDirName, gwhStatus) )
					resultFile.close()
					print target+cleanDirName+" => "+ str(gwhStatus)
			else:
				gwhRequester=requests.get(target+cleanDirName,verify=False)
				gwhStatus=gwhRequester.status_code
				print target+cleanDirName+" => "+ str(gwhStatus)
				BadResultObject.writerow( (target+cleanDirName, gwhStatus) )
				badResults.close()
def giveTheWebSomeHead():
    alienParser = OptionParser(usage="usage: %prog --help for [options]",
                          version="%prog version : 1.0")
    alienParser.add_option("-t", "--target",
                      action="store",
                      dest="target",
                      default="http://iWannaFindyourDirectories.ws",
                      help="Target URL")
    alienParser.add_option("-w", "--wordlist",
                      action="store", 
                      dest="wordlist",
                      default="dirlist.txt",
                      help="Path to wordlist with directory names")
    alienParser.add_option("-i", "--ignore-redirects",
				  action="store", 
				  dest="redirects",
				  default=False,
				  help="Path to wordlist with directory names")
    alienParser.add_option("-m", "--method",
				  action="store", 
				  dest="method",
				  default="HEAD",
				  help="Method to use to get results i.e. HEAD or GET")				  
    (options, args) = alienParser.parse_args()
	

    if options.target =="http://iWannaFindyourDirectories.ws" or options.target=="":
        alienParser.error("I'm sorry there simply has to be a target for this to work")
    elif options.wordlist=="":
		alienParser.error("You haven't selected a wordlist")
    else:
		myTarget=options.target
		if myTarget[len(myTarget)-1] != "/":
			myTarget = myTarget + "/"
		gwhEngine(myTarget, options.wordlist, options.method, options.redirects)
def banner():
      print "##########################################"
      print "\tGive Web Head v1.0\n\t by Alienwithin\n"
      print "##########################################"
if __name__ == '__main__':
	banner()
	giveTheWebSomeHead()
