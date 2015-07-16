# -*- coding: utf-8 -*-

import requests
r = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')
print r.text
