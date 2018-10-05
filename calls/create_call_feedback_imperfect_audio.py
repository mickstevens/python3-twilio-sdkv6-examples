# *** Create Call Feedback for Imperfect Audio ***
# Code based on https://www.twilio.com/docs/voice/api/call-quality-feedback
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/calls/logs/call_feedback.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of call feedback parameters & their permissable values, comment out (#) those lines not required:

feedback = client.calls("CAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") \
                 .feedback() \
                 .create(quality_score=4, #1-5, where 1=imperfect & 5=perfect
                         issue=['imperfect-audio'])

#print list of all call feedback properties to console, useful for learning info available you can work with?

print(feedback.account_sid)
print(feedback.date_created)
print(feedback.date_updated)
print(feedback.issues)
print(feedback.quality_score)
print(feedback.sid)

#create variable for this call
cdr = (feedback.issues)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/calls/logs/" + str( cdr ) + ".log", "a")
#write list of all call feedback properties to above file...
f.write("Account SID : " + str(feedback.account_sid) + "\n")
f.write("Date Created : " + str(feedback.date_created) + "\n")
f.write("Date Updated : " + str(feedback.date_updated) + "\n")
f.write("Issues : " + str(feedback.issues) + "\n")
f.write("Quality Score : " + str(feedback.quality_score) + "\n")
f.write("SID : " + str(feedback.sid) + "\n")
f.close()