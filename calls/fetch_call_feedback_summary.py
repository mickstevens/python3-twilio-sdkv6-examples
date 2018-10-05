# *** Fetch Call Feedback Summary ***
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

summary = client.calls \
                .feedback_summaries("FSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") \
                .fetch()


print(summary.account_sid)
print(summary.call_count)
print(summary.call_feedback_count)
print(summary.date_created)
print(summary.date_updated)
print(summary.end_date)
print(summary.issues)
print(summary.quality_score_average)
print(summary.quality_score_median)
print(summary.quality_score_standard_deviation)
print(summary.sid)
print(summary.start_date)
print(summary.status)

#create variable for this call
cdr = (summary.sid)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/calls/logs/" + str( cdr ) + ".log", "a")
#write list of all call feedback properties to above file...
f.write("Account SID : " + str(summary.account_sid) + "\n")
f.write("Call Count : " + str(summary.call_count) + "\n")
f.write("Call Feedback Count : " + str(summary.call_feedback_count) + "\n")
f.write("Date Created : " + str(summary.date_created) + "\n")
f.write("Date Updated : " + str(summary.date_updated) + "\n")
f.write("End Date : " + str(summary.end_date) + "\n")
f.write("Issues : " + str(summary.issues) + "\n")
f.write("Quality Score Average : " + str(summary.quality_score_average) + "\n")
f.write("Quality Score Median : " + str(summary.quality_score_median) + "\n")
f.write("Quality Score Standard Deviation : " + str(summary.quality_score_standard_deviation) + "\n")
f.write("SID : " + str(summary.sid) + "\n")
f.write("Start Date : " + str(summary.start_date) + "\n")
f.write("Status : " + str(summary.status) + "\n")
f.close()