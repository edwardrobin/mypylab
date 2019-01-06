#!/usr/bin/env python3

import requests
#r1 = requests.get("http://httpbin.org/get")

headers = { 'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; ADR6400L 4G Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1' }
r2 = requests.get("http://pdawiki.com/forum/member.php?mod=logging&action=login&mobile=2", headers=headers)
print(r2.text.encode('utf-8'))

