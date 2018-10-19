# *** Create a  Channel for a Chat ***
# Code based on https://www.twilio.com/docs/chat/rest/credentials
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from datetime import datetime
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

# A list of chat channel parameters & their permissable values

channel = client.chat.services('ISxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                     .channels \
                     .create(
                         attributes="",
                         created_by="stevensm",
                         date_created=datetime(2018, 10, 19, 13, 40),
                         date_updated=datetime(2018, 10, 19, 13, 40),
                         friendly_name='My_Private_Channel',
                         type="private",
                         unique_name="Channel_Private_My"
                         )



#print list of all chat channel properties to console, useful for learning info available you can work with?

print(channel.account_sid)
print(channel.attributes)
print(channel.created_by)
print(channel.date_created)
print(channel.date_updated)
print(channel.friendly_name)
print(channel.links)
print(channel.members_count)
print(channel.messages_count)
print(channel.service_sid)
print(channel.sid)
print(channel.type)
print(channel.unique_name)
print(channel.url)

#create variable for this channel
cdr = (channel.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat channels properties to above file...
f.write("Account SID : " + str(channel.account_sid) + "\n")
f.write("Attributes : " + str(channel.attributes) + "\n")
f.write("Created By : " + str(channel.created_by) + "\n")
f.write("Date Created : " + str(channel.date_created) + "\n")
f.write("Date Updated : " + str(channel.date_updated) + "\n")
f.write("Friendly Name : " + str(channel.friendly_name) + "\n")
f.write("Links : " + str(channel.links) + "\n")
f.write("Members Count : " + str(channel.members_count) + "\n")
f.write("Messages Count : " + str(channel.messages_count) + "\n")
f.write("Service SID : " + str(channel.service_sid) + "\n")
f.write("SID : " + str(channel.sid) + "\n")
f.write("Type : " + str(channel.type) + "\n")
f.write("Unique Name : " + str(channel.unique_name) + "\n")
f.write("URL : " + str(channel.url) + "\n")
f.close()
