# *** Fetch an Event for Account ***
# Code based on https://www.twilio.com/docs/usage/monitor-events
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python/python3-twilio-sdkv6-examples/monitor/logs/twilio_monitor.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of event parameters & their permissable values, comment out (#) those lines not required

event = client.monitor.events('AExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').fetch()

#print list of all event properties to console, useful for learning info available you can work with?

print(event.account_sid)
print(event.actor_sid)
print(event.actor_type)
print(event.description)
print(event.event_data)
print(event.event_date)
print(event.event_type)
print(event.links)
print(event.resource_sid)
print(event.resource_type)
print(event.sid)
print(event.source)
print(event.source_ip_address)
print(event.url)

#create variable for this event
cdr = (event.sid)
#open *.log file with cdr var as filename...

f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/monitor/logs/" + str( cdr ) + ".log", "a")
#write list of all event properties to above file...
f.write("Account SID : " + str(event.account_sid) + "\n")
f.write("Actor SID : " + str(event.actor_sid) + "\n")
f.write("Actor Type : " + str(event.actor_type) + "\n")
f.write("Description : " + str(event.description) + "\n")
f.write("Event Data : " + str(event.event_data) + "\n")
f.write("Event Date : " + str(event.event_date) + "\n")
f.write("Event Type : " + str(event.event_type) + "\n")
f.write("Links : " + str(event.links) + "\n")
f.write("Resoure SID : " + str(event.resource_sid) + "\n")
f.write("Resoure Type : " + str(event.resource_type) + "\n")
f.write("SID : " + str(event.sid) + "\n")
f.write("Source : " + str(event.source) + "\n")
f.write("Source IP Address : " + str(event.source_ip_address) + "\n")
f.write("URL : " + str(event.url) + "\n")
f.close()