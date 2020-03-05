#!/bin/bash
cp -r splunk-sdk-python /opt
#for i in $(cat crontab.txt);
#do
crontab -u root crontab.txt;
#done;
