# *** Delete a Conference Participant ***
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
participant = client.conferences('CFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                    .participants('CAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                    .delete()

#print list of all conference participant properties to console, useful for learning info available you can work with?
print(participant.account_sid)
print(participant.call_sid)
print(participant.conference_sid)
print(participant.date_created)
print(participant.date_updated)
print(participant.end_conference_on_exit)
print(participant.from_)
print(participant.hold)
print(participant.muted)
print(participant.start_conference_on_enter)
print(participant.status)
print(participant.to)
print(participant.uri)

#create variable for this participant
cdr = (participant.call_sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/conferences/logs/" + str( cdr ) + ".log", "a")
#write list of all participant properties to above file...
f.write("Account SID : " + str(participant.account_sid) + "\n")
f.write("Call SID : " + str(participant.call_sid) + "\n")
f.write("Conference SID : " + str(participant.conference_sid) + "\n")
f.write("Date Created : " + str(participant.date_created) + "\n")
f.write("Date Updated : " + str(participant.date_updated) + "\n")
f.write("End Conference on Exit : " + str(participant.end_conference_on_exit) + "\n")
f.write("From : " + str(participant.from_) + "\n")
f.write("Hold : " + str(participant.hold) + "\n")
f.write("Mute : " + str(participant.mute) + "\n")
f.write("Start Conference on Enter : " + str(participant.start_conference_on_enter) + "\n")
f.write("Status : " + str(participant.status) + "\n")
f.write("To : " + str(participant.to) + "\n")
f.write("URI : " + str(participant.uri) + "\n")
f.close()