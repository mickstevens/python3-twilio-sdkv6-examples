# *** Update an Outgoing Caller ID's Friendly Name by Phone Number ***
# Code based on https://www.twilio.com/docs/voice/api/outgoing-caller-ids
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
#from datetime import datetime | not required for this examples
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/outgoing_caller_ids/logs/twilio_outgoing_caller_ids.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of outgoing_caller_id parameters & their permissable values

outgoing_caller_id = client \
    .outgoing_caller_ids('PNxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
    .update(friendly_name='My Updated CLI')

#print list of all outgoing_caller_id properties to console, useful for learning info available you can work with?
print(outgoing_caller_id.account_sid)
print(outgoing_caller_id.date_created)
print(outgoing_caller_id.date_updated)
print(outgoing_caller_id.friendly_name)
print(outgoing_caller_id.phone_number)
print(outgoing_caller_id.sid)
print(outgoing_caller_id.uri)

#create variable for this outgoing_caller_id
cdr = (outgoing_caller_id.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/outgoing_caller_ids/logs/" + str( cdr ) + ".log", "a")
#write list of all outgoing_caller_id properties to above file...
f.write("Account SID : " + str(outgoing_caller_id.account_sid) + "\n")
f.write("Date Created : " + str(outgoing_caller_id.date_created) + "\n")
f.write("Date Updated : " + str(outgoing_caller_id.date_updated) + "\n")
f.write("Friendly Name : " + str(outgoing_caller_id.friendly_name) + "\n")
f.write("Phone Number : " + str(outgoing_caller_id.phone_number) + "\n")
f.write("SID : " + str(outgoing_caller_id.sid) + "\n")
f.write("URI : " + str(outgoing_caller_id.uri) + "\n")
f.close()
