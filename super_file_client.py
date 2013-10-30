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
parser.add_argument('filename',
                    help='final file name for all file blocks')
parser.add_argument('blocks',
                    nargs='+',
                    help='blocks need to join')
args = parser.parse_args()
print(args)

json_content = open(args.token).read()
json_content = json.loads(json_content)
token = json_content['access_token']
pcs = PCS(token, api_template='https://c.pcs.baidu.com/rest/2.0/pcs/{0}')

finalname = '/apps/gentoo/' + os.path.basename(args.filename)
blocks_md5 = []
for block in args.blocks:
    with open(block) as f:
        resp = pcs.upload_tmpfile(f)
        blocks_md5.append(resp.json()['md5'])
pcs.api_template = 'https://pcs.baidu.com/rest/2.0/pcs/{0}'
pcs.upload_superfile(finalname, blocks_md5)
