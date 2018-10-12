# coding=utf8

import httplib
import md5
import urllib
import random

appid = '20181012000218310'  # 你的appid
secretKey = '6idUuWd86a9Hiq8rZlJq'  # 你的密钥

httpClient = None
myurl = '/api/trans/vip/translate'
q = 'apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768, 65536)

sign = appid + q + str(salt) + secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
httpClient.request('GET', myurl)

# response是HTTPResponse对象
response = httpClient.getresponse()
httpClient.close()
