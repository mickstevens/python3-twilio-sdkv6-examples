# *** Create a Message using an API Key ***
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
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
api_secret = 'your_api_secret'
client = Client(api_key, api_secret, account_sid)

# A list of message parameters & their permissable values, comment out (#) those lines not required
message = client.messages.create(
                        application_sid='APxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', # Optional
                        body='this is a message body', # Required if MediaUrl is not passed 
                        from_='+15005550000', # Required if MessagingServiceSid is not passed
                        max_price='0.0001', #Optional
                        media_url='https://feywy.com/mbFQBRi4CG', # Required if Body is not passed
                        messaging_service_sid='MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', #Required if From is not passed
                        provide_feedback='true', #Optional, default = false
                        status_callback='http://demo.twilio.com/docs/voice.xml', # Optional, default = completed
                        to='+15005550001', # Required
                        validity_period='14400' # Optional, in seconds, valid values = between 1 - 14400 (default) 
                    )
#print list of all message properties to console, useful for learning info available you can work with?
print(message.account_sid)
print(message.api_version)
print(message.body)
print(message.date_created)
print(message.date_sent)
print(message.date_updated)
print(message.direction)
print(message.error_code)
print(message.error_message)
print(message.from_)
print(message.messaging_service_sid)
print(message.num_media)
print(message.num_segments)
print(message.price)
print(message.price_unit)
print(message.sid)
print(message.status)
print(message.subresource_uris)
print(message.to)
print(message.uri)

#create variable for this message
cdr = (message.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/messages/logs/" + str( cdr ) + ".log", "a")
#write list of all message properties to above file...
f.write("Account SID : " + str(message.account_sid) + "\n")
f.write("API Version : " + str(message.api_version) + "\n")
f.write("Body : " + str(message.body) + "\n")
f.write("Date Created : " + str(message.date_created) + "\n")
f.write("Date Sent : " + str(message.date_sent) + "\n")
f.write("Date Updated : " + str(message.date_updated) + "\n")
f.write("Direction : " + str(message.direction) + "\n")
f.write("Error Code : " + str(message.error_code) + "\n")
f.write("Error Message : " + str(message.error_message) + "\n")
f.write("From : " + str(message.from_) + "\n")
f.write("Messaging SID : " + str(message.messaging_service_sid) + "\n")
f.write("Number of Media Files : " + str(message.num_media) + "\n")
f.write("Number of Segments : " + str(message.num_segments) + "\n")
f.write("Price : " + str(message.price) + "\n")
f.write("Price Unit : " + str(message.price_unit) + "\n")
f.write("SID : " + str(message.sid) + "\n")
f.write("Status : " + str(message.status) + "\n")
f.write("Subresource URIs : " + str(message.subresource_uris) + "\n")
f.write("To : " + str(message.to) + "\n")
f.write("URI : " + str(message.uri) + "\n")
f.close()