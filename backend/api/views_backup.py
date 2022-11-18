import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request -> HTTPRequest -> Django
    # print(dir(request))
    # request.body
    print(request.GET) # url query param
    print(request.POST)
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    # print(body)
    # print(data.keys())
    print(data)
    # data['headers'] = request.headers # older versions of Django needed request.META
    print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    # return JsonResponse({"message":"Hi there, this is your Django API response!"})
    return JsonResponse(data)