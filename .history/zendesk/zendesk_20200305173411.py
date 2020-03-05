#!/usr/bin/env python

from zenpy import Zenpy
import datetime
import os
import requests
import json
import ast
# Zenpy accepts an API token
creds = {
    'email' : 'fsoler@wigilabs.com',
    'token' : 'AsQqNqvMl1Kvgrz5Vz4IjbEu4yZiuPs0uGiyeRT6',
    'subdomain': 'wigilabs'
}

nrheaders={'Content-type': 'application/json', 'x-insert-key' : 'NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4'}
nrAPI='https://insights-collector.newrelic.com/v1/accounts/2482859/events'

zenpy_client = Zenpy(**creds)
nrevent='OpenTicket'
str =zenpy_client.search(type='ticket', status='open')
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
result_generator = zenpy_client.tickets.incremental(start_time=yesterday)
aobj=[{ "eventType" : nrevent , "content" : "0","ticketid":"0" }]
print(aobj[0])
print (type(result_generator))
for ticket in result_generator:
    last_ticket_open=ticket.id
    userId=ticket.assignee
    print (ticket.id)
    for comment in zenpy_client.tickets.comments(ticket=last_ticket_open):
        content=comment.body
        print comment.body
        aobj[0].update({"content": content.encode("utf-8")})
        aobj[0].update({"ticketid": last_ticket_open})
        data=json.dumps(aobj)
        print(data)
        req=requests.post(nrAPI, data=json.dumps(aobj), headers=nrheaders)
        data = []
        curlData = 'curl -X POST -i -H "x-insert-key:NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4" -H "Content-Type: application/json" --data "{}"  https://insights-collector.newrelic.com/v1/accounts/2482859/events'.format(data)
        print("*"*100)
        print(json.dumps(curlData))
        print("*"*100)
        os.system(curlData)
audit_generator = zenpy_client.tickets.audits()
# You can retrieve the cursor values from the generator.
print(audit_generator.after_cursor, audit_generator.before_cursor)
# Iterate over the last 1000 audits.
for audit in audit_generator:
    print(audit)
# Reversing the generator reverses the direction in which you consume objects. The
# following grabs objects from just before the cursor value until the beginning of time.
for audit in reversed(zenpy_client.tickets.audits(cursor='fDE1MTc2MjkwNTQuMHx8')):
    print(audit)
index=0
for ticket in zenpy_client.tickets(include=['users']):
    print(ticket.submitter)
    index=index+1
    last_user=ticket.submitter
for user in zenpy_client.users():
    print user.name
    last_client=user.name
for comment in zenpy_client.tickets.comments(ticket=index):
    print comment
    id_content=comment
    content_ticket=comment.body
##Create json object
print ('"eventType" : "ticketLog", "user_id" : "{}", "client":"{}", "content":"{}" '.format(last_user, last_client, id_content))
str='"eventType" : "ticketLog", "user_id" : "{}", "client":"{}", "content":"{}" '.format(last_user, last_client, id_content)
obj='[{' + str + '}]'
URL='https://insights-collector.newrelic.com/v1/accounts/2482859/events'
nrheaders={'Content-type': 'application/json', 'x-insert-key' : 'NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4'}
req=requests.post(URL, data=obj, headers=nrheaders)
print(" >>> Object send: " + obj)
if req.status_code== 200:
    print("=> Success")
else:
    print("=> Error")
