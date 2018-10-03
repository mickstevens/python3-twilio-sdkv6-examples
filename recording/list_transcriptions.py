# *** List Transcriptions ***
# Code based on https://www.twilio.com/docs/voice/api/recording-transcription
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

# A list of recording transcription parameters & their permissable values, comment out (#) those lines not required
transcriptions = client.transcriptions.list()

#print list of all recording transcription properties to console, useful for learning info available you can work with?
for record in transcriptions:

    print(record.account_sid)
    print(record.date_created)
    print(record.date_updated)
    print(record.duration)
    print(record.price)
    print(record.price_unit)
    print(record.recording_sid)
    print(record.sid)
    print(record.status)
    print(record.transcription_text)
    print(record.uri)

#create variable for this record
cdr = (record.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/recordings/logs/" + str( cdr ) + ".log", "a")
#write list of all message properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("Duration : " + str(record.duration) + "\n")
f.write("Price : " + str(record.price) + "\n")
f.write("Price Unit : " + str(record.price_unit) + "\n")
f.write("Recording SID : " + str(record.recording_sid) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Status : " + str(record.status) + "\n")
f.write("Transcription Text : " + str(record.transcription_text) + "\n")
f.write("URI : " + str(record.uri) + "\n")
f.close()