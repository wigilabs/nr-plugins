# encoding: utf-8
import requests
import json
import ast
import os
import mysql.connector

db = mysql.connector.connect(
  host="tcp.ngrok.io",
  port="16714",
  user="root",
  passwd="",
  database="LIGHTNING_TEAM"
)
cursor=db.cursor();
sql='INSERT INTO TASKS(SEQ, MONITOR, CLIENT_NAME, DATA_STREAM, TIME_EVENT) VALUES(0, "zabbix", %s, %s, NOW());'

nrheaders={'Content-type': 'application/json', 'x-insert-key' : 'NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4'}
nrAPI='https://insights-collector.newrelic.com/v1/accounts/2482859/events'
API='http://64.227.58.169/zabbix/api_jsonrpc.php'
data = {'jsonrpc': '2.0', 'method': 'user.login', 'params': {  "user": "Admin", "password": "zabbix"},"id": 1 }
headers = {'Content-type': 'application/json'}
response = requests.post(API, data=json.dumps(data), headers=headers)
print(">>> Status : ",response)
print(">>> Content : ", json.dumps(response.json()))
auth = json.dumps(response.json())[30:62];

## Get data
###  Host list
hostList = {
        "jsonrpc": "2.0",
        "method": "host.get",
         "params": {
                "output": [
                "hostid",
                "host"
                ],

         "selectInterfaces": [
                "interfaceid",
                "ip"
                ]
                },
                "id": 1,
        "auth": auth
                }
template = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "selectParentTemplates": [
            "templateid",
            "name"
        ],
        "hostids": "10084"
    },
    "id": 1,
    "auth": auth
}

maintance = {
    "jsonrpc": "2.0",
    "method": "maintenance.get",
    "params": {
        "output": "extend",
        "selectGroups": "extend",
        "selectTimeperiods": "extend"
    },
    "auth": auth,
    "id": 1
}

ZabbixAgent = {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "triggerids": "15982",
        "output": "extend",
        "selectFunctions": "extend"
    },
    "auth": auth,
    "id": 1
}

HTTP = {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "triggerids": "13545",
        "output": "extend",
        "selectFunctions": "extend"
    },
    "auth": auth,
    "id": 1
}

SSH = {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "triggerids": "15986",
        "output": "extend",
        "selectFunctions": "extend"
    },
    "auth": auth,
    "id": 1
}

events = {
         "jsonrpc": "2.0",
    "method": "event.get",
    "params": {
            "output": "extend",
            "selectHosts": "ubuntu",
            "selectRelatedObject": "extend"
},
    "auth": auth,
    "id": 1
}

response = requests.post(API, data=json.dumps(hostList), headers=headers)
response1 = requests.post(API, data=json.dumps(template), headers=headers)
response2 = requests.post(API, data=json.dumps(maintance), headers=headers)
trigger1 = requests.post(API, data=json.dumps(ZabbixAgent), headers=headers)
trigger2 = requests.post(API, data=json.dumps(HTTP), headers=headers)
trigger3 = requests.post(API, data=json.dumps(SSH), headers=headers)
#response4 = requests.post(API, data=json.dumps(events), headers=headers)
if response.status_code == 200:
    print(">>> Hostlist : ",response)
    print(">>> Content : ", json.dumps(response.json()))
    current = ast.literal_eval(json.dumps(response.json()["result"]))
    current[0].update({"eventType":"zabbixHostTemplate"})
    current[1].update({"eventType":"zabbixHostTemplate"})
    print("[========================================================================================================================================================================]")
    local=str(current[0])[:-2].replace("[","")
    remote=str(current[1])[:-2].replace("[","")
    local=local.replace("u'interfaces': {","")
    remote=remote.replace("u'interfaces': {","")
    local='['+local+']'
    remote='['+remote+']'
##Enviar hostlist a new relic
    local=local.replace("'interfaces': {","")
    remote=remote.replace("'interfaces': {","")
    local=local.replace("'interfaces': {","")
    remote=remote.replace("\'","\"")
    local=local.replace("\'","\"")
    print(local)
    print(remote)
    os.system('curl -X POST -i -H "x-insert-key:NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4" -H "Content-Type: application/json" --data "+ json.dumps(local).json() +" https://insights-collector.newrelic.com/v1/accounts/2482859/events')
    os.system('curl -X POST -i -H "x-insert-key:NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4" -H "Content-Type: application/json" --data "+ json.dumps(remote).json() +" https://insights-collector.newrelic.com/v1/accounts/2482859/events')
    val=("movii",local.decode('utf-8'))
    cursor.execute(sql,val)
    db.commit()
    val=("movii",remote.decode('utf-8'))
    cursor.execute(sql,val)
    db.commit()
    #nr
    customEvent1=requests.post(nrAPI, data=local, headers=nrheaders)
    customEvent2=requests.post(nrAPI, data=remote, headers=nrheaders)
elif response.status_code == 404:
    print('Not Found.')

##################################################

if trigger1.status_code == 200:
    print(">>> ZabbixAgent : ",trigger1)
    print(">>> Content : ", json.dumps(trigger1.json()))
    current = ast.literal_eval(json.dumps(trigger1.json()["result"]))
    print("[======================================================================[ Crafted Data ]===================================================================================]")
    current[0].update({"eventType" : "ZabbixAgent"})
    print (current[0])
    agentData=current[0]
    print("agent data:")
    strAgent=str(agentData).replace("'functions': [{'itemid': '28727', 'function': 'diff', 'triggerid': '15982', 'parameter': '0', 'functionid': '18287'}],","")
    strAgent= "[" + strAgent + "]"
    strAgent=strAgent.replace("'status': '0', ","")
    strAgent=strAgent.replace("'","\"")
    print(strAgent)
    os.system('curl -X POST -i -H "x-insert-key:NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4" -H "Content-Type: application/json" --data "+ json.dumps(strAgent).json() +" https://insights-collector.newrelic.com/v1/accounts/2482859/events')
    val1=("movii",strAgent.decode('utf-8'))
    cursor.execute(sql,val1)
    db.commit()
    req=requests.post(nrAPI, data=strAgent, headers=nrheaders)
    if req.status_code== 200:
        print("=> Success")
    else:
        print("=> Error")
    print("[========================================================================================================================================================================]")
elif response.status_code == 404:
    print('Not Found.')



if trigger2.status_code == 200:
    print(">>> HTTP : ",trigger2)
    print(">>> Content : ", json.dumps(trigger2.json()))
    current = ast.literal_eval(json.dumps(trigger2.json()["result"]))
    print("[======================================================================[ Crafted Data ]===================================================================================]")
    current[0].update({"eventType" : "ZabbixHTTP"})
    print (current[0])
    agentData=current[0]
    print("agent data:")
    strAgent=str(agentData).replace("'functions': [{'itemid': '23645', 'function': 'max', 'triggerid': '13545', 'parameter': '#3', 'functionid': '12995'}], ","")
    strAgent= "[" + strAgent + "]"
    strAgent=strAgent.replace("'status': '0', ","")
    strAgent=strAgent.replace("'","\"")
    print(strAgent)
    os.system('curl -X POST -i -H "x-insert-key:NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4" -H "Content-Type: application/json" --data "+ json.dumps(strAgent).json() +" https://insights-collector.newrelic.com/v1/accounts/2482859/events')
    val2=("movii",strAgent.decode('utf-8'))
    cursor.execute(sql,val2)
    db.commit()
    req=requests.post(nrAPI, data=strAgent, headers=nrheaders)
    if req.status_code== 200:
        print("=> Success")
    else:
        print("=> Error")
    print("[========================================================================================================================================================================]")
elif response.status_code == 404:
    print('Not Found.')


if trigger3.status_code == 200:
    print(">>> SSH : ",trigger3)
    print(">>> Content : ", json.dumps(trigger3.json()))
    current = ast.literal_eval(json.dumps(trigger3.json()["result"]))
    print("[======================================================================[ Crafted Data ]===================================================================================]")
    current[0].update({"eventType" : "ZabbixSSH"})
    print (current[0])
    agentData=current[0]
    print("agent data:")
    strAgent=str(agentData).replace("'functions': [{'itemid': '28731', 'function': 'max', 'triggerid': '15986', 'parameter': '#3', 'functionid': '18291'}], ","")
    strAgent= "[" + strAgent + "]"
    strAgent=strAgent.replace("'status': '0', ","")
    strAgent=strAgent.replace("'","\"")
    print(strAgent)
    os.system('curl -X POST -i -H "x-insert-key:NRII-pYm6C-u6URp234A29Quv_kXZHlDw2ZJ4" -H "Content-Type: application/json" --data "+ json.dumps(strAgent).json() +" https://insights-collector.newrelic.com/v1/accounts/2482859/events')
    val3=("movii",strAgent.decode('utf-8'))
    cursor.execute(sql,val3)
    db.commit()
    req=requests.post(nrAPI, data=strAgent, headers=nrheaders)
    if req.status_code== 200:
        print("=> Success")
    else:
        print("=> Error")
    print("[========================================================================================================================================================================]")
elif response.status_code == 404:
    print('Not Found.')
