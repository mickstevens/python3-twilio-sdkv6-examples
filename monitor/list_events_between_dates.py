# *** List Events for account ***
# Code based on https://www.twilio.com/docs/usage/monitor-events
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from datetime import datetime # not required for this example
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

events = client.monitor.events.list(
                                   end_date=datetime(2018, 10, 25, 0, 0),
                                   start_date=datetime(2018, 9, 18, 0, 0)
                               )

#print list of all event properties to console, useful for learning info available you can work with?

for record in events:
    print(record.account_sid)
    print(record.actor_sid)
    print(record.actor_type)
    print(record.description)
    print(record.event_data)
    print(record.event_date)
    print(record.event_type)
    print(record.links)
    print(record.resource_sid)
    print(record.resource_type)
    print(record.sid)
    print(record.source)
    print(record.source_ip_address)
    print(record.url)

#create variable for this event
cdr = (record.sid)

f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/monitor/logs/" + str( cdr ) + ".log", "a")
#write list of all event properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Actor SID : " + str(record.actor_sid) + "\n")
f.write("Actor Type : " + str(record.actor_type) + "\n")
f.write("Description : " + str(record.description) + "\n")
f.write("Event Data : " + str(record.event_data) + "\n")
f.write("Event Date : " + str(record.event_date) + "\n")
f.write("Event Type : " + str(record.event_type) + "\n")
f.write("Links : " + str(record.links) + "\n")
f.write("Resoure SID : " + str(record.resource_sid) + "\n")
f.write("Resoure Type : " + str(record.resource_type) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Source : " + str(record.source) + "\n")
f.write("Source IP Address : " + str(record.source_ip_address) + "\n")
f.write("URL : " + str(record.url) + "\n")
f.close()