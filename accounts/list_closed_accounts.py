# *** List Accounts by status - closed ***
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

accounts = client.api.accounts.list(status='closed')

#print list of all account properties to console, useful for learning info available you can work with?
for record in accounts:

    print(record.auth_token)
    print(record.date_created)
    print(record.date_updated)
    print(record.friendly_name)
    print(record.owner_account_sid)
    print(record.sid)
    print(record.status)
    print(record.subresource_uris)
    print(record.type)
    print(record.uri)

#create variable for this account
cdr = (record.sid)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/accounts/logs/" + str( cdr ) + ".log", "a")
#write list of all account properties to above file...
f.write("Auth Token : " + str(record.auth_token) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Update : " + str(record.date_updated) + "\n")
f.write("Friendly Name : " + str(record.friendly_name) + "\n")
f.write("Owner record SID : " + str(record.owner_account_sid) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Status : " + str(record.status) + "\n")
f.write("Subresource URIs : " + str(record.subresource_uris) + "\n")
f.write("Type : " + str(record.type) + "\n")
f.write("URI : " + str(record.uri) + "\n")
f.close()
