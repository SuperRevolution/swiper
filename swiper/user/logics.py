import re
import random
from libs.note import send_note
from django.core.cache import cache


def is_phonenum(phonenum):
    '''验证是否是一个正确的手机号'''
    if re.match(r'1[3-9]\d{9}$', phonenum):
        return True
    else:
        return False


def random_code(length=6):
    '''产生指定长度随机码'''
    nums = [str(random.randint(0, 9)) for i in range(length)]
    return ''.join(nums)


def send_vcode(phonenum):
    '''给用户发送短信验证码'''
    if not is_phonenum(phonenum):
        return False
    key = 'Vcode-%s' % phonenum

    # 
    if cache.get(key):
        return True

    # 产生验证码
    vcode = random_code()
    print('随机码', vcode)
    cache.set(key,vcode,600)

    # 向用户手机发送验证码
    return send_note(phonenum, vcode)  # 向手机发送验证码
