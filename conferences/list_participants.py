# *** List Conference Participants ***
# Code based on https://www.twilio.com/docs/voice/api/conference-participant
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import date # | not required for this example 
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

# A list of conference participant parameters & their permissable values, comment out (#) those lines not required
participants = client.conferences('CFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                     .participants \
                     .list()

#print list of all conference participant properties to console, useful for learning info available you can work with?
for record in participants:
    print(record.account_sid)
    print(record.call_sid)
    print(record.conference_sid)
    print(record.date_created)
    print(record.date_updated)
    print(record.end_conference_on_exit)
    print(record.from_)
    print(record.hold)
    print(record.muted)
    print(record.start_conference_on_enter)
    print(record.status)
    print(record.to)
    print(record.uri)

#create variable for this participant
cdr = (record.conference_sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/conferences/logs/" + str( cdr ) + ".log", "a")
#write list of all participant properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Call SID : " + str(record.call_sid) + "\n")
f.write("Conference SID : " + str(record.conference_sid) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("End Conference on Exit : " + str(record.end_conference_on_exit) + "\n")
f.write("From : " + str(record.from_) + "\n")
f.write("Hold : " + str(record.hold) + "\n")
f.write("Mute : " + str(record.mute) + "\n")
f.write("Start Conference on Enter : " + str(record.start_conference_on_enter) + "\n")
f.write("Status : " + str(record.status) + "\n")
f.write("To : " + str(record.to) + "\n")
f.write("URI : " + str(record.uri) + "\n")
f.close()