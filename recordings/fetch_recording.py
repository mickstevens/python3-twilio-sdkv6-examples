# *** Fetch a Recording ***
# Code based on https://www.twilio.com/docs/voice/api/recording
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful, IMHO, for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/recordings/logs/twilio_recordings.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of recording parameters & their permissable values, comment out (#) those lines not required
recording = client.recordings('RExxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').fetch()

#print list of all recording properties to console, useful for learning info available you can work with?
print(recording.account_sid)
print(recording.api_version)
print(recording.call_sid)
print(recording.channels)
print(recording.conference_sid)
print(recording.date_created)
print(recording.date_updated)
print(recording.duration)
print(recording.encryption_details)
print(recording.error_code)
print(recording.price)
print(recording.price_unit)
print(recording.sid)
print(recording.source)
print(recording.start_time)
print(recording.status)
print(recording.uri)

#create variable for this record
cdr = (recording.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/recordings/logs/" + str( cdr ) + ".log", "a")
#write list of all message properties to above file...
f.write("Account SID : " + str(recording.account_sid) + "\n")
f.write("API Version : " + str(recording.api_version) + "\n")
f.write("Call SID : " + str(recording.call_sid) + "\n")
f.write("Channels : " + str(recording.channels) + "\n")
f.write("Conference SID : " + str(recording.conference_sid) + "\n")
f.write("Date Created : " + str(recording.date_created) + "\n")
f.write("Date Updated : " + str(recording.date_updated) + "\n")
f.write("Duration : " + str(recording.duration) + "\n")
f.write("Encryption Details : " + str(recording.encryption_details) + "\n")
f.write("Error Code : " + str(recording.error_code) + "\n")
f.write("Price : " + str(recording.price) + "\n")
f.write("Price Unit : " + str(recording.price_unit) + "\n")
f.write("SID : " + str(recording.sid) + "\n")
f.write("Source : " + str(recording.source) + "\n")
f.write("Start Time : " + str(recording.start_time) + "\n")
f.write("Status : " + str(recording.status) + "\n")
f.write("URI : " + str(recording.uri) + "\n")
f.close()