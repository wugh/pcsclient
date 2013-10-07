#!/usr/bin/python2
# -*- coding:utf-8 -*-

from baidupcs import PCS
import json
import argparse
import os

parser = argparse.ArgumentParser(description='This is a simple \
                                 client of baiduyun')
parser.add_argument('-t', '--token',
                    default='token/access_token.txt',
                    help='access token file name')
parser.add_argument('file',
                    help='file need to upload')
args = parser.parse_args()
print(args)


json_content = open(args.token).read()
json_content = json.loads(json_content)
token = json_content['access_token']
pcs = PCS(token)

f = open(args.file)
pcs.upload('/apps/gentoo/' + os.path.basename(args.file), f)
