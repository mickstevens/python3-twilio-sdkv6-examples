# *** Create Invite for Chat ***
# Code based on https://www.twilio.com/docs/chat/rest/invites
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

# A list of chat invite parameters & their permissable values

invite = client.chat.services('ISxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                    .channels('CHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                    .invites \
                    .create(identity='name@domain.com', role_sid='RLxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#print list of all chat invite properties to console, useful for learning info available you can work with?

print(invite.account_sid)
print(invite.channel_sid)
print(invite.date_created)
print(invite.date_updated)
print(invite.identity)
print(invite.role_sid)
print(invite.service_sid)
print(invite.sid)
print(invite.url)

#create variable for this record
cdr = (invite.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat invite properties to above file...
f.write("Account SID : " + str(invite.account_sid) + "\n")
f.write("Channel SID : " + str(invite.channel_sid) + "\n")
f.write("Date Created : " + str(invite.date_created) + "\n")
f.write("Date Updated : " + str(invite.date_updated) + "\n")
f.write("Identity : " + str(invite.identity) + "\n")
f.write("Role SID : " + str(invite.role_sid) + "\n")
f.write("Service SID : " + str(invite.service_sid) + "\n")
f.write("SID : " + str(invite.sid) + "\n")
f.write("URL : " + str(invite.url) + "\n")
f.close()
