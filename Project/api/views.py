from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import logging

logger = logging.getLogger('mylog')


@csrf_exempt
def run_job(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'POST':
        try:
            # 解析请求的json格式入参
            data = JSONParser().parse(request)
        except Exception as why:
            print(why.args)
        else:
            content = {'msg': 'SUCCESS'}
            print(data)
            # 返回自定义请求内容content,200状态码
            return JsonResponse(data=content, status=status.HTTP_200_OK)
    # 如果不是post 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])


# 获取等级金额关系
@csrf_exempt
def getPricelist(request):
    # if request.content_type != 'application/json':
    #     return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # pass
    if request.method == 'GET':
        logger.info("This is a info  GET log.")
        from django.db import models
        models.AppsUser.objects.create(wechat_id=123456, role=1, name="gaojb")

        # 数据库获取数据
        # 打包JSON
        pass
    return HttpResponseNotAllowed(permitted_methods=['GET'])


# 发布订单
@csrf_exempt
def submitOrder(request):
    if request.content_type != 'application/json':
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    pass
    if request.method == 'POST':
        # 打包JSON
        # 数据库写数据
        pass
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])


# 接单
@csrf_exempt
def acceptOrder(request):
    if request.content_type != 'application/json':
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    pass
    if request.method == 'POST':
        # 打包JSON
        # 数据库写数据
        pass
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])


# 确认订单
@csrf_exempt
def confirmOrder(request):
    if request.content_type != 'application/json':
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    pass
    if request.method == 'POST':
        # 打包JSON
        # 数据库写数据
        pass
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])


# 交付订单
def payOrder(request):
    if request.content_type != 'application/json':
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    pass
    if request.method == 'POST':
        # 打包JSON
        # 数据库写数据
        pass
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])


# 结单
def finishOrder(request):
    if request.content_type != 'application/json':
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    pass
    if request.method == 'POST':
        # 打包JSON
        # 数据库写数据
        pass
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])


# 沟通
def sendChat(request):
    if request.content_type != 'application/json':
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    pass
    if request.method == 'POST':
        # 打包JSON
        # 数据库写数据
        pass
    else:
        return HttpResponseNotAllowed(permitted_methods=['POST'])
