# *** Delete Call Feedback Summary ***
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

# A list of call feedback summary parameters & their permissable values, comment out (#) those lines not required:

# FSe6b77c80b547957f8ab7329b5c0b556c

client.calls \
      .feedback_summaries("FSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") \
      .delete()
