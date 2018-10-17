# *** Fetch an API Key ***
# Code based on www.twilio.com/docs/iam/keys/api
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
#from datetime import datetime | not required for this examples
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python/python3-twilio-sdkv6-examples/keys/logs/twilio_keys.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of key parameters & their permissable values

key = client.keys('SKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').fetch()

#print list of all key properties to console, useful for learning info available you can work with?

print(key.date_created)
print(key.date_updated)
print(key.friendly_name)
print(key.sid)

#create variable for this record
cdr = (key.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/keys/logs/" + str( cdr ) + ".log", "a")
#write list of all key properties to above file...
f.write("Date Created : " + str(key.date_created) + "\n")
f.write("Date Updated : " + str(key.date_updated) + "\n")
f.write("Friendly Name : " + str(key.friendly_name) + "\n")
f.write("SID : " + str(key.sid) + "\n")
f.close()
