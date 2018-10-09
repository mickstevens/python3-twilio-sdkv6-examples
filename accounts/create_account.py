# *** Create Account ***
# Code based on https://www.twilio.com/docs/iam/api/account
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
#from datetime import datetime | not required for this examples
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/accounts/logs/twilio_accounts.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of account parameters & their permissable values

account = client.api.accounts.create()

#print list of all account properties to console, useful for learning info available you can work with?
print(account.auth_token)
print(account.date_created)
print(account.date_updated)
print(account.friendly_name)
print(account.owner_account_sid)
print(account.sid)
print(account.status)
print(account.subresource_uris)
print(account.type)
print(account.uri)

#create variable for this account
cdr = (account.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/accounts/logs/" + str( cdr ) + ".log", "a")
#write list of all account properties to above file...
f.write("Auth Token : " + str(account.auth_token) + "\n")
f.write("Date Created : " + str(account.date_created) + "\n")
f.write("Date Update : " + str(account.date_updated) + "\n")
f.write("Friendly Name : " + str(account.friendly_name) + "\n")
f.write("Owner Account SID : " + str(account.owner_account_sid) + "\n")
f.write("SID : " + str(account.sid) + "\n")
f.write("Status : " + str(account.status) + "\n")
f.write("Subresource URIs : " + str(account.subresource_uris) + "\n")
f.write("Type : " + str(account.type) + "\n")
f.write("URI : " + str(account.uri) + "\n")
f.close()
