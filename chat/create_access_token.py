# *** Create Access Token for Chat ***
# Code based on https://www.twilio.com/docs/chat/create-tokens
# Download Python 3 from https://www.python.org/downloads/
# Download the Twilio helper library from https://www.twilio.com/docs/python/install
import os
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
import logging
#write requests & responses from Twilio to log file, useful for debugging:
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/twilio_chat.log',
                    filemode='a')

# required for all twilio access tokens
account_sid = os.environ.get('$TWILIO_ACCOUNT_SID')
api_key = os.environ.get('$TWILIO_API_KEY')
api_secret = os.environ.get('$TWILIO_API_SECRET')

# required for Chat grants
service_sid = os.environ.get('$TWILIO_SERVICE_SID')
identity = os.environ.get('$TWILIO_IDENTITY')

# Create access token with credentials
token = AccessToken(account_sid, api_key, api_secret, identity=identity)

# Create an Chat grant and add to token
chat_grant = ChatGrant(service_sid=service_sid)
token.add_grant(chat_grant)

# Return token info as JSON
print(token.add_grant)
print(token.from_jwt)
print(token.headers)
print(token.payload)
print(token.to_jwt())

#create variable for this record
cdr = (token.to_jwt)
#open *.log file with cdr var as filename...
f = open("/usr/local/twilio/python/python3-twilio-sdkv6-examples/chat/logs/" + str( cdr ) + ".log", "a")
#write list of all chat invite properties to above file...
f.write("Add Grant : " + str(token.add_grant) + "\n")
f.write("From JWT : " + str(token.from_jwt) + "\n")
f.write("Headers : " + str(token.headers) + "\n")
f.write("Payload : " + str(token.payload) + "\n")
f.write("To JWT : " + str(token.to_jwt) + "\n")
f.close()
