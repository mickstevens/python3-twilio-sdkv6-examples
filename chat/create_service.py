# *** Create Chat Services ***
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

service = client.chat.services.create(
                                     friendly_name="TO_BE_DELETED"
                                     )

#print list of all chat services properties to console, useful for learning info available you can work with?

print(service.account_sid)
print(service.consumption_report_interval)
print(service.date_created)
print(service.date_updated)
print(service.default_channel_creator_role_sid)
print(service.default_channel_role_sid)
print(service.default_service_role_sid)
print(service.friendly_name)
print(service.limits)
print(service.links)
print(service.notifications)
print(service.post_webhook_retry_count)
print(service.post_webhook_url)
print(service.pre_webhook_retry_count)
print(service.pre_webhook_url)
print(service.reachability_enabled)
print(service.read_status_enabled)
print(service.sid)
print(service.typing_indicator_timeout)
print(service.url)
print(service.webhook_filters)
print(service.webhook_method)

#create variable for this service
cdr = (service.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat services properties to above file...
f.write("Account SID : " + str(service.account_sid) + "\n")
f.write("Consumption Report Interval : " + str(service.consumption_report_interval) + "\n")
f.write("Date Created : " + str(service.date_created) + "\n")
f.write("Date Updated : " + str(service.date_updated) + "\n")
f.write("Default Channel Creator Role SID : " + str(service.default_channel_creator_role_sid) + "\n")
f.write("Default Channel Role SID : " + str(service.default_channel_role_sid) + "\n")
f.write("Default Service Role SID : " + str(service.default_service_role_sid) + "\n")
f.write("Friendly Name : " + str(service.friendly_name) + "\n")
f.write("Limits : " + str(service.limits) + "\n")
f.write("Links : " + str(service.links) + "\n")
f.write("Notifications : " + str(service.notifications) + "\n")
f.write("Post Webhook Retry Count : " + str(service.post_webhook_retry_count) + "\n")
f.write("Post Webhook Retry URL : " + str(service.post_webhook_url) + "\n")
f.write("Pre Webhook Retry Count : " + str(service.pre_webhook_retry_count) + "\n")
f.write("Pre Webhook Retry URL : " + str(service.pre_webhook_retry_url) + "\n")
f.write("Reachability Enabled : " + str(service.reachability_enabled) + "\n")
f.write("Read Status Enabled : " + str(service.read_status_enabled) + "\n")
f.write("SID : " + str(service.sid) + "\n")
f.write("Typing Indicator Timeout : " + str(service.typing_indicator_timeout) + "\n")
f.write("URL : " + str(service.url) + "\n")
f.write("Webhook Filters : " + str(service.webhook_filters) + "\n")
f.write("Webhook Method : " + str(service.webhook_method) + "\n")
f.close()
