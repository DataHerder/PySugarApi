import json
import requests
import hashlib
import collections
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

class PySugarApi(object):

    def __init__(self, username='', password='', url=None, verify_ssl=True):
        """

        :param development:
        :return:
        """
        self.username = username
        self.password = password
        self.url = url
        self.session_id = None
        if username != '' and password != '' and url is not None:
            self.login(verify_ssl)

    def set_url(self, url=''):
        self.url = url

    def __params(self):
        return


    def post(self, method='login', parameter={}, verify_ssl=True):
        """
        Post parameters to Sugar's API
        :param method:
        :param parameter:
        :return:
        """
        json_data = json.dumps(parameter)
        payload = {
            'method': method,
            'input_type': 'JSON',
            'response_type': 'JSON',
            'rest_data': json_data
        }

        if self.url is None:
            raise RuntimeError('URL to your sugar instance is required.')

        r = requests.post(self.url, data=payload, verify=verify_ssl)
        return r.text


    def login(self, verify_ssl=True):
        m = hashlib.md5(self.password)
        passwrd = m.hexdigest()
        # Unfortunately, Sugar made a poor decision here
        # with their API, it requires this to be in a certain order
        # You wouldn't recognize that if you just copy paste their
        # code from their site, but when you are adapting to a different
        # language rather than PHP, this becomes an obvious oversight.
        # This is squirrelly and should be changed.  There isn't any
        # reason why this should be in a certain order
        payload = collections.OrderedDict()
        payload['user_auth'] = {
            'user_name': 'pcarlton',
            'password': passwrd,
            'version': '1',
        }
        payload['application_name'] = 'RestTest'
        payload['name_value_list'] = []
        text = json.loads(self.post('login', payload, verify_ssl=verify_ssl))
        try:
            self.session_id = text['id']
        except Exception as e:
            pp(text)
            raise Exception('There was an error logging in: ' + e.message)
