# *** List Chat Services ***
# Code based on https://www.twilio.com/docs/chat/rest/services
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

# A list of chat services parameters & their permissable values

services = client.chat.services.list()

#print list of all chat services properties to console, useful for learning info available you can work with?

for record in services:
    print(record.account_sid)
    print(record.consumption_report_interval)
    print(record.date_created)
    print(record.date_updated)
    print(record.default_channel_creator_role_sid)
    print(record.default_channel_role_sid)
    print(record.default_service_role_sid)
    print(record.friendly_name)
    print(record.limits)
    print(record.links)
    print(record.notifications)
    print(record.post_webhook_retry_count)
    print(record.post_webhook_url)
    print(record.pre_webhook_retry_count)
    print(record.pre_webhook_url)
    print(record.reachability_enabled)
    print(record.read_status_enabled)
    print(record.sid)
    print(record.typing_indicator_timeout)
    print(record.url)
    print(record.webhook_filters)
    print(record.webhook_method)

#create variable for this service
cdr = (record.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat services properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Consumption Report Interval : " + str(record.consumption_report_interval) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("Default Channel Creator Role SID : " + str(record.default_channel_creator_role_sid) + "\n")
f.write("Default Channel Role SID : " + str(record.default_channel_role_sid) + "\n")
f.write("Default Service Role SID : " + str(record.default_service_role_sid) + "\n")
f.write("Friendly Name : " + str(record.friendly_name) + "\n")
f.write("Limits : " + str(record.limits) + "\n")
f.write("Links : " + str(record.links) + "\n")
f.write("Notifications : " + str(record.notifications) + "\n")
f.write("Post Webhook Retry Count : " + str(record.post_webhook_retry_count) + "\n")
f.write("Post Webhook Retry URL : " + str(record.post_webhook_url) + "\n")
f.write("Pre Webhook Retry Count : " + str(record.pre_webhook_retry_count) + "\n")
f.write("Pre Webhook Retry URL : " + str(record.pre_webhook_retry_url) + "\n")
f.write("Reachability Enabled : " + str(record.reachability_enabled) + "\n")
f.write("Read Status Enabled : " + str(record.read_status_enabled) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Typing Indicator Timeout : " + str(record.typing_indicator_timeout) + "\n")
f.write("URL : " + str(record.url) + "\n")
f.write("Webhook Filters : " + str(record.webhook_filters) + "\n")
f.write("Webhook Method : " + str(record.webhook_method) + "\n")
f.close()
