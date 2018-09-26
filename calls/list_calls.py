# *** List Calls for Account ***
# Code based on https://www.twilio.com/docs/voice/api/call
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/calls/logs/twilio_calls.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of call parameters & their permissable values, comment out (#) those lines not required

calls = client.calls.list()

for record in calls:
    print(record.sid)

#print list of all call properties to console, useful for learning info available you can work with?
print(record.account_sid)
print(record.annotation)
print(record.answered_by)
print(record.api_version)
print(record.caller_name)
print(record.date_created)
print(record.date_updated)
print(record.direction)
print(record.duration)
print(record.end_time)
print(record.forwarded_from)
print(record.from_)
print(record.from_formatted)
print(record.group_sid)
print(record.parent_call_sid)
print(record.phone_number_sid)
print(record.price)
print(record.price_unit)
print(record.sid)
print(record.start_time)
print(record.status)
print(record.subresource_uris)
print(record.to)
print(record.to_formatted)
print(record.uri)

#create variable for this call
cdr = (record.sid)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/calls/logs/" + str( cdr ) + ".log", "a")
#write list of all call properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Annotation : " + str(record.annotation) + "\n")
f.write("Answered By : " + str(record.answered_by) + "\n")
f.write("API Version : " + str(record.api_version) + "\n")
f.write("Caller Name : " + str(record.caller_name) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("Direction : " + str(record.direction) + "\n")
f.write("Duration : " + str(record.duration) + "\n")
f.write("End Time : " + str(record.end_time) + "\n")
f.write("Forwarded From : " + str(record.forwarded_from) + "\n")
f.write("From : " + str(record.from_) + "\n")
f.write("From Formatted : " + str(record.from_formatted + "\n"))
f.write("Group SID : " + str(record.group_sid) + "\n")
f.write("Parent Call SID : " + str(record.parent_call_sid) + "\n")
f.write("Phone Number SID : " + str(record.phone_number_sid) + "\n")
f.write("Price : " + str(record.price) + "\n")
f.write("Price Unit : " + str(record.price_unit) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Start Time : " + str(record.start_time) + "\n")
f.write("Status : " + str(record.status) + "\n")
f.write("Subresource URIs : " + str(record.subresource_uris) + "\n")
f.write("To : " + str(record.to) + "\n")
f.write("To Formatted : " + str(record.to_formatted) + "\n")
f.write("URI : " + str(record.uri) + "\n")
f.close()