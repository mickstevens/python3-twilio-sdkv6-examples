# *** Delete a Transcription ***
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
transcription = client.transcriptions('TRxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').delete()

# print list of all recording transcription properties to console, useful for learning info available you can work with?
#print(transcription.account_sid)
#print(transcription.date_created)
#print(transcription.date_updated)
#print(transcription.duration)
#print(transcription.price)
#print(transcription.price_unit)
#print(transcription.recording_sid)
#print(transcription.sid)
#print(transcription.status)
#print(transcription.transcription_text)
#print(transcription.uri)

# create variable for this transcription
#cdr = (transcription.sid)
# open *.log file with cdr var as filename...
#f = open("/usr/local/twilio/python3/sdkv6x/recordings/logs/" + str( cdr ) + ".log", "a")
# write list of all message properties to above file...
#f.write("Account SID : " + str(transcription.account_sid) + "\n")
#f.write("Date Created : " + str(transcription.date_created) + "\n")
#f.write("Date Updated : " + str(transcription.date_updated) + "\n")
#f.write("Duration : " + str(transcription.duration) + "\n")
#f.write("Price : " + str(transcription.price) + "\n")
#f.write("Price Unit : " + str(transcription.price_unit) + "\n")
#f.write("Recording SID : " + str(transcription.recording_sid) + "\n")
#f.write("SID : " + str(transcription.sid) + "\n")
#f.write("Status : " + str(transcription.status) + "\n")
#f.write("Transcription Text : " + str(transcription.transcription_text) + "\n")
#f.write("URI : " + str(transcription.uri) + "\n")
#f.close()