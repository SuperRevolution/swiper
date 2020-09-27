import time
import json
from hashlib import md5
import requests
from swiper import config

def send_note(phonenum, vcode):
    '''发送短信'''

    args = {
        'appid': config.SD_APPID,
        'to': phonenum,
        'project': config.SD_PROJECT,
        'vars': json.dumps({'vcode': '123456'}),
        'timestamp': int(time.time()),
        'sign_type': config.SD_SIGN_TYPE,
    }

    # 计算签名参数签名
    sorted_args = sorted(args.items())  # 提取每一项
    args_str = '&'.join([f'{key}={value}' for key, value in sorted_args])  # 对参数排序,组合
    sign_str = f'{config.SD_APPID}{config.SD_APPKEY}{args_str}{config.SD_APPID}{config.SD_APPKEY}'.encode('utf8')  # 拼接成待签名字符串
    signature = md5(sign_str).hexdigest()
    args['signature'] = signature

    response = requests.post(config.SD_API, data=args)
    if response.status_code == 200:
        result = response.json()
        print('短信结果', result)
        if result.get('status') == 'success':
            return True
    return False
