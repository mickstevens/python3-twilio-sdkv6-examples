# *** Create an APN Credential for Chat ***
# Code based on https://www.twilio.com/docs/chat/rest/credentials
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

# A list of chat credentials parameters & their permissable values

credential = client.chat.credentials.create(
                                         type='apn', # Required, apn, fcm or gcm
#                                        api_key='apn_api_Key', # gcm only
#                                        certificate='', # Optional, apn only, url encoded representation of the certificate
                                         friendly_name='create_apn_credential_all_parms', # Optional, 
#                                        private_key='', # Optional, apn only, url encoded representation of the private key
                                         sandbox='false' # Optional, apn only, use this credential for sending to production or sandbox apn
#                                        secret='' # Optional, fcm only, This is the "Server key" of your project from Firebase console under Settings / Cloud messaging
                                     )
#print list of all chat credentials properties to console, useful for learning info available you can work with?

print(credential.account_sid)
print(credential.date_created)
print(credential.date_updated)
print(credential.friendly_name)
print(credential.sandbox)
print(credential.sid)
print(credential.type)
print(credential.url)

#create variable for this record
cdr = (credential.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat credentials properties to above file...
f.write("Account SID : " + str(credential.account_sid) + "\n")
f.write("Date Created : " + str(credential.date_created) + "\n")
f.write("Date Updated : " + str(credential.date_updated) + "\n")
f.write("Friendly Name : " + str(credential.friendly_name) + "\n")
f.write("Sandbox : " + str(credential.sandbox) + "\n")
f.write("SID : " + str(credential.sid) + "\n")
f.write("Type : " + str(credential.type) + "\n")
f.write("URL : " + str(credential.url) + "\n")
f.close()
