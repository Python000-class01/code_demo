import requests
# SSL 证书
# 如果你将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
requests.get('https://kennethreitz.org', verify=False)
# <Response [200]>

# 客户端证书
# 你也可以指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组：
requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
# <Response [200]>
