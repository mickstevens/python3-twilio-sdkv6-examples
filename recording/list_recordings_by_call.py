# *** List Recordings by Call ***
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
                    filename='/usr/local/twilio/python3/sdkv6x/recording/logs/twilio_recordings.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of recording parameters & their permissable values, comment out (#) those lines not required
recordings = client.recordings.list(call_sid='CAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

for record in recordings:

#print list of all recording properties to console, useful for learning info available you can work with?
    print(record.account_sid)
    print(record.api_version)
    print(record.call_sid)
    print(record.channels)
    print(record.conference_sid)
    print(record.date_created)
    print(record.date_updated)
    print(record.duration)
    print(record.encryption_details)
    print(record.error_code)
    print(record.price)
    print(record.price_unit)
    print(record.sid)
    print(record.source)
    print(record.start_time)
    print(record.status)
    print(record.uri)

#create variable for this record
cdr = (record.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/recording/logs/" + str( cdr ) + ".log", "a")
#write list of all message properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("API Version : " + str(record.api_version) + "\n")
f.write("Call SID : " + str(record.call_sid) + "\n")
f.write("Channels : " + str(record.channels) + "\n")
f.write("Conference SID : " + str(record.conference_sid) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("Duration : " + str(record.duration) + "\n")
f.write("Encryption Details : " + str(record.encryption_details) + "\n")
f.write("Error Code : " + str(record.error_code) + "\n")
f.write("Price : " + str(record.price) + "\n")
f.write("Price Unit : " + str(record.price_unit) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Source : " + str(record.source) + "\n")
f.write("Start Time : " + str(record.start_time) + "\n")
f.write("Status : " + str(record.status) + "\n")
f.write("URI : " + str(record.uri) + "\n")
f.close()