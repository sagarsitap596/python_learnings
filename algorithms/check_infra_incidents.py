#!/usr/bin/env python

"""
Author: Abhishek Tiwari

Purpose:
This script checks whether the infra is up and running for Incident Collectors and Service

"""
import warnings
import argparse
import re
import sys
import requests
import json
import time
import sys
import boto3
import botocore
import ftplib
from requests import Request, Session
from socket import timeout, gaierror

parser = argparse.ArgumentParser(description="Check infra for a given env")
parser.add_argument("-e", "--env", help="Environment name. eg: aws01_si, aws01_pr, aws05_pr, etc...")
parser.add_argument("-t", "--token", help="Consul ACL Token.")
args = parser.parse_args()

env = args.env.lower()
consul_token = args.token
ftp_user = "oregon"
ftp_password = "Hy6712gjju78"
isError = False
s3_bucket = "collection-deployment-artifacts"
s3_key = "incidentdynamocapacity/dynamo_capacity.txt"

dynamo_db_map = {
                "acv-overrides-feedback-{0}": {
                    "table": "1,1"
                },
                "acv-overrides-{0}": {
                    "table": "10,100"
                },
                "detection-closures-{0}": {
                    "table": "5,5",
                    "countryCodeIndex": "5,5",
                    "geoKeyAndHash": "5,5"
                },
                "detection-superlinks-{0}": {
                    "table": "5,100",
                    "countryCodeIndex": "5,100",
                    "geoKeyAndHash": "5,100",
                    "timeOpenedIndex": "5,100"
                },
                "historicalLinkToSuperlink-Q218-{0}": {
                    "table": "30,1"
                },
                "historicalSuperlinks-Q218-{0}": {
                    "table": "30,1"
                },
                "incident-cancellations-{0}": {
                    "table": "10,20"
                },
                "linears-Q418-{0}": {
                    "table": "10,1"
                },
                "links-Q418-{0}": {
                    "TableStatus": "ACTIVE"
                },
                "locations-Q418-{0}": {
                    "TableStatus": "ACTIVE"
                },
                "rco-alertc-{0}": {
                    "table": "1,1"
                },
                "rco-closures-{0}": {
                    "table": "40,20"
                },
                "rco-historical-closures-{0}": {
                    "table": "1,10",
                    "updateHour": "1,10"
                }
    }

env_table_list = ["incident-cancellations-{0}", "rco-alertc-{0}", "rco-closures-{0}", "rco-historical-closures-{0}"]

def env_mapping():
    if env == "aws01_si" or env == "si":
        return "si"
    elif env == "aws01_pt" or env == "pt":
        return "pt"
    elif env == "aws01_ds" or env == "ds":
        return "ds"
    elif env == "aws01_st" or env == "st1":
        return "st1"
    elif env == "aws05_st" or env == "st5":
        return "st5"
    elif env == "aws01_pr" or env == "pr1":
        return "pr1"
    elif env == "aws05_pr" or env == "pr5":
        return "pr5"
    elif env == "aws01_dv" or env == "dv":
        return "dv"
    else:
        print "Env parameter not recognized. Please check format."
        sys.exit(1)


def processed_rabbitmq_mapping():
    if env == "aws01_si" or env == "si":
        return "http://rabbitmq{0}-processed.si.aws01.traffic.in.here.com:18311"
    elif env == "aws01_pt" or env == "pt":
        return "http://rabbitmq{0}-processed.pt.aws01.traffic.in.here.com:18311"
    elif env == "aws01_ds" or env == "ds":
        return "http://rabbitmq{0}-processed.ds.aws01.traffic.in.here.com:18311"
    elif env == "aws01_st" or env == "st1":
        return "http://rabbitmq{0}-processed.st.aws01.traffic.in.here.com:18311"
    elif env == "aws05_st" or env == "st5":
        return "http://rabbitmq{0}-processed.st.aws05.traffic.in.here.com:18311"
    elif env == "aws01_pr" or env == "pr1":
        return "http://rabbitmq{0}-processed.pr.aws01.traffic.in.here.com:18311"
    elif env == "aws05_pr" or env == "pr5":
        return "http://rabbitmq{0}-processed.pr.aws05.traffic.in.here.com:18311"
    elif env == "aws01_dv" or env == "dv":
        return "http://rabbitmq{0}-processed.dv.aws01.traffic.in.here.com:18311"
    else:
        print "Env parameter not recognized. Please check format."
        sys.exit(1)


def product_rabbitmq_mapping():
    if env == "aws01_si" or env == "si":
        return "http://productrabbit1.si.aws01.traffic.in.here.com:18311"
    elif env == "aws01_pt" or env == "pt":
        return "http://productrabbit1.pt.aws01.traffic.in.here.com:15672"
    elif env == "aws01_ds" or env == "ds":
        return "http://productrabbit1.ds.aws01.traffic.in.here.com:15672"
    elif env == "aws01_st" or env == "st1":
        return "http://productrabbit1.st.aws01.traffic.in.here.com:15672"
    elif env == "aws05_st" or env == "st5":
        return "http://productrabbit1.st.aws05.traffic.in.here.com:15672"
    elif env == "aws01_pr" or env == "pr1":
        return "http://productrabbit1.pr.aws01.traffic.in.here.com:15672"
    elif env == "aws05_pr" or env == "pr5":
        return "http://productrabbit1.pr.aws05.traffic.in.here.com:15672"
    elif env == "aws01_dv" or env == "dv":
        return "http://productrabbit1.dv.aws01.traffic.in.here.com:15672"
    else:
        print "Env parameter not recognized. Please check format."
        sys.exit(1)


def consul_host_mapping():
    if env == "aws01_si" or env == "si":
        return "consul.si.aws01.traffic.in.here.com"
    elif env == "aws01_pt" or env == "pt":
        return "consul.pt.aws01.traffic.in.here.com"
    elif env == "aws01_ds" or env == "ds":
        return "consul.ds.aws01.traffic.in.here.com"
    elif env == "aws01_st" or env == "st1":
        return "consul.st.aws01.traffic.in.here.com"
    elif env == "aws05_st" or env == "st5":
        return "consul.st.aws05.traffic.in.here.com"
    elif env == "aws01_pr" or env == "pr1":
        return "consul.pr.aws01.traffic.in.here.com"
    elif env == "aws05_pr" or env == "pr5":
        return "consul.pr.aws05.traffic.in.here.com"
    elif env == "aws01_dv" or env == "dv":
        return "consul.dv.aws01.traffic.in.here.com"
    else:
        print "Env parameter not recognized. Please check format."
        sys.exit(1)


def ftp_dns_mapping():
    if env == "aws01_si" or env == "si":
        return "incidentftp.si.aws01.traffic.data.here.com"
    elif env == "aws01_pt" or env == "pt":
        return "incidentftp.pt.aws01.traffic.data.here.com"
    elif env == "aws01_ds" or env == "ds":
        return "incidentftp.ds.aws01.traffic.data.here.com"
    elif env == "aws01_st" or env == "st1":
        return "incidentftp.st.aws01.traffic.data.here.com"
    elif env == "aws05_st" or env == "st5":
        return "incidentftp.st.aws05.traffic.data.here.com"
    elif env == "aws01_pr" or env == "pr1":
        return "incidentftp.pr.aws01.traffic.data.here.com"
    elif env == "aws05_pr" or env == "pr5":
        return "incidentftp.pr.aws05.traffic.data.here.com"
    elif env == "aws01_dv" or env == "dv":
        return "incidentftp.dv.aws01.traffic.data.here.com"
    else:
        print "Env parameter not recognized. Please check format."
        sys.exit(1)


def aws_region_mapping():
    if env == "aws01_si" or env == "si":
        return "us-east-1"
    elif env == "aws01_pt" or env == "pt":
        return "us-east-1"
    elif env == "aws01_ds" or env == "ds":
        return "us-east-1"
    elif env == "aws01_st" or env == "st1":
        return "us-east-1"
    elif env == "aws05_st" or env == "st5":
        return "eu-west-1"
    elif env == "aws01_pr" or env == "pr1":
        return "us-east-1"
    elif env == "aws05_pr" or env == "pr5":
        return "eu-west-1"
    elif env == "aws01_dv" or env == "dv":
        return "us-east-1"
    else:
        print "Env parameter not recognized. Please check format."
        sys.exit(1)


def check_rabbitmq_up_running(rabbitmq):
    try:
        global isError
        req = requests.get(rabbitmq)
        print("Rabbitmq " + rabbitmq + " is up and running")
    except:
        print("Error: Rabbitmq " + rabbitmq + " is not responding")
        isError = True


def check_consul_up_running(consul_url, consul_token):
    try:
        global isError
        headers = {"X-Consul-Token": consul_token}
        req = requests.get("http://" + consul_url + "/ui/", headers)
        print("Consul " + consul_url + " is up and running")
    except:
        print("Error: Consul " + consul_url + " is not responding")
        isError = True


def check_ftp_up_running(ftp_url, ftp_user, ftp_password):
    try:
        global isError
        ftp = ftplib.FTP(ftp_url, ftp_user, ftp_password)
        print("Incident FTP " + ftp_url + " is up and running")
    except:
        print("Error: Incident FTP " + ftp_url + " is not responding")
        isError = True


def get_dynamo_capacity_config():
    s3 = boto3.resource('s3')
    try:
        s3.Bucket(s3_bucket).download_file(s3_key, 'dynamo.txt')
    except:
        print("File not found")


def check_dynamo_capacity_config(curated_env, aws_region):
    client = boto3.client('dynamodb',aws_region)
    for dynamo_table, capacity_config_map in dynamo_db_map.items():
        if dynamo_table in env_table_list:
            if curated_env.endswith('1') or curated_env.endswith('5'):
                dynamo_table = dynamo_table.format(curated_env[:-1])
            else:
                dynamo_table = dynamo_table.format(curated_env)
        else:
            dynamo_table = dynamo_table.format(curated_env)
        global isError
        counter = 0
        for attribute, value in capacity_config_map.items():
            try:
                response_json = client.describe_table(
                    TableName=dynamo_table
                )
                if value != "ACTIVE":
                    read_capacity_units = int(value.split(",")[0])
                    write_capacity_units = int(value.split(",")[1])
                if attribute == "table":
                    if response_json[u'Table'][u'ProvisionedThroughput'][u'ReadCapacityUnits'] == read_capacity_units:
                        if response_json[u'Table'][u'ProvisionedThroughput'][u'WriteCapacityUnits'] == write_capacity_units:
                            print("Read/Write capacity units matches for TABLE attribute for Dynamo Table " + dynamo_table)
                        else:
                            print("Error: Write capacity units does not match for TABLE attribute for Dynamo Table " + dynamo_table)
                            isError = True
                    else:
                        print("Error: Read capacity units does not match for TABLE attribute for Dynamo Table " + dynamo_table)
                        print(response_json[u'Table'][u'ProvisionedThroughput'][u'ReadCapacityUnits'])
                        print(read_capacity_units)
                        isError = True
                elif attribute == "TableStatus":
                    if response_json[u'Table'][u'TableStatus'] == value:
                        print("TableStatus attribute is ACTIVE for Dynamo Table " + dynamo_table)
                    else:
                        print("Error: TableStatus attribute is INACTIVE for Dynamo Table " + dynamo_table)
                        isError = True
                else:
                    if response_json[u'Table'][u'GlobalSecondaryIndexes'][counter][u'ProvisionedThroughput'][u'ReadCapacityUnits'] == read_capacity_units:
                        if response_json[u'Table'][u'GlobalSecondaryIndexes'][counter][u'ProvisionedThroughput'][u'WriteCapacityUnits'] == write_capacity_units:
                            print("Read/Write capacity units matches for " + attribute + " attribute for Dynamo Table " + dynamo_table)
                        else:
                            print("Error: Write capacity units does not match for " + attribute + " attribute for Dynamo Table " + dynamo_table)
                            isError = True
                    else:
                        print("Error: Read capacity units does not match for " + attribute + " attribute for Dynamo Table " + dynamo_table)
                        isError = True
                    counter = counter + 1
            except:
                print("Error: Dynamo DB table " + dynamo_table + " does not exists")
                isError = True


if __name__ == "__main__":
    curated_env = env_mapping()
    get_dynamo_capacity_config()

    with open('dynamo.txt', 'r') as myfile:
        data=myfile.read()
    for dynamo_table, capacity_config_map in data.items():
        print(dynamo_table + ", " + capacity_config_map)

    # warnings.simplefilter("ignore")
    # consul_url = consul_host_mapping()
    # ftp_url = ftp_dns_mapping()
    # aws_region = aws_region_mapping()

    # check_ftp_up_running(ftp_url, ftp_user, ftp_password)

    # check_consul_up_running(consul_url, consul_token)

    # rabbitmq_processed = processed_rabbitmq_mapping()
    # product_rabbit = product_rabbitmq_mapping()

    # counterlist = [1, 2, 3]
    # for counter in counterlist:
    #     check_rabbitmq_up_running(rabbitmq_processed.format(counter))

    # check_rabbitmq_up_running(product_rabbit)

    # check_dynamo_capacity_config(curated_env, aws_region)

    # if isError == True:
    #     sys.exit(1)
    # sys.exit(0)
