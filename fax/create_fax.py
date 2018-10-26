# *** Create a Fax ***
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
fax = client.fax.faxes.create(
                             from_='+15017122661', # Optional?
                             to='+15558675310', # Required, phone number or SIP address
                             media_url='https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf', # Required, HTTP(S) URL 
                             quality='superfine', # Optional, or standard or fine (default)
                             sip_auth_password='', # Optional
                             sip_auth_username='', # Optional
                             status_callback='', # Optional, URL that will receive a POST
                             store_media='false', # Optional, or true (default) store media on Twilio servers  
                             ttl='' # Optional, How many minutes from when a fax was initiated should Twilio attempt to send a fax
                             )
#print list of all fax properties to console, useful for learning info available you can work with?
print(fax.account_sid)
print(fax.api_version)
print(fax.date_created)
print(fax.date_updated)
print(fax.direction)
print(fax.duration)
print(fax.from_)
print(fax.links)
print(fax.media_sid)
print(fax.media_url)
print(fax.num_pages)
print(fax.price)
print(fax.price_unit)
print(fax.quality)
print(fax.sid)
print(fax.status)
print(fax.to)
print(fax.url)

#create variable for this fax
cdr = (fax.sid)

#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python3/sdkv6x/fax/logs/" + str( cdr ) + ".log", "a")
#write list of all fax properties to above file...
f.write("Account SID : " + str(fax.account_sid) + "\n")
f.write("API Version : " + str(fax.api_version) + "\n")
f.write("Date Created : " + str(fax.date_created) + "\n")
f.write("Date Updated : " + str(fax.date_updated) + "\n")
f.write("Direction : " + str(fax.direction) + "\n")
f.write("Duration : " + str(fax.duration) + "\n")
f.write("From : " + str(fax.from_) + "\n")
f.write("Links : " + str(fax.links) + "\n")
f.write("Media SID : " + str(fax.media_sid) + "\n")
f.write("Media URL : " + str(fax.media_url) + "\n")
f.write("No. of Pages : " + str(fax.num_pages) + "\n")
f.write("Price : " + str(fax.price) + "\n")
f.write("Price Unit : " + str(fax.price_unit) + "\n")
f.write("Quality : " + str(fax.quality) + "\n")
f.write("SID : " + str(fax.sid) + "\n")
f.write("Status : " + str(fax.status) + "\n")
f.write("To : " + str(fax.to) + "\n")
f.write("URL : " + str(fax.url) + "\n")
f.close()