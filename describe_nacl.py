import logging
from botocore.exceptions import ClientError
import json
import boto3

import time

#taking input from the user 
REGION= input("Please, Enter the region name where you want to Delete this NACL:-\n=")

# setup the logger
logger_info = logging.getLogger()
logging.basicConfig(level=logging.INFO,format=' %(message)s')

client = boto3.client("ec2", region_name=REGION)


# function to descrine the NACL
def describe_nacl(tag, tag_values, max_items):
    try:
        paginator = client.get_paginator('describe_network_acls')

        response_iterator = paginator.paginate(
            Filters=[{'Name': f'tag:{tag}','Values': tag_values}],
            PaginationConfig={'MaxItems': max_items})

        result = response_iterator.build_full_result()
        list = []

        for i in result['NetworkAcls']:
            list.append(i)
    except ClientError:
        logger_info.exception('Sorry, We are not able to describe the NACL.')
        raise
    else:
        return list



if __name__ == '__main__':
    # taking tag input from user
    TAG_NAME = input("Please, Enter the tag")
    # list to take the tag value from the user
    LST = []    
    # ittration 
    for i in range(0, 1):
        TAG_VALUE = input("Please, Enter the tag value to get the details of the NACL")
        LST.append(TAG_VALUE) # adding the element  
    print(LST)
    MAXIMUM = 10
    network_acls = describe_nacl(TAG_NAME, LST, MAXIMUM)

    for i in range(3):
        logger_info.info(f'Please wait ......  \n We are creating your NACL...\U0001F570')
        time.sleep(5)
    logger_info.info('Hurry, Now This is your Network Acls Details: \U0001F44D ')

    for network_acl in network_acls:
        logger_info.info(json.dumps(network_acl, indent=4) + '\n')