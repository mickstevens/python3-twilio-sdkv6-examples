# *** List Faxes for account ***
# Code based on https://www.twilio.com/docs/fax/api
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/fax/logs/twilio_fax.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of fax parameters & their permissable values, comment out (#) those lines not required

faxes = client.fax.faxes.list()

#print list of all fax properties to console, useful for learning info available you can work with?

for record in faxes:
    print(record.account_sid)
    print(record.api_version)
    print(record.date_created)
    print(record.date_updated)
    print(record.direction)
    print(record.duration)
    print(record.from_)
    print(record.links)
    print(record.media_sid)
    print(record.media_url)
    print(record.num_pages)
    print(record.price)
    print(record.price_unit)
    print(record.quality)
    print(record.sid)
    print(record.status)
    print(record.to)
    print(record.url)

#create variable for this fax
cdr = (record.sid)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/fax/logs/" + str( cdr ) + ".log", "a")
#write list of all fax properties to above file...
f.write("Account SID : " + str(record.account_sid) + "\n")
f.write("API Version : " + str(record.api_version) + "\n")
f.write("Date Created : " + str(record.date_created) + "\n")
f.write("Date Updated : " + str(record.date_updated) + "\n")
f.write("Direction : " + str(record.direction) + "\n")
f.write("Duration : " + str(record.duration) + "\n")
f.write("From : " + str(record.from_) + "\n")
f.write("Links : " + str(record.links + "\n")
f.write("Media SID : " + str(record.media_sid) + "\n")
f.write("Media URL : " + str(record.media_url) + "\n")
f.write("No. of Pages : " + str(record.num_pages) + "\n")
f.write("Price : " + str(record.price) + "\n")
f.write("Price Unit : " + str(record.price_unit) + "\n")
f.write("Quality : " + str(record.quality) + "\n")
f.write("SID : " + str(record.sid) + "\n")
f.write("Status : " + str(record.status) + "\n")
f.write("To : " + str(record.to) + "\n")
f.write("URL : " + str(record.url) + "\n")
f.close()