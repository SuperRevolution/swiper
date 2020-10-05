from django.http import JsonResponse
from user.logics import send_vcode
from django.core.cache import cache

from user.models import User


def fetch_vcode(request):
    '''给用户发送验证码'''
    phonenum = request.GET.get('phonenum')
    if send_vcode(phonenum):
        return JsonResponse({'code': 0, 'data': None})
    else:
        return JsonResponse({'code': 1000, 'data': '验证码发送失败'})


def submit_vcode(request):
    '''提交验证码,执行登录注册'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    key = 'Vcode-%s' % phonenum
    cached_vcode = cache.get(key)

    if vcode and vcode == cached_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)

        request.session['uid'] = user.id
        return JsonResponse({'code': 0, 'data': user.to_dict()})
    else:
        return JsonResponse({'code':1001,'data':'验证码错误'})


def show_profile(request):
    '''查看个人寂寥'''

    return JsonResponse({'code':0,'data':'测试成功'})


def update_profile(request):
    '''更新个人资料'''
    return JsonResponse()


def qn_token(request):
    '''获取七牛云 Token'''
    return JsonResponse()


def qn_callback(request):
    '''七牛云回调接口'''
    return JsonResponse()
