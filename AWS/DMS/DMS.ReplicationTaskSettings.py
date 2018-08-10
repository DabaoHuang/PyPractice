#!/usr/bin/python3

import boto3
import time

default_region = "<region id>"

try :
    dms_client = boto3.client('dms' , region_name = default_region )

    response = dms_client.modify_replication_tasks(
        ReplicationTaskArn = '<AWS arn>',
        # 這段 json 來自 DMS.GetSettingStringJson.py 所產出的字串中擷取
        ReplicationTaskSettings = '{"TargetMetadata":{ ....... "StatementCacheSize":50}}'
    )

    print(response)

except Exception as e :
    print("DMS tasks error message : %s" %str(e))