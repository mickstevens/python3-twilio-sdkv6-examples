# *** Create a new Outgoing Caller ID ***
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

validation_request = client.validation_requests \
                           .create(
                                call_delay='60', # Optional, 0 - 60 (default)
                                extension='', # Optional, digits to dial after connecting the verification call
                                friendly_name='My Home Phone Number',
                                phone_number='+441234567890',
                                status_callback='https://handler.twilio.com/twiml/EHebde64ac2eb6a48fef634b3b352e82fb',
                                status_callback_method='POST' # Optional, GET or POST (default)
                                )

#print list of all outgoing_caller_id properties to console, useful for learning info available you can work with?
print(validation_request.account_sid)
print(validation_request.call_sid)
print(validation_request.friendly_name)
print(validation_request.phone_number)
print(validation_request.validation_code)

#create variable for this outgoing_caller_id
cdr = (validation_request.validation_code)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/outgoing_caller_ids/logs/" + str( cdr ) + ".log", "a")
#write list of all outgoing_caller_id properties to above file...
f.write("Account SID : " + str(validation_request.account_sid) + "\n")
f.write("Call SID : " + str(validation_request.call_sid) + "\n")
f.write("Friendly Name : " + str(validation_request.friendly_name) + "\n")
f.write("Phone Number : " + str(validation_request.phone_number) + "\n")
f.write("Validation Code : " + str(validation_request.validation_code) + "\n")
f.close()
