# inistial code cloned from https://gist.github.com/bradmontgomery/2219997#gistcomment-2057683 "ghost"

## this service is designed to route ifttt request to domoticz instead of exposing domoticz instance to the world.
## the idea is to put in IFTTT url with secret key like:  http://1.2.3.4/LightsOn&secret=abcdjkneidnn, then parse it and run url request to domoticz Locally.
# there's also an advantage - you can use IFTTT with ingredients like :   http://{url}/GoingToSleep and map it to a scene in domoticz. You can not do it directly to domoticz because of idx instead of scene name in url. 
#  Now you can have just 1 rule in IFTTT to manage your scenes and map them to IDX in this script.
# USAGE: CREATE file called secret.txt and put there your secret. Then modify the script to map URL postfix to IDX in domoticz.
# Use secret to launch scenes, for example:
# http://1.2.3.4:8456/GOTOSLEEP&secret=ThisIsMYPrettySecret123

#!/usr/bin/python3


import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import urllib.request
import config

hostName = ""

with open('/home/pi/git/python/secret.txt', 'r') as file:
	secret = file.read().replace('\n', '')

class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
		global secret
		idx = 0
		self.send_response(200)
		self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
		if self.path == '/LEDY'+'&secret='+secret:
			idx = 10
		if self.path == '/SPANIE'+'&secret='+secret:
                        idx = 6
		print('ustawiam IDX = '+str(idx))
		url = 'http://127.0.0.1:8080/json.htm?type=command&param=switchscene&idx='+str(idx)+'&switchcmd=On'


		#print(url)
		if idx > 0 :
			with urllib.request.urlopen(url) as response:
				print('Making request: '+url)
				html = response.read()	
	
		#import pdb; pdb.set_trace()


myServer = HTTPServer((hostName, config.hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, config.hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, config.hostPort))
