# *** Create a Channel Type Role with editAnyUserInfo permission for Chat ***
# Code based on https://www.twilio.com/docs/chat/rest/roles
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

# A list of chat roles parameters & their permissable values

role = client.chat.services('ISxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                  .roles \
                  .create(
                       friendly_name='Channel - editAnyUserInfo',
                       type='channel',
                       permission='editAnyUserInfo'
                   )
                   
#print list of all chat roles properties to console, useful for learning info available you can work with?

print(role.account_sid)
print(role.date_created)
print(role.date_updated)
print(role.friendly_name)
print(role.permissions)
print(role.service_sid)
print(role.sid)
print(role.type)
print(role.url)

#create variable for this record
cdr = (role.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat roles properties to above file...
f.write("Account SID : " + str(role.account_sid) + "\n")
f.write("Date Created : " + str(role.date_created) + "\n")
f.write("Date Updated : " + str(role.date_updated) + "\n")
f.write("Friendly Name : " + str(role.friendly_name) + "\n")
f.write("Permissions : " + str(role.permissions) + "\n")
f.write("Service SID : " + str(role.service_sid) + "\n")
f.write("SID : " + str(role.sid) + "\n")
f.write("Type : " + str(role.type) + "\n")
f.write("URL : " + str(role.url) + "\n")
f.close()