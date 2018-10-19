# *** List Users for Chat ***
# Code based on https://www.twilio.com/docs/chat/rest/users
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

# A list of chat users parameters & their permissable values

users = client.chat.services('ISxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').users.list()

#print list of all chat users properties to console, useful for learning info available you can work with?

for record in users:
    print(record.account_sid)
    print(record.attributes)
    print(record.date_created)
    print(record.date_updated)
    print(record.friendly_name)
    print(record.identity)
    print(record.is_notifiable)
    print(record.is_online)
    print(record.joined_channels_count)
    print(record.role_sid)
    print(record.service_sid)
    print(record.sid)
    print(record.url)

#create variable for this record
cdr = (record.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat users properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Attributes : " + str(record.attributes) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("Friendly Name : " + str(record.friendly_name) + "\n")
f.write("Identity : " + str(record.identity) + "\n")
f.write("Is Notifiable : " + str(record.is_notifiable) + "\n")
f.write("Is Online : " + str(record.is_online) + "\n")
f.write("Joined Channels Count : " + str(record.joined_channels_count) + "\n")
f.write("Role SID : " + str(record.role_sid) + "\n")
f.write("Service SID : " + str(record.service_sid) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("URL : " + str(record.url) + "\n")
f.close()
