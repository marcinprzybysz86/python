# pythonwebserver.py

Initial code cloned from https://gist.github.com/bradmontgomery/2219997#gistcomment-2057683 "ghost"

this service is designed to route ifttt request to domoticz instead of exposing domoticz instance to the world.
the idea is to put in IFTTT url with secret key like:  http://1.2.3.4/LightsOn&secret=abcdjkneidnn, then parse it and run url request to domoticz Locally.
there's also an advantage - you can use IFTTT with ingredients like :   http://{url}/GoingToSleep and map it to a scene in domoticz. You can not do it directly to domoticz because of idx instead of scene name in url.

 Now you can have just 1 rule in IFTTT to manage your scenes and map them to IDX in this script.
USAGE: CREATE file called secret.txt and put there your secret. Then modify the script to map URL postfix to IDX in domoticz.
Use secret to launch scenes, for example:
http://1.2.3.4:8456/GOTOSLEEP&secret=ThisIsMYPrettySecret123

you need to create config.py file with content: hostPort = <portnumber>  example: hostPort = 9002


