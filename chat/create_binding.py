# *** Create Bindings for Chat ***
# Code based on https://www.twilio.com/docs/chat/rest/bindings-resource
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
#from datetime import datetime | not required for this examples
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/twilio_chat.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of chat binding parameters & their permissable values

binding = client.notify.services('ISxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                       .bindings \
                       .create(
                            address='+441234567890', # Required, 
                            binding_type='sms',
#                           credential_sid='', # Not required for binding_type 'sms'
#                           endpoint='endpoint_id', # Deprecated
                            identity='00000001'
 #                          notification_protocol_version='' # Not required for binding_type 'sms'
 #                          tag='new user' # Optional
                        )

#print list of all chat binding properties to console, useful for learning info available you can work with?
print(record.account_sid)
print(record.binding_type)
print(record.date_created)
print(record.date_updated)
print(record.endpoint)
print(record.identify)
print(record.links)
print(record.message_types)
print(record.service_sid)
print(record.sid)
print(record.url)

#create variable for this record
cdr = (record.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat binding properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Binding Type : " + str(record.binding_type) + "\n")
f.write("Credential SID : " + str(record.credential_sid) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("Endpoint : " + str(record.endpoint) + "\n")
f.write("Identity : " + str(record.identity) + "\n")
f.write("Links : " + str(record.links) + "\n")
f.write("Message Types : " + str(record.message_types) + "\n")
f.write("Service SID : " + str(record.service_sid) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("URL : " + str(record.url) + "\n")
f.close()
