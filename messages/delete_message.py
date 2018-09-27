# *** Delete a Message ***
# Code based on https://www.twilio.com/docs/sms/api/message
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful, IMHO, for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/messages/logs/twilio_messages.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of message parameters & their permissable values, comment out (#) those lines not required

client.messages('MMxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx').delete()

#for record in messages:
#print list of all message properties to console, useful for learning info available you can work with?
#    print(record.account_sid)
#    print(record.api_version)
#    print(record.body)
#    print(record.date_created)
#    print(record.date_sent)
#    print(record.date_updated)
#    print(record.direction)
#    print(record.error_code)
#    print(record.error_message)
#    print(record.from_)
#    print(record.messaging_service_sid)
#    print(record.num_media)
#    print(record.num_segments)
#    print(record.price)
#    print(record.price_unit)
#    print(record.sid)
#    print(record.status)
#    print(record.subresource_uris)
#    print(record.to)
#    print(record.uri)

# create variable for this message
#cdr = (message.sid)
# open *.log file with cdr var as filename...
#f = open("/usr/local/twilio/python3/sdkv6x/messages/logs/" + str( cdr ) + ".log", "a")
# write list of all message properties to above file...
#f.write("Account SID : " + str(message.account_sid) + "\n")
#f.write("API Version : " + str(message.api_version) + "\n")
#f.write("Body : " + str(message.body) + "\n")
#f.write("Date Created : " + str(message.date_created) + "\n")
#f.write("Date Sent : " + str(message.date_sent) + "\n")
#f.write("Date Updated : " + str(message.date_updated) + "\n")
#f.write("Direction : " + str(message.direction) + "\n")
#f.write("Error Code : " + str(message.error_code) + "\n")
#f.write("Error Message : " + str(message.error_message) + "\n")
#f.write("From : " + str(message.from_) + "\n")
#f.write("Messaging SID : " + str(message.messaging_service_sid) + "\n")
#f.write("Number of Media Files : " + str(message.num_media) + "\n")
#f.write("Number of Segments : " + str(message.num_segments) + "\n")
#f.write("Price : " + str(message.price) + "\n")
#f.write("Price Unit : " + str(message.price_unit) + "\n")
#f.write("SID : " + str(message.sid) + "\n")
#f.write("Status : " + str(message.status) + "\n")
#f.write("Subresource URIs : " + str(message.subresource_uris) + "\n")
#f.write("To : " + str(message.to) + "\n")
#f.write("URI : " + str(message.uri) + "\n")
#f.close()