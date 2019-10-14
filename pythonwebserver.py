# inistial code cloned from https://gist.github.com/bradmontgomery/2219997#gistcomment-2057683 "ghost"

## this service is designed to route ifttt request to domoticz instead of exposing domoticz instance to the world.
## the idea is to put in IFTTT url with secret key like:  http://1.2.3.4/LightsOn&secret=abcdjkneidnn, then parse it and run url request to domoticz Locally.
# there's also an advantage - you can use IFTTT with ingredients like :   http://{url}/GoingToSleep and map it to a scene in domoticz. You can not do it directly to domoticz because of idx instead of scene name in url. 
#  Now you can have just 1 rule in IFTTT to manage your scenes and map them to IDX in this script.

#!/usr/bin/python3


import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = ""
hostPort = 16123

class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
		self.send_response(200)
		self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))

	#	POST is for submitting data.
	def do_POST(self):

		print( "incomming http: ", self.path )

		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		self.send_response(200)

		client.close()

		#import pdb; pdb.set_trace()


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
