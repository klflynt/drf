from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    print(request.GET) # will always grab URL query params
    body = request.body # byte of string JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data --> Python Dict
    except:
        pass
    print(data)
    print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    # return JsonResponse({"message": "Hi there, this is your Django API response!!"})
    return JsonResponse(data)