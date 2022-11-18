import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


from products.models import Product
from products.serializers import ProductSerializer

# @api_view(["GET"])
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # model_data = Product.objects.all().order_by("?").first()
    data = request.data
    serializer = ProductSerializer(data=request.data)
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # # if model_data:
    # #     """
    # #     Now a DRF API VIEW due to @api_view and the return Response(data)
    # #     """
    # #     # data = model_to_dict(model_data)
    # #     # data = model_to_dict(model_data, fields=['id', 'title'])
    # #     data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])

    # #     # before adding model_to_dict
    # #     # data['id'] = model_data.id
    # #     # data['title'] = model_data.title
    # #     # data['content'] = model_data.content
    # #     # data['price'] = model_data.price
    # #     # | ----- this is what is happening ----- |
    # #     # 
    # #     # model instance (model_data)
    # #     # turn a Python dict
    # #     # return JSON to my client
    # #     # END COMMENT
        
    # if instance:
    #     data = ProductsSerializer(instance).data
    # # return JsonResponse(data)
    # # return Response(data)

    if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
        print(serializer.data)
        # data = serializer.data
    # return JsonResponse(data)
        # return Response(data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
    