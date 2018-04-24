### 本项目仿照[proxy_pool](https://github.com/jhao104/proxy_pool), 内容基本一致，仿照主要为了学习新知识


    ______                        ______             _
    | ___ \_                      | ___ \           | |
    | |_/ / \__ __   __  _ __   _ | |_/ /___   ___  | |
    |  __/|  _// _ \ \ \/ /| | | ||  __// _ \ / _ \ | |
    | |   | | | (_) | >  < \ |_| || |  | (_) | (_) || |___
    \_|   |_|  \___/ /_/\_\ \__  |\_|   \___/ \___/ \_____\
                           __ / /
                          /___ /

![](https://img.shields.io/badge/Python-3.x-blue.svg)

测试地址: http://120.79.155.23:5010<br>
博客地址: https://blog.csdn.net/sinat_34200786/article/details/79451499

---
### How to use
```
git clone https://github.com/Dengqlbq/ProxyPool.git
```
```
pip install -r requirements.txt
```

Override the Config.ini

```
[Database]
Host = 127.0.0.1
Port = 6379
Name = proxy
Type = Redis

[GetProxyFunction]
get_proxy_one = 1 
get_proxy_two = 1
get_proxy_three = 1
get_proxy_forth = 1

[ProxyPool]
Host = 0.0.0.0 
Port = 5010
```
```
# For better performance：gunicorn + flask
cd Run
python main.py
```

---
### Use by spider

#### Api

| api | method | Description | arg|
| ----| ---- | ---- | ----|
| / | GET | 欢迎 | None |
| /get | GET | 随机获取一个代理 | None|
| /get_all | GET | 获取所有代理 |None|
| /get_status | GET | 查看代理数量 |None|

#### Code

```python
import requests
import json

proxy = requests.get('http://xxxx:xxxx/get')
proxy = json.loads(proxy)
```

---
### Expand
You can add method to fetch proxy

1. Write your static method in Proxy/ProxyGetter.py

```
class ProxyGetter():
    ...
    @staticmethod
    def get_proxy_one(self):
        """
        Must yield proxy like ip:port
        """
        proxies = ['1.2.3.4:5', '6.7.8.9:10']
        for p in proxies:
            yield p
 ```

2. Registered your method in Config.ini
```
[GetProxyFunction]
get_proxy_one = 1 # 0 to disable
```

