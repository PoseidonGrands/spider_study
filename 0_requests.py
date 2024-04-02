import requests
import json
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000'
params = {'name': 'sewell', 'password': '123'}
# res = requests.get(url)
# print(res.text)


# res = requests.post(url, params)
# print(res.text, type(res.text))
# print(res.json(), type(res.json()))


# headers = {
#     'user-agent': 'requests',
#     'test': 'hhhhhh'
# }
# res = requests.get(url, headers=headers)

# res = requests.get('http://www.baidu.com')
# # 返回的是响应的头部信息
# print(res.headers)

# requests.get(url, params=params)
# 请求方法中data和json参数的区别
# 1、data：里面是字典：Content-Type等于 application/x-www-form-urlencoded
# requests.get(url, data=params)
# 序列化后成了字符串，没有content-type参数了
# requests.get(url, data=json.dumps(params))

# 2、json：Content-Type 为 application/json
# requests.post(url, json=json.dumps(params))
# 推荐：自动处理参数的 JSON 序列化和设置请求头信息
requests.post(url, json=params)