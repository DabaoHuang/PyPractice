#!/usr/bin/python3

import boto3
import time

# 輸入主機所在地的 region id
default_region = "<region-ip>"

try:
    dms_client = boto3.client( 'dms' , region_name = default_region )

    response = dms_client.describe_replication_tasks(
        Filters = [
            {
                'Name' : 'replication-task-arn' ,
                'Values' : [
                    '<AWS arn>'
                ]
            },
        ],
    )

    for task in response["ReplicationTasks"] : 
        print(task)

except Exception as e :
    print("DMS tasks error message : %s" %str(e))
