#!/usr/bin/env python
# Simply a replication of the Python SimpleHTTPServer but with added functionality to simply log requests
__author__ = "Munir Njiru"
__email__ = "munir@alien-within.com"
__status__ = "Production"

import SimpleHTTPServer as xxeDTDServer
import SocketServer
import sys
import base64

PORT = 8000

class xxeServerHandler(xxeDTDServer.SimpleHTTPRequestHandler):
    log_file = open('xxelog.txt', 'a')
    def log_message(self, format, *args):
        self.log_file.write("%s - - [%s] %s\n" %
                            (self.client_address[0],
                             self.log_date_time_string(),
                             base64.b64decode(format%args)))
	
try:
	Handler = xxeServerHandler
	httpd = SocketServer.TCPServer(("", PORT), Handler)
	print "Starting XXE Server on port: ", PORT
	print 'Press ^C to shut down the web server'
	httpd.serve_forever()
except:
	print '^C received, shutting down the web server'
	httpd.socket.close()