# *** Delete a Chat User by SID ***
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

client.chat.services('ISxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
           .users('USxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
           .delete()


# print list of all chat users properties to console, useful for learning info available you can work with?

#print(user.account_sid)
#print(user.attributes)
#print(user.date_created)
#print(user.date_updated)
#print(user.friendly_name)
#print(user.identity)
#print(user.is_notifiable)
#print(user.is_online)
#print(user.joined_channels_count)
#print(user.role_sid)
#print(user.service_sid)
#print(user.sid)
#print(user.url)

# create variable for this record
#cdr = (user.sid)
# open *.log file with cdr var as filename...
#f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
# write list of all chat users properties to above file...
#f.write("Account SID : " + str(user.account_sid) + "\n")
#f.write("Attributes : " + str(user.attributes) + "\n")
#f.write("Date Created : " + str(user.date_created) + "\n")
#f.write("Date Updated : " + str(user.date_updated) + "\n")
#f.write("Friendly Name : " + str(user.friendly_name) + "\n")
#f.write("Identity : " + str(user.identity) + "\n")
#f.write("Is Notifiable : " + str(user.is_notifiable) + "\n")
#f.write("Is Online : " + str(user.is_online) + "\n")
#f.write("Joined Channels Count : " + str(user.joined_channels_count) + "\n")
#f.write("Role SID : " + str(user.role_sid) + "\n")
#f.write("Service SID : " + str(user.service_sid) + "\n")
#f.write("SID : " + str(user.sid) + "\n")
#f.write("URL : " + str(user.url) + "\n")
#f.close()
