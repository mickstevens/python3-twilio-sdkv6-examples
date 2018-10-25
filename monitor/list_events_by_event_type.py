# *** List Events by Event Type ***
# Code based on https://www.twilio.com/docs/usage/monitor-events
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from datetime import datetime # not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python/python3-twilio-sdkv6-examples/monitor/logs/twilio_monitor.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of event parameters & their permissable values, comment out (#) those lines not required

events = client.monitor.events.list(
                                   end_date=datetime(2018, 10, 25, 0, 0),
                                   event_type='phone-number.created',
# List possible valid event types:
# account.created 
# account.updated 
# account.deleted
# application.created 
# application.updated 
# application.deleted
# authorized-connect-app.created
# authorized-connect-app.deleted
# call.deleted
# caller-id.created 
# caller-id.updated 
# caller-id.deleted
# connect-app.created 
# connect-app.updated 
# connect-app.deleted
# invoice-settings.updated
# message.updated 
# message.deleted
# message-body.deleted
# message-media.deleted
# payment.created
# payment-method.created
# payment-method.updated
# payment-method.deleted
# payment-refund.created
# phone-number.created
# phone-number.updated
# phone-number.deleted
# recharge-trigger.created
# recharge-trigger.updated
# recharge-trigger.deleted
# recording.deleted
# shortcode.created 
# shortcode.updated 
# shortcode.deleted
# sip-credential-list.created
# sip-credential-list.updated
# sip-credential-list.deleted
# sip-domain.created 
# sip-domain.updated 
# sip-domain.deleted
# sip-ip-access-control-list.created
# sip-ip-access-control-list.updated
# sip-ip-access-control-list.deleted
# support-plan.updated
# sms-geographic-permissions.updated
# transcription.deleted
# usage-trigger.created
# usage-trigger.updated
# usage-trigger.deleted
# voice-geographic-permissions.updated
# wireless-sim.updated
                                   start_date=datetime(2017, 12, 31, 0, 0)
                                   )

#print list of all event properties to console, useful for learning info available you can work with?

for record in events:
    print(record.account_sid)
    print(record.actor_sid)
    print(record.actor_type)
    print(record.description)
    print(record.event_data)
    print(record.event_date)
    print(record.event_type)
    print(record.links)
    print(record.resource_sid)
    print(record.resource_type)
    print(record.sid)
    print(record.source)
    print(record.source_ip_address)
    print(record.url)

#create variable for this event
cdr = (record.sid)

f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/monitor/logs/" + str( cdr ) + ".log", "a")
#write list of all event properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("Actor SID : " + str(record.actor_sid) + "\n")
f.write("Actor Type : " + str(record.actor_type) + "\n")
f.write("Description : " + str(record.description) + "\n")
f.write("Event Data : " + str(record.event_data) + "\n")
f.write("Event Date : " + str(record.event_date) + "\n")
f.write("Event Type : " + str(record.event_type) + "\n")
f.write("Links : " + str(record.links) + "\n")
f.write("Resoure SID : " + str(record.resource_sid) + "\n")
f.write("Resoure Type : " + str(record.resource_type) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Source : " + str(record.source) + "\n")
f.write("Source IP Address : " + str(record.source_ip_address) + "\n")
f.write("URL : " + str(record.url) + "\n")
f.close()