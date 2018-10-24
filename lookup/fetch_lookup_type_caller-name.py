# *** Fetch a Lookup ***
# Code based on https://www.twilio.com/docs/lookup/api
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# from datetime import datetime | not required for this example
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python3/sdkv6x/lookup/logs/twilio_lookup.log',
                    filemode='a')

# Your Account Sid and Auth Token from twilio.com/console & stored in Mac OS ~/.bash_profile in this example 
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('$TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# A list of lookup parameters & their permissable values, comment out (#) those lines not required

phone_number = client.lookups \
                            .phone_numbers('16502530000') \
                            .fetch(
                            add_ons='', # Optional, Add-On Unique Names 
                            country_code='US', # Optional, ISO Country Code
                            type='caller-name' # Optional, or caller-name, default = null, fraud = bet
                            )

#print list of all lookup properties to console, useful for learning info available you can work with?

print(phone_number.add_ons)
print(phone_number.caller_name)
print(phone_number.carrier)
print(phone_number.country_code)
print(phone_number.national_format)
print(phone_number.phone_number)
print(phone_number.url)

#create variable for this lookup
cdr = (phone_number.phone_number)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/lookup/logs/" + str( cdr ) + ".log", "a")
#write list of all lookup properties to above file...
f.write("Add Ons : " + str(phone_number.add_ons) + "\n")
f.write("Caller Name : " + str(phone_number.caller_name) + "\n")
f.write("Carrier : " + str(phone_number.carrier) + "\n")
f.write("Country Code : " + str(phone_number.country_code) + "\n")
f.write("National Format : " + str(phone_number.national_format) + "\n")
f.write("Phone No. : " + str(phone_number.phone_number) + "\n")
f.write("url : " + str(phone_number.url) + "\n")
f.close()