# *** Create a Notification with Identity & Tag ***
# Code based on https://www.twilio.com/docs/notify/api
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/python3_twilio-sdkv6_examples/notify/logs/twilio_notify.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of Notifcation parameters & their permissable values, comment out (#) those lines not required
notification = client.notify \
                     .services('ISxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') \
                     .notifications \
                     .create(
                          body='Hello Bob',
                          identity='00000001',
                          tag='preferred_device'
                      )
                      
#print list of all Notification properties to console, useful for learning info available you can work with?
print(notification.account_sid)
print(notification.action)
print(notification.alexa)
print(notification.apn)
print(notification.body)
print(notification.data)
print(notification.date_created)
print(notification.facebook_messenger)
print(notification.fcm)
print(notification.gcm)
print(notification.identities)
print(notification.priority)
print(notification.segments)
print(notification.service_sid)
print(notification.sid)
print(notification.sms)
print(notification.sound)
print(notification.tags)
print(notification.title)
print(notification.ttl)

#create variable for this Notification
cdr = (notification.sid)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/python3_twilio-sdkv6_examples/notify/logs/" + str( cdr ) + ".log", "a")
#write list of all Notification properties to above file...
f.write("Account SID : " + str(notification.account_sid) + "\n")
f.write("Action : " + str(notification.action) + "\n")
f.write("Alexa : " + str(notification.alexa) + "\n")
f.write("APN : " + str(notification.apn) + "\n")
f.write("Body : " + str(notification.body) + "\n")
f.write("Data : " + str(notification.data) + "\n")
f.write("Date Created : " + str(notification.date_created) + "\n")
f.write("Facebook Messenger : " + str(notification.facebook_messenger) + "\n")
f.write("GCM : " + str(notification.gcm) + "\n")
f.write("Identities : " + str(notification.identities) + "\n")
f.write("Priority : " + str(notification.priority) + "\n")
f.write("Segments : " + str(notification.segments) + "\n")
f.write("Service SID : " + str(notification.service_sid) + "\n")
f.write("SID : " + str(notification.sid) + "\n")
f.write("SMS : " + str(notification.sms) + "\n")
f.write("Sound : " + str(notification.sound) + "\n")
f.write("Tags : " + str(notification.tags) + "\n")
f.write("Title : " + str(notification.title) + "\n")
f.write("TTL : " + str(notification.ttl) + "\n")
f.close()
