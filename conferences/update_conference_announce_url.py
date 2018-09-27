# *** Update a Conference announce_url ***
# Code based on https://www.twilio.com/docs/voice/api/conference
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/conferences/logs/twilio_conferences.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of conference parameters & their permissable values, comment out (#) those lines not required
conference = client.conferences('CF974a79bdd3a50a3d8677cd3b0d1c6bde') \
                  .update(announce_url='https://handler.twilio.com/twiml/EHee375cb86b94dc23803edd919f8a80f1'), #Optional, url may return MP3, WAV or TwiMl <Play> or <Say>

#print list of all conference properties to console, useful for learning info available you can work with
print(conference.account_sid)
print(conference.date_created)
print(conference.date_updated)
print(conference.friendly_name)
print(conference.region)
print(conference.sid)
print(conference.status)
print(conference.uri)

#create variable for this conference
cdr = (conference.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/conferences/logs/" + str( cdr ) + ".log", "a")
#write list of all conference properties to above file...
f.write("Account SID : " + str(conference.account_sid) + "\n")
f.write("Date Created : " + str(conference.date_created) + "\n")
f.write("Date Updated : " + str(conference.date_updated) + "\n")
f.write("Friendly Name : " + str(conference.friendly_name) + "\n")
f.write("Region : " + str(conference.region) + "\n")
f.write("SID : " + str(conference.sid) + "\n")
f.write("Status : " + str(conference.status) + "\n")
f.write("URI : " + str(conference.uri) + "\n")
f.close()