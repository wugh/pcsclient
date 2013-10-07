#!/usr/bin/python2
import httplib2
import ConfigParser
import os


class auth:
    def __init__(self, config_file):
        self.config_file = config_file
        self._read_config()
        self.httpclient = httplib2.Http('.cache')

    def _read_config(self):
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.read(self.config_file)
        self.api_key = config.get('app', 'api_key')
        self.sec_key = config.get('app', 'secret_key')
        self.token_dir = config.get('token', 'dir')
        if not os.path.exists(self.token_dir):
            os.makedirs(self.token_dir)

    def get_code(self):
        code_url = 'https://openapi.baidu.com/oauth/2.0/authorize?'\
                'response_type=code&'\
                'client_id={}&'\
                'redirect_uri=oob&'\
                'scope=netdisk&'\
                'display=popup'.format(self.api_key)
        print('open follow url in web browser\n{}'.format(code_url))
        self.code = raw_input('input your code: ')

    def get_access_token(self):
        self.get_code()
        access_token_url = 'https://openapi.baidu.com/oauth/2.0/token?'\
                'client_id={}&'\
                'client_secret={}&'\
                'grant_type=authorization_code&'\
                'code={}&redirect_uri=oob'.format(self.api_key,
                                                 self.sec_key,
                                                 self.code)
        resp, content = self.httpclient.request(access_token_url,
                                                'GET')
        with open(self.token_dir + '/access_token.txt', 'w') as handle:
            handle.write(content)


if __name__ == '__main__':
    test_auth = auth('pcsclient.cfg')
    test_auth.get_access_token()
