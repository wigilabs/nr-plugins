#!/usr/bin/env/ python
#zenpy.lib.exception.APIException
from zenpy import Zenpy
import datetime
import requests
creds = {
    'email' : 'fsoler@wigilabs.com',
    'token' : 'KReVfF0YKjP3FULMTnQIDZ3J7fjQywNT8saaoM8x',
    'subdomain': 'wigilabs4435'
}
nrheaders={'Content-type': 'application/json', 'x-insert-key' : 'NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4'}
nrAPI='https://insights-collector.newrelic.com/v1/accounts/2482859/events'
zenpy_client = Zenpy(**creds)
validate = zenpy_client.search(type='ticket')
last_check=datetime.datetime.now()
URL='https://insights-collector.newrelic.com/v1/accounts/2482859/events'
nrheaders={'Content-type': 'application/json', 'x-insert-key' : 'NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4'}
if validate is not None: 
    print "online"
    print validate
    str='"eventType" : "zendeskStatus", "status" : "online", "lastCheck":"{}"'.format(last_check)
    obj='[{' + str + '}]'
    req=requests.post(URL, data=obj, headers=nrheaders)
    print(" >>> Object send: " + obj)
    if req.status_code == 200:
        print("=> Success event insights")
    else:
        print("=> Error sending data")
else:
    print "offline"
    print validate
    str='"eventType" : "zendeskStatus", "status" : "offline", "lastCheck":"{}"'.format(last_check)
    obj='[{' + str + '}]'
    req=requests.post(URL, data=obj, headers=nrheaders)
    print(" >>> Object send: " + obj)
    if req.status_code == 200:
        print("=> Success event insights")
    else:
        print("=> Error sending data")
