#!/usr/bin/python3

from platform import processor

from datetime import datetime, timezone
import secrets
import string
import hashlib
import requests

from abc import abstractclassmethod, abstractmethod,ABC

def __init__(self):
    

    pass

    config_url = {
        "API_key" : {'K6Y6W12OCmIR4merI0yeF2NWX89gGLTr6fUyNPQIvfrgyuqhnpkSFBzmOblV9zAcwyvnFrCxqGLkJPef23KB5HTjqqPLhLzGuk3V6HJtsg3kenF3YH69egW20lGf7119'},
        "API_id"  : {'10'},
        "fqdn"    :{'https://api-woolworthssa.xdr.uk.paloaltonetworks.com/'},
        "API_name" :{''} 

    }

'''
    curl -X POST https://api-woolworthssa.xdr.uk.paloaltonetworks.com/public_api/v1/incidents/get_incidents/ \
-H "x-xdr-auth-id:10" \
-H "Authorization:K6Y6W12OCmIR4merI0yeF2NWX89gGLTr6fUyNPQIvfrgyuqhnpkSFBzmOblV9zAcwyvnFrCxqGLkJPef23KB5HTjqqPLhLzGuk3V6HJtsg3kenF3YH69egW20lGf7119" \
-H "Content-Type:application/json" \
-d '{ 
   "request_data":{}
   }'

'''



# abstractmethod
def test_advanced_authentication(api_key_id, api_key):
   # Generate a 64 bytes random string
    nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
    # Get the current timestamp as milliseconds.
    timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
    # Generate the auth key:
    auth_key = "%s%s%s" % (api_key, nonce, timestamp)
    # Convert to bytes object
    auth_key = auth_key.encode("utf-8")
    # Calculate sha256:
    api_key_hash = hashlib.sha256(auth_key).hexdigest()
    # Generate HTTP call headers
    headers = {
        "x-xdr-timestamp": str(timestamp),
        "x-xdr-nonce": nonce,
        "x-xdr-auth-id": str(api_key_id),
        "Authorization": api_key_hash
    }
    parameters = {}
    res = requests.post(url="https://api-woolworthssa.xdr.uk.paloaltonetworks.com/public_api/v1/incidents/get_incidents/",
						headers=headers,
						json=parameters)
    return res

