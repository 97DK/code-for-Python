import requests
import json

# 定义请求体的内容
payload = {
    "data": [
        {
            "whitelist": "2497",  # 这里可以根据需要填写白名单内容
            "time": 1712553150434  # 时间戳，确保这是正确的值
        }
    ],
    "name": "13553204558"  # 电话号码或其他标识名
}

# 设置请求的URL
url = 'http://123.60.128.114:5100/whitelist/add'

# 发送POST请求，并将payload作为JSON数据发送
response = requests.post(url, json=payload)

# 检查请求是否成功
if response.status_code == 200:
    print("请求成功")
    # 如果需要，你可以打印或处理响应内容
    print(response.json())
else:
    print(f"请求失败，状态码：{response.status_code}")
    # 打印响应的文本内容，这可以帮助你调试问题
    print(response.text)