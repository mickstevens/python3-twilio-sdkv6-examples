# *** Create a Call & specify a Status Callback URL ***
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
call = client.calls.create(
#                        application_sid='APxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', # Required, if Url is not passed
#                        caller_id='+15005550000', # Optional, E.164 format or ClientID or SIP address
#                        fallback_method="GET", # Optional, default = POST 
#                        fallback_url='http://demo.twilio.com/docs/voice.xml', # Optional, ignored if application_sid is present
                         from_='+15005550000', # Required, Twilio no or verified outgoing CLI
#                        machine_detection='enable', # Optional, or DetectMessageEnd, ignored if SendDigits & MachineDetection are present
#                        machine_detection_timeout='20', # Optional, default 30 (seconds)
                         method='GET', # Optional, default = POST, ignored if application_sid is present
#                        record='true',# Optional, default = false
#                        recording_channels='dual', # Optional, default = mono
#                        recording_status_callback='https://handler.twilio.com/twiml/EHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', # Optional
#                        recording_status_callback_event='completed in-progress failed', # Optional, also available seperately, default = completed & failed
#                        recording_status_callback_method='GET', # Optional, default = POST
#                        send_digits='#', # Optional, valid characters = 0-9, #, * & w (pause)
                         status_callback='https://www.myapp.com/events', # Optional, default = completed
#                        status_callback_event=['initiated', 'answered'], # Optional or initiated, ringing, answered & completed default = completed, ignored if application_sid is present
                         status_callback_method='POST', #Optional, default = POST
#                        timeout='15', #Optional,  seconds, default 60, max 600
                         to='+15005550001', # Required
#                        trim='do-not-trim', #Optional, default = trim-silence
                         url='http://demo.twilio.com/docs/voice.xml' # Required if ApplicationSid is not passed
                    )

#print list of all call properties to console, useful for learning info available you can work with?
print(call.account_sid)
print(call.annotation)
print(call.answered_by)
print(call.api_version)
print(call.caller_name)
print(call.date_created)
print(call.date_updated)
print(call.direction)
print(call.duration)
print(call.end_time)
print(call.forwarded_from)
print(call.from_)
print(call.from_formatted)
print(call.group_sid)
print(call.parent_call_sid)
print(call.phone_number_sid)
print(call.price)
print(call.price_unit)
print(call.sid)
print(call.start_time)
print(call.status)
print(call.subresource_uris)
print(call.to)
print(call.to_formatted)
print(call.uri)

#create variable for this call
cdr = (call.sid)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/calls/logs/" + str( cdr ) + ".log", "a")
#write list of all call properties to above file...
f.write("Account SID : " + str(call.account_sid) + "\n")
f.write("Annotation : " + str(call.annotation) + "\n")
f.write("Answered By : " + str(call.answered_by) + "\n")
f.write("API Version : " + str(call.api_version) + "\n")
f.write("Caller Name : " + str(call.caller_name) + "\n")
f.write("Date Created : " + str(call.date_created) + "\n")
f.write("Date Updated : " + str(call.date_updated) + "\n")
f.write("Direction : " + str(call.direction) + "\n")
f.write("Duration : " + str(call.duration) + "\n")
f.write("End Time : " + str(call.end_time) + "\n")
f.write("Forwarded From : " + str(call.forwarded_from) + "\n")
f.write("From : " + str(call.from_) + "\n")
f.write("From Formatted : " + str(call.from_formatted + "\n"))
f.write("Group SID : " + str(call.group_sid) + "\n")
f.write("Parent Call SID : " + str(call.parent_call_sid) + "\n")
f.write("Phone Number SID : " + str(call.phone_number_sid) + "\n")
f.write("Price : " + str(call.price) + "\n")
f.write("Price Unit : " + str(call.price_unit) + "\n")
f.write("SID : " + str(call.sid) + "\n")
f.write("Start Time : " + str(call.start_time) + "\n")
f.write("Status : " + str(call.status) + "\n")
f.write("Subresource URIs : " + str(call.subresource_uris) + "\n")
f.write("To : " + str(call.to) + "\n")
f.write("To Formatted : " + str(call.to_formatted) + "\n")
f.write("URI : " + str(call.uri) + "\n")
f.close()